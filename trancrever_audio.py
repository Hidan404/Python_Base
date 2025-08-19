import speech_recognition as sr
from pydub import AudioSegment

# Caminho do áudio original (em OGG, MP3, etc)
audio_ogg = "WhatsApp Ptt 2025-08-19 at 10.50.24.ogg"
audio_wav = "audio_temp.wav"

# Converter para WAV (SpeechRecognition entende melhor)
AudioSegment.from_file(audio_ogg).export(audio_wav, format="wav")

# Inicializar reconhecedor
recognizer = sr.Recognizer()

# Carregar o áudio convertido
with sr.AudioFile(audio_wav) as source:
    print("🔊 Reconhecendo áudio...")
    audio_data = recognizer.record(source)

# Reconhecer em português do Brasil
try:
    texto = recognizer.recognize_google(audio_data, language="pt-BR")
    print("✅ Transcrição:")
    print(texto)
except sr.UnknownValueError:
    print("Não consegui entender o áudio.")
except sr.RequestError as e:
    print(f"Erro ao conectar com Google Speech Recognition: {e}")
