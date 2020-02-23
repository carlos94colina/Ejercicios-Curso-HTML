var Medidas = {
    Suma: 0,
    Media: 0,
    Maximo: 0,
    Minimo: 0,
    Elementos: 0
};

var numeros = [1, 56, 200, 12, 65, 890, 23, 1, 23, 112, 69, 34, 98];

let Calculos = (n) => {
    return new Promise((ok, nok) => {
        try {
            for(var i = 0; i < n.length; i++)
            {
                if(i === 0) Medidas.Minimo = n[0];
                if(n[i] < Medidas.Minimo) Medidas.Minimo = n[i];
                if(n[i] > Medidas.Maximo) Medidas.Maximo = n[i];
                Medidas.Suma += n[i]
            }
            Medidas.Media = Medidas.Suma / n.length;
            Medidas.Elementos = n.length;
            ok(JSON.stringify(Medidas));
        } catch {
            nok('Ufff, error');
        }
    });
};

Calculos(numeros)
    .then(r => console.log(r))
    .catch(e => console.log(e));