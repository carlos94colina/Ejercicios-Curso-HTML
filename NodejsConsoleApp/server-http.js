let http = require('http');

http.createServer((req, res) => {
    res.write('<h1>Hola Mundo !!!</h1>');
    res.end();
}).listen(8080);

console.log('Escuchando por el puerto 8080');
