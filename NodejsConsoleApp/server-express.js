const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('<h1>Hola Mundo !!!</h1>')
});
//app.listen(3000);
//console.log('Escuchando por el puerto 3000');

/////////////////////////////////////////////////////////////////////////////////

const app2 = express();

app2.use(express.static(__dirname + '/wwwroot'));
app2.listen(8000, () => console.log('Escuchando por el puerto 8000'));




