//Lab 02 - Número Par ?????

let EsPar = (n) => {
     return new Promise((resolve, reject) => {
        let r = n % 2;
        if(r == 0) resolve(`El número ${n} es Par`);
        else reject(`El número ${n} es Impar`);
    });
};

EsPar(11)
    .then(r => { console.log(r); })
    .catch(e => { console.log(e); });

console.log('Fin del Programa');