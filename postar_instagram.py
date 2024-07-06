from instabot import Bot
import os
from dotenv import load_dotenv
import time

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def postar_no_instagram(caminho_imagem, legenda):
    # Obtém as credenciais do arquivo .env
    usuario = os.getenv('INSTAGRAM_USUARIO')
    senha = os.getenv('INSTAGRAM_SENHA')

    # Cria uma instância do bot
    bot = Bot()

    # Função para realizar login e postagem
    def tentar_postar():
        bot.login(username=usuario, password=senha)
        bot.upload_photo(caminho_imagem, caption=legenda)
        bot.logout()

    # Tenta realizar login e postar, com tratamento de exceções
    try:
        tentar_postar()
    except Exception as e:
        if "429" in str(e):
            print("Erro 429: Muitas solicitações. Esperando 10 minutos antes de tentar novamente...")
            time.sleep(600)  # Espera 10 minutos antes de tentar novamente
        else:
            print(f"Erro ao postar no Instagram: {e}")
        try:
            tentar_postar()
        except Exception as e:
            print(f"Falha ao tentar novamente: {e}")
