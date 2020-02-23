const axios = require('axios');
const read = require('readline-sync');
require('colors');

let cp = read.question('Código Postal: ', { encoding: 'UTF-8'});
let url = 'https://api.zippopotam.us/es/' + cp;

axios.get(url)
    .then(json => {
        console.log('El código postal '.blue 
            + cp.red + ' pertenece a '.blue 
            + json.data.places[0]['place name'].red);
    })
    .catch(e => console.log(`El código postal ${cp} no pertenece a ninguna ciudad.`.red.bgYellow));