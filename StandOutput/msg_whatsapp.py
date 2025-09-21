# Importe a biblioteca pywhatkit
import pywhatkit as kit

# Número de telefone do destinatário (inclua o código do país)
telefone_destinatario = "+5511991444502"

# Mensagem que você deseja enviar
mensagem = "Olá, este é um Bot Whatsapp Python!"

# Envie a mensagem
kit.sendwhatmsg(telefone_destinatario, mensagem, 20, 25)