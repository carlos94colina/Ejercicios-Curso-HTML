//Lab 01 
const rd = require('readline-sync');

let Random = (m) => Math.floor(Math.random() * (m + 1)); 
let testigo = false;

while(!testigo) {
    let n1 = Random(10).toString();
    let n2 = rd.question('Dime un número del 0 al 10: ');

    if(n1 === n2) {
        console.log('Has ACERTADO !!!!!');
        testigo = true;
    } else console.log(`Ufff el número era el ${n1}`);
}