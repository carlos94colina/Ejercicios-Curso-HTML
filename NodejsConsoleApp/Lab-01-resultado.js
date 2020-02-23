//Lab 01 - Resuelto
const rd = require('readline-sync');
let Random = (m) => Math.floor(Math.random() * (m + 1));

function AdivinaNumero2() {
    let n1 = Random(10).toString();
    let n2 = rd.question('Dime un número del 0 al 10: ');

    if(n1 === n2) console.log('Has ACERTADO !!!!!');
    else console.log(`Ufff el número era el ${n1}`); 
}

let AdivinaNumero = () => {
     return new Promise((ok, nok) => {
        let n1 = Random(10).toString();
        let n2 = rd.question('Dime un número del 0 al 10: ');
    
        if(n1 === n2) ok('Has ACERTADO !!!!!');
        else nok(`Ufff el número era el ${n1}`);
    });
};

AdivinaNumero()
    .then(r => { console.log(r); })
    .catch(e => { console.log(e); });

console.log('Fin del Programa');