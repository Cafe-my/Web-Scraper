import requests
from bs4 import BeautifulSoup

class Produto:
    def __init__(self, url):
         self.url = url
         self.soup = None
         self.titulo = None
         self.preco = None
         self.descricao = None
         self.imagem = None

    def requisicao(self):
    # headers para simular comportamento humano e prevenir o site de barrar a requisição por suspeita de bot
        headers = {
        'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/115.0.0.0 Safari/537.36'
            ),
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.google.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print(f'Erro: {response.status_code}')

    def extrair_dados(self):
        if self.soup is None:
            self.requisicao()
        self.titulo = self.soup.find('h1', class_="product-name").text.strip()
        self.preco = self.soup.find('span', class_="saleInCents-value").text.strip()
        self.descricao = self.soup.find('div', class_="feature__main-content").text.strip()
        self.imagem = self.soup.find('div', class_= "image-presenter__carousel").img['src']
    

if __name__ == '__main__':
    url = 'https://www.netshoes.com.br/p/mochila-nike-heritage-preto+branco-2IC-3604-026'
    produto = Produto(url)
    produto.extrair_dados()
    print(f'Título do produto: {produto.titulo} \nDescrição: {produto.descricao} \nPreço: {produto.preco} \nUrl da Imagem: {produto.imagem}')