const axios = require('axios');
const read = require('readline-sync');

let ciudad = read.question('Nombre de la Ciudad: ');

let url = 'https://api.openweathermap.org/data/2.5/weather?q=' + ciudad;
url += '&units=metric&appid=6048d91c3f7c26deaa1d8a6ac38f06b2';

axios.get(url)
    .then(json => {
        console.log(`Temperatura en ${ciudad}: ${json.data.main.temp}`);
    })
    .catch(e => console.log(e));