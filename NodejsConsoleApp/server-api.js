const express = require('express');
const app = express();

const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/northwind', { useNewUrlParser: true, 	useUnifiedTopology: true }, () => console.log('CONECTADO con mongoDB'));

const CustomersSchema = new mongoose.Schema({
    _id: {type: mongoose.Schema.Types.ObjectId},
    CustomerID: { type: mongoose.Schema.Types.String, require: true, unique: true},
    CompanyName: String,
    ContactName: String,
    ContactTitle: String,
    Address: String,
    City: String,
    Region: String,
    PostalCode: String,
    Country: String,
    Phone: String,
    Fax: String
});

var Customers = mongoose.model('Customers', CustomersSchema);

app.get('/clientes', (req, res) => { 
    Customers.find({}, function(error, documents) {
        res.send(documents);
    });
});

app.get('/clientes/:id', (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:8000');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
    res.setHeader('Access-Control-Allow-Credentials', true);

    Customers.find({CustomerID: req.params['id']}, function(error, documents) {
        res.send(documents);
    });
});

app.get('/', (req, res) => { res.send('get'); });
app.post('/', (req, res) => { res.send('post'); });
app.put('/', (req, res) => { res.send('put'); });
app.delete('/', (req, res) => { res.send('delete'); });

app.listen(3000, () => console.log('Escuchando por el puerto 3000'));