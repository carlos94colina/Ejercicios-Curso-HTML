using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Newtonsoft.Json;

namespace Exam.WebApplication.api
{
    /// <summary>
    /// Descripción breve de secretos
    /// </summary>
    public class secretos : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            int estado = 200;
            string mensaje = "";

            try
            {
                string param = context.Request.Params["p"];
                if (param != null) param = param.ToLower();

                switch (param) 
                {
                    case "secreto de madrid":
                        mensaje = "Además del archiconocido ángel caído del Retiro, hay una estatua en Madrid (en la azotea de Milaneses, 3, esq. Mayor) que representa mucho mejor lo que supone un verdadero tortazo contra el suelo.";
                        break;
                    case "secreto de new york":
                        mensaje = "La estación abandonada de Old City Hall despierta gran curiosidad entre los viajeros. A pesar de que cerró en 1945, los techos abovedados y las elegantes paredes de esta estación han sobrevivido al paso del tiempo, una cápsula de otra época en el subsuelo de la ciudad.";
                        break;
                    case "secreto de nueva work":
                        mensaje = "La estación abandonada de Old City Hall despierta gran curiosidad entre los viajeros. A pesar de que cerró en 1945, los techos abovedados y las elegantes paredes de esta estación han sobrevivido al paso del tiempo, una cápsula de otra época en el subsuelo de la ciudad.";
                        break;
                    case "secreto de tokio":
                        mensaje = "Tamagawa Daishi, ee trata de un templo budista que tiene un túnel de más de 100 metros que tienes que recorrer a oscuras llegando a ciertos puntos con luz donde podrás encontrar estatuas de Buda como si de una cripta recién descubierta de Indiana Jones se tratara.";
                        break;
                    case "secreto de london":
                        mensaje = "Cementerio de Highgate, este cementerio es uno de los lugares secretos de Londres que más te impresionarán. Al encontrarse al norte de la ciudad, en uno de sus puntos más altos, disfruta de unas vistas increíbles. Es enorme y en él podrás hallar las tumbas de figuras realmente reconocidas como el mismísimo Karl Marx.";
                        break;
                    case "secreto de londres":
                        mensaje = "Cementerio de Highgate, este cementerio es uno de los lugares secretos de Londres que más te impresionarán. Al encontrarse al norte de la ciudad, en uno de sus puntos más altos, disfruta de unas vistas increíbles. Es enorme y en él podrás hallar las tumbas de figuras realmente reconocidas como el mismísimo Karl Marx.";
                        break;
                    default:
                        mensaje = "No te puedo entender";
                        break;
                }

            }
            catch (Exception ex)
            {
                estado = 500;
                mensaje = ex.Message;
            }

            context.Response.ContentType = "text/plain";
            context.Response.Write(JsonConvert.SerializeObject(new { version = "1.0.0", estado, mensaje }));
        }

        public bool IsReusable
        {
            get
            {
                return false;
            }
        }
    }
}