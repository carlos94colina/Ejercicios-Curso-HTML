let nombre = 'Borja';
console.log('Hola ' + nombre);
console.log(`Hola ${nombre}`);

console.log('Inicio del programa');

setInterval(function() { console.log('interval'); }, 500);

setTimeout(function() { 
    console.log('Primer Timeout'); }, 3000);
setTimeout(function() { 
    console.log('Segundo Timeout'); }, 0);
setTimeout(function() {
    console.log('Tercer Timeout'); }, 0);
console.log('Fin del programa');

