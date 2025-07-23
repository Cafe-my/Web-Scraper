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
        try{
            const response = await axios.get(this.url);
            const html = response.data;
            const $ = cheerio.load(html);
            this.titulo = $('.showcase__description > h1').text().trim();
            this.descricao = $('.feature__main-content').text().trim();
            this.preco = $('.saleInCents-value').first().text().trim();
            this.imagem = $('.image-presenter__carousel img').attr('src');
        }
        catch (erro) {
            console.error("Erro:", erro.message);
        }
    }
}

(async() => {
    const url = 'https://www.netshoes.com.br/p/mochila-nike-heritage-preto+branco-2IC-3604-026';
    const produto = new Produto(url);
    await produto.extrair_dados();  
    console.log(`Título do produto: ${produto.titulo}\n`);  
    console.log(`Descrição: ${produto.descricao}\n`);
    console.log(`Preço: ${produto.preco}\n`);
    console.log(`Url da imagem: ${produto.imagem}`);
})()
