"""
Módulo de transcrição de áudio com suporte a múltiplos formatos e engines.

Recursos:
    - Conversão automática para WAV (OGG, MP3, M4A, FLAC, etc.)
    - Transcrição via Google Speech Recognition ou Sphinx (offline)
    - Suporte a áudios longos divididos em chunks
    - Salva transcrição em arquivo .txt
    - Logs detalhados com timestamps
    - Limpeza opcional de arquivos temporários
"""

from __future__ import annotations

import argparse
import logging
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional

import speech_recognition as sr
from pydub import AudioSegment

# ---------------------------------------------------------------------------
# Configuração de logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constantes / dicionário de engines suportados
# ---------------------------------------------------------------------------

SUPPORTED_ENGINES: dict[str, str] = {
    "google": "Reconhecimento via Google Web Speech API (requer internet)",
    "sphinx": "Reconhecimento offline via CMU Sphinx (mais limitado)",
}

FORMATOS_SUPORTADOS = (".ogg", ".mp3", ".wav", ".m4a", ".flac", ".aac", ".wma")

# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------


def _validar_arquivo_audio(caminho: Path) -> None:
    """Valida se o arquivo de áudio existe e tem extensão conhecida."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    if not caminho.is_file():
        raise IsADirectoryError(f"O caminho informado é um diretório: {caminho}")
    if caminho.suffix.lower() not in FORMATOS_SUPORTADOS:
        log.warning(
            "Extensão '%s' não está na lista de formatos conhecidos %s. "
            "Tentando conversão mesmo assim.",
            caminho.suffix,
            FORMATOS_SUPORTADOS,
        )


def _tamanho_segundos(caminho: Path) -> float:
    """Retorna a duração aproximada do áudio em segundos."""
    try:
        audio = AudioSegment.from_file(str(caminho))
        return len(audio) / 1000.0
    except Exception:
        return 0.0


def converter_para_wav(
    origem: Path,
    destino: Optional[Path] = None,
    formato: Optional[str] = None,
) -> Path:
    """
    Converte um arquivo de áudio para WAV.

    Args:
        origem: Caminho do arquivo de áudio original.
        destino: Caminho de saída (opcional). Se omitido, cria um temp file.
        formato: Formato de origem (opcional, detectado pela extensão).

    Returns:
        Caminho do arquivo WAV gerado.
    """
    if destino is None:
        destino = Path(tempfile.mkstemp(suffix=".wav", prefix="transcricao_")[1])

    log.info("Convertendo %s -> %s ...", origem.name, destino.name)
    try:
        AudioSegment.from_file(str(origem), format=formato).export(
            str(destino), format="wav"
        )
    except Exception as exc:
        raise RuntimeError(f"Falha na conversão de {origem.name} para WAV") from exc

    log.info("Conversão concluída: %s", destino)
    return destino


def transcrever_audio(
    arquivo_wav: Path,
    engine: str = "google",
    language: str = "pt-BR",
    chunk_minutos: int = 3,
) -> str:
    """
    Transcreve um arquivo WAV usando o engine especificado.

    Args:
        arquivo_wav: Caminho para o arquivo WAV.
        engine: Engine de reconhecimento ('google' ou 'sphinx').
        language: Código do idioma (ex.: 'pt-BR', 'en-US').
        chunk_minutos: Duração máxima de cada chunk em minutos para áudios longos.

    Returns:
        Texto transcrito completo.
    """
    recognizer = sr.Recognizer()
    duracao = _tamanho_segundos(arquivo_wav)
    log.info("Duração do áudio: %.1f segundos", duracao)

    # Ajusta energia ambiente para melhor precisão
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    # Abre o áudio
    with sr.AudioFile(str(arquivo_wav)) as source:
        # Se o áudio for curto, processa inteiro de uma vez
        chunk_seg = chunk_minutos * 60
        if duracao <= chunk_seg:
            log.info("🔊 Processando áudio completo...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.record(source)
            return _reconhecer(recognizer, audio_data, engine, language)

        # Áudio longo: divide em chunks
        log.info(
            "🔊 Áudio longo detectado. Dividindo em chunks de %d minuto(s)...",
            chunk_minutos,
        )
        texto_completo: list[str] = []
        inicio = 0.0

        while inicio < duracao:
            fim = min(inicio + chunk_seg, duracao)
            log.info(
                "Processando chunk %.1fs - %.1fs (%.1f%%) ...",
                inicio,
                fim,
                (fim / duracao) * 100,
            )
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio_chunk = recognizer.record(source, duration=chunk_seg, offset=inicio)
            try:
                parcial = _reconhecer(recognizer, audio_chunk, engine, language)
                texto_completo.append(parcial)
                log.info("Chunk OK — %d caracteres", len(parcial))
            except sr.UnknownValueError:
                log.warning("Chunk %.1fs-%.1fs: áudio não compreendido", inicio, fim)
            except Exception:
                log.exception("Erro inesperado no chunk %.1fs-%.1fs", inicio, fim)
            inicio = fim

        return " ".join(texto_completo).strip()


def _reconhecer(
    recognizer: sr.Recognizer,
    audio_data: sr.AudioData,
    engine: str,
    language: str,
) -> str:
    """
    Dispara o reconhecimento de fala no engine escolhido.

    Args:
        recognizer: Instância do Recognizer.
        audio_data: Dados de áudio capturados.
        engine: 'google' ou 'sphinx'.
        language: Código do idioma.

    Returns:
        Texto reconhecido.

    Raises:
        sr.UnknownValueError: Se o áudio não pôde ser compreendido.
        sr.RequestError: Se houve erro de conexão (apenas Google).
    """
    if engine == "google":
        return recognizer.recognize_google(audio_data, language=language)
    elif engine == "sphinx":
        return recognizer.recognize_sphinx(audio_data, language=language)
    else:
        raise ValueError(f"Engine desconhecido: '{engine}'. Use 'google' ou 'sphinx'.")


def salvar_transcricao(texto: str, caminho: Path) -> None:
    """
    Salva o texto transcrito em um arquivo.

    Args:
        texto: Texto a ser salvo.
        caminho: Caminho de saída.
    """
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(texto, encoding="utf-8")
    log.info("✅ Transcrição salva em: %s", caminho.resolve())


# ---------------------------------------------------------------------------
# Interface de linha de comando
# ---------------------------------------------------------------------------


def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos da CLI."""
    parser = argparse.ArgumentParser(
        description="Transcreve áudio para texto usando reconhecimento de fala.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s audio.ogg
  %(prog)s audio.mp3 -l en-US -o transcricao.txt
  %(prog)s audio.m4a --engine sphinx --no-cleanup
  %(prog)s audio.wav --chunk-minutos 5 -v
        """,
    )

    parser.add_argument(
        "audio",
        type=str,
        help="Caminho do arquivo de áudio (OGG, MP3, WAV, M4A, FLAC, AAC, WMA)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Caminho do arquivo de saída .txt (default: <audio_nome>_transcricao.txt)",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        default="pt-BR",
        help="Código do idioma (ex.: pt-BR, en-US, es-ES) [default: pt-BR]",
    )
    parser.add_argument(
        "--engine",
        type=str,
        choices=list(SUPPORTED_ENGINES.keys()),
        default="google",
        help="Engine de reconhecimento de fala [default: google]",
    )
    parser.add_argument(
        "--chunk-minutos",
        type=int,
        default=3,
        help="Duração de cada chunk em minutos para áudios longos [default: 3]",
    )
    parser.add_argument(
        "--no-cleanup",
        action="store_true",
        help="Não remover o arquivo WAV temporário após a transcrição",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Ativa logs mais detalhados (DEBUG)",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    """
    Função principal do script.

    Args:
        argv: Lista de argumentos (padrão: sys.argv[1:]).

    Returns:
        Código de saída (0 = sucesso, 1 = erro).
    """
    parser = criar_parser()
    args = parser.parse_args(argv)

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        log.debug("Modo verboso ativado.")

    # --- 1. Validar arquivo de entrada ---
    caminho_audio = Path(args.audio).resolve()
    try:
        _validar_arquivo_audio(caminho_audio)
    except (FileNotFoundError, IsADirectoryError) as exc:
        log.error("❌ %s", exc)
        return 1

    log.info("🎤 Arquivo de áudio: %s", caminho_audio)
    log.info("🌐 Idioma: %s  |  Engine: %s", args.language, args.engine)

    # --- 2. Determinar caminho de saída ---
    if args.output:
        caminho_saida = Path(args.output).resolve()
    else:
        caminho_saida = caminho_audio.with_name(
            f"{caminho_audio.stem}_transcricao.txt"
        ).resolve()

    # --- 3. Converter para WAV (se necessário) ---
    wav_temp: Optional[Path] = None
    try:
        if caminho_audio.suffix.lower() == ".wav":
            log.info("Arquivo já está em WAV, pulando conversão.")
            arquivo_wav = caminho_audio
        else:
            arquivo_wav = converter_para_wav(caminho_audio)
            wav_temp = arquivo_wav

        # --- 4. Transcrever ---
        inicio = time.perf_counter()
        texto = transcrever_audio(
            arquivo_wav,
            engine=args.engine,
            language=args.language,
            chunk_minutos=args.chunk_minutos,
        )
        duracao = time.perf_counter() - inicio

        if not texto:
            log.warning("⚠️  Nenhum texto foi reconhecido no áudio.")
        else:
            log.info(
                "✅ Transcrição concluída em %.1f segundos (%d caracteres).",
                duracao,
                len(texto),
            )
            print("\n" + "=" * 60)
            print("📝 TRANSCRIÇÃO:")
            print("=" * 60)
            print(texto)
            print("=" * 60 + "\n")

            # --- 5. Salvar transcrição ---
            salvar_transcricao(texto, caminho_saida)

    except sr.UnknownValueError:
        log.error("❌ Não foi possível entender o áudio (idioma incorreto ou áudio ruidoso).")
        return 1
    except sr.RequestError as exc:
        log.error("❌ Erro de conexão com o serviço de reconhecimento: %s", exc)
        return 1
    except RuntimeError as exc:
        log.error("❌ %s", exc)
        return 1
    except Exception:
        log.exception("❌ Erro inesperado durante a transcrição.")
        return 1
    finally:
        # --- 6. Limpeza ---
        if wav_temp and wav_temp.exists() and not args.no_cleanup:
            try:
                wav_temp.unlink()
                log.debug("Arquivo temporário removido: %s", wav_temp)
            except OSError:
                log.warning(
                    "Não foi possível remover o arquivo temporário: %s", wav_temp
                )

    return 0


# ---------------------------------------------------------------------------
# Ponto de entrada
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(main())
