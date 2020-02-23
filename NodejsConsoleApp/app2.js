const fs = require('fs');
const readline = require('readline-sync');

let numero = readline.question('Número: ');
let texto = '';

for (let i = 1; i < 11; i++) {
    texto += `${numero} x ${i} = ${ numero * i}\n`;
    console.log(`${numero} x ${i} = ${numero * i}`);
}

fs.writeFileSync(`./out/tabla-multiplicar-${numero}.txt`, texto);