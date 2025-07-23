import requests
from bs4 import BeautifulSoup

def requisicao(url):
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
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dados_pagina = BeautifulSoup(response.text, 'html.parser')
        return dados_pagina
    else:
        print(f'Erro: {response.status_code}')

def extrair_dados(dados):
    titulo = dados.find('h1', class_="product-name").text.strip()
    preco = dados.find('span', class_="saleInCents-value").text.strip()
    descricao = dados.find('div', class_="feature__main-content").text.strip()
    imagem = dados.find('img', alt="Mochila Nike Heritage")['src']
    return imagem

if __name__ == '__main__':
    url = 'https://www.netshoes.com.br/p/mochila-nike-heritage-preto+branco-2IC-3604-026'
    dados_pagina = requisicao(url)
    divs = extrair_dados(dados_pagina)
    # for div in divs:
    print(divs)