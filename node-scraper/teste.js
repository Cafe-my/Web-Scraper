const axios = require("axios");
const cheerio = require("cheerio");

async function extrair_dados(url) {
    const response = await axios.get(url);
    const html = response.data;
    console.log(html)
}

const url = 'https://www.netshoes.com.br/p/mochila-nike-heritage-preto+branco-2IC-3604-026'
extrair_dados(url)