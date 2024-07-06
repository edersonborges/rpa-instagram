
# Instagram Automation Project

Este projeto em Python automatiza postagens no Instagram. A automação verifica uma pasta específica para imagens e arquivos de legenda, e posta as imagens no Instagram com base no horário especificado no nome do arquivo.

## Estrutura do Projeto

```
instagram_automation/
├── .env
├── main.py
├── postar_instagram.py
├── verificar_pasta.py
├── imagens/  # Pasta onde você colocará as imagens e os arquivos de legenda
```

### Arquivos

- **.env**: Armazena variáveis de ambiente, incluindo credenciais do Instagram.
- **main.py**: Arquivo principal que inicia a automação.
- **postar_instagram.py**: Contém a função para postar no Instagram.
- **verificar_pasta.py**: Contém a lógica para verificar a pasta e realizar postagens automáticas.
- **imagens/**: Pasta onde as imagens e arquivos de legenda devem ser colocados.

## Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/instagram_automation.git
cd instagram_automation
```

### 2. Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
```

- No Windows:
  ```bash
  venv\Scripts\activate
  ```
- No macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
INSTAGRAM_USUARIO=seu_usuario
INSTAGRAM_SENHA=sua_senha
```

### 5. Estrutura dos Arquivos de Imagem e Legenda

Coloque as imagens na pasta `imagens` com o seguinte formato de nome:

```
ddMMyyyy_HHmm_nome_do_arquivo.jpg
```

Exemplo:

```
06072024_2008_legendaarquivo.jpg
```

Crie um arquivo de texto correspondente com a legenda da imagem:

```
legendaarquivo.txt
```

### 6. Executar o Projeto

```bash
python main.py
```

## Funcionamento

- O script `main.py` inicia a automação, que continuamente verifica a pasta `imagens`.
- Se encontrar uma imagem cujo horário de postagem (indicado no nome do arquivo) seja igual ou anterior ao horário atual, a imagem será postada no Instagram com a legenda correspondente.
- Após a postagem, a imagem e o arquivo de legenda são removidos da pasta `imagens`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
