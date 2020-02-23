let getTipoInteres = () => {
 return new Promise((resolve, reject) => {
     reject('Error de acceso a los datos');
     //setTimeout(() => resolve('Tipo de Interes 6%'), 3000);
 });
}

let Interes = async() => {
    return await getTipoInteres();
};

console.log('Pedir tipo de Interes');

Interes()
    .then((res) => { console.log(res); })
    .catch((error) => { console.log(error); });

console.log('Calcular Intereses');