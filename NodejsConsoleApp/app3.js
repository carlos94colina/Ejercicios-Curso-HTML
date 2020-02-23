const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/northwind', 
    { useNewUrlParser: true, useUnifiedTopology: true }, 
    () => console.log('CONECTADO mongoDB'));

const Schema = mongoose.Schema;

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

Customers.find({CustomerID: 'ANATR'}, function(error, comments) {
    console.log(comments);
});
