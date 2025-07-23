const axios = require("axios");
const cheerio = require("cheerio");

class Produto{
    constructor(url){
        this.url = url;
        this.titulo = null;
        this.descricao = null;
        this.preco = null;
        this.imagem = null;
    }
    async extrair_dados() {
        const response = await axios.get(this.url);
        const html = response.data;
        const $ = cheerio.load(html);
        this.titulo = $('.showcase__description > h1').text().trim();
        this.descricao = $('.feature__main-content').text().trim();
        this.preco = $('.saleInCents-value').first().text().trim();
        this.imagem = $('.image-presenter__carousel img').attr('src');
    }
}

const url = 'https://www.netshoes.com.br/p/mochila-nike-heritage-preto+branco-2IC-3604-026';
async function main() {
  const produto = new Produto(url);
  await produto.extrair_dados();  
  console.log(produto.titulo);  
  console.log(produto.descricao);
  console.log(produto.preco);
  console.log(produto.imagem);
}

main();

// const produto = new Produto(url)
// produto.extrair_dados()
// console.log(produto.titulo)