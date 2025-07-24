# Web Scraper

Este repositório contém dois projetos de web scraping, um em Python e outro em Node.js, que extraem informações de produtos de páginas do site Netshoes (https://www.netshoes.com.br/).

## Estrutura dos Projetos

- `python-scraper/`: Web scraper em Python
  - `produto_scraper.py`: Código principal para extração de dados de produtos
  - `requirements.txt`: Dependências do projeto
- `node-scraper/`: Web scraper em Node.js
  - `produto_scraper.js`: Código principal para extração de dados de produtos
  - `package.json`: Dependências do projeto
- `Outputs/`: prints dos outputs dos projetos

## Objetivo

Os scrapers têm como objetivo acessar páginas de produtos da Netshoes, extrair informações como título, descrição, preço e imagem, e exibir esses dados no terminal.

## Como Executar

### Passos Iniciais

1. Faça o download ou clone o repositório:
   ```powershell
   git clone https://github.com/Cafe-my/Web-Scraper.git
   ```
   Ou baixe o ZIP pelo GitHub e extraia os arquivos.

### Python Scraper

2. Acesse a pasta do scraper Python:
   ```powershell
   cd "Web-Scraper/python-scraper"
   ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
4. Execute o script:
   ```powershell
   python produto_scraper.py
   ```

### Node.js Scraper

2. Acesse a pasta do scraper Node.js:
   ```powershell
   cd "Web-Scraper/node-scraper"
   ```
3. Instale as dependências:
   ```powershell
   npm install
   ```
4. Execute o script:
   ```powershell
   node produto_scraper.js
   ```

## Como Testar

- Para ambos os projetos, basta executar o respectivo script conforme instruções acima. Os dados extraídos serão exibidos no terminal.
- Para testar com outras páginas, altere a URL de cada scraper.

## Observações

- Os scrapers utilizam bibliotecas populares para requisições HTTP e manipulação de HTML (`requests`/`BeautifulSoup` para Python, `axios`/`cheerio` para Node.js).
- Certifique-se de que a estrutura da página alvo não mudou, pois isso pode afetar a extração dos dados.

---

Desenvolvido por Cafe-my.
