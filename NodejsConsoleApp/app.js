const fs = require('fs');
const readline = require('readline-sync');

let contenido = fs.readFileSync('./json/employees.json', 'utf-8');
let datos = JSON.parse(contenido);

//let numero = readline.question('ID del Empleado: ');
//let r = datos.find(r => r.EmployeeID == numero);
//console.log(r);

console.log('Empleados en London: ' + datos.filter(r => r.City == 'London').length);

