import flet as ft
import dados_api
import os
import json

def main(page: ft.Page):
    page.title = "Previsão do Tempo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 600
    page.window_resizable = False


    

    dados = os.path.abspath(__file__)
    dados = os.path.dirname(dados)
    caminho = os.path.join(dados, "dados.json")
    if not os.path.exists(caminho):
        os.makedirs(caminho)

      
    
    def clima(e):
        cidade = cidade_input.value if cidade_input.value else "São Paulo"
        dados_api.salvar_dados_json(cidade)
        with open(caminho, "r") as arquivo:
            dados = json.load(arquivo)
            resultado_text.value = f"\n📍 Clima por hora em {cidade.title()}\n"
            for dia in dados['weather']:
                resultado_text.value += f"\n📅 Data: {dia['date']}\n"
                for hora in dia['hourly']:
                    hora_formatada = f"{int(hora['time'])//100:02d}:00"
                    temp = hora['tempC']
                    desc = hora['weatherDesc'][0]['value']
                    resultado_text.value += f"🕒 {hora_formatada} → 🌡️ {temp}°C - {desc}\n"
        page.update()
    
    cidade_input = ft.TextField(label="Digite o nome da cidade", width=300)
    botao_clima = ft.ElevatedButton(text="Consultar Clima", on_click=clima)
    resultado_text = ft.Text(value="", size=20, color=ft.Colors.BLUE)

    page.add(cidade_input, botao_clima, resultado_text)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")