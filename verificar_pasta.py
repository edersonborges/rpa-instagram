import os
import time
from datetime import datetime
from postar_instagram import postar_no_instagram

def verificar_e_postar_imagens(caminho_pasta):
    while True:
        for nome_arquivo in os.listdir(caminho_pasta):
            if nome_arquivo.endswith(".jpg") or nome_arquivo.endswith(".jpeg") or nome_arquivo.endswith(".png"):
                # Extrai a data, hora e o nome do arquivo de legenda
                partes_arquivo = nome_arquivo.split('_')
                data_hora_str = partes_arquivo[0] + '_' + partes_arquivo[1]
                nome_arquivo_legenda = '_'.join(partes_arquivo[2:]) + '.txt'

                # Converte a string de data e hora em um objeto datetime
                data_hora_postagem = datetime.strptime(data_hora_str, "%d%m%Y_%H%M")

                # Se o horário for igual ou já tiver passado, realiza a postagem
                if datetime.now() >= data_hora_postagem:
                    caminho_imagem = os.path.join(caminho_pasta, nome_arquivo)
                    caminho_legenda = os.path.join(caminho_pasta, nome_arquivo_legenda)

                    # Lê a legenda do arquivo txt
                    with open(caminho_legenda, 'r', encoding='utf-8') as f:
                        legenda = f.read()

                    # Realiza a postagem no Instagram
                    postar_no_instagram(caminho_imagem, legenda)

                    # Remove a imagem e o arquivo de legenda após a postagem
                    os.remove(caminho_imagem)
                    os.remove(caminho_legenda)

        # Espera um minuto antes de checar a pasta novamente
        time.sleep(60)
