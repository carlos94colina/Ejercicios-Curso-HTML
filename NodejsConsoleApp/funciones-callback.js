let usuario = {
    id: 'BORJA',
    nombre : 'Borja',
    apellido1 : 'Cabeza',
    apellido2 : 'Rozas'
};

let getUsuarioById = (id, callback) => {
    if(id != 'BORJA') callback(`El usuario ${id} no exite`, null);
    else callback(null, usuario);
};

getUsuarioById('BORJA', (e, data) => {
    if(e) console.log(e);
    else console.log(data);
});
