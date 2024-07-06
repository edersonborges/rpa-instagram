from instabot import Bot
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def postar_no_instagram(caminho_imagem, legenda):
    # Obtém as credenciais do arquivo .env
    usuario = os.getenv('INSTAGRAM_USUARIO')
    senha = os.getenv('INSTAGRAM_SENHA')

    # Cria uma instância do bot
    bot = Bot()

    # Realiza login no Instagram
    bot.login(username=usuario, password=senha)

    # Realiza a postagem
    bot.upload_photo(caminho_imagem, caption=legenda)

    # Logout
    bot.logout()
