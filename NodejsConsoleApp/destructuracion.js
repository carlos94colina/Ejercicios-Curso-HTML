let usuario = {
    nombre : 'Borja',
    apellido1 : 'Cabeza',
    apellido2 : 'Rozas'
};

//let nombre = usuario.nombre;
//let apellido1 = usuario.apellido1;

let { nombre, apellido1 } = usuario;
console.log(`${nombre} ${apellido1}`);

let { nombre: n, apellido1: a } = usuario;
console.log(`${n} ${a}`);

