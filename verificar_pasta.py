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
                nome_arquivo_legenda = '_'.join(partes_arquivo[2:])

                # Converte a string de data e hora em um objeto datetime
                data_hora_postagem = datetime.strptime(data_hora_str, "%d%m%Y_%H%M")

                # Se o horário for igual ou já tiver passado, realiza a postagem
                if datetime.now() >= data_hora_postagem:
                    caminho_imagem = os.path.join(caminho_pasta, nome_arquivo)
                    legenda = ""

                    # Verifica se o nome do arquivo de legenda não é "0"
                    if nome_arquivo_legenda != "0":
                        caminho_legenda = os.path.join(caminho_pasta, nome_arquivo_legenda + '.txt')
                        
                        # Verifica se o arquivo de legenda existe antes de tentar abri-lo
                        if os.path.exists(caminho_legenda):
                            with open(caminho_legenda, 'r', encoding='utf-8') as f:
                                legenda = f.read()
                        else:
                            print(f"Arquivo de legenda {caminho_legenda} não encontrado, publicando sem legenda.")

                    # Realiza a postagem no Instagram
                    try:
                        postar_no_instagram(caminho_imagem, legenda)
                        
                        # Imprime a mensagem de log
                        print(f"Publicação realizada: {nome_arquivo}")
                        
                        # Remove a imagem após a postagem
                        os.remove(caminho_imagem)
                        
                        # Remove o arquivo de legenda se existir
                        if nome_arquivo_legenda != "0" and os.path.exists(caminho_legenda):
                            os.remove(caminho_legenda)

                    except Exception as e:
                        print(f"Erro ao postar a imagem {nome_arquivo}: {e}")

        # Espera um minuto antes de checar a pasta novamente
        time.sleep(60)
