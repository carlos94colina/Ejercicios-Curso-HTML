using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Lab.Northwind.WebApplication1.api
{
    public class comandos : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            string texto = context.Request.Params["texto"];
            string comando = context.Request.Params["comando"];
            string resultado = "";

            switch (comando)
            {
                case "cuenta":
                    resultado = texto.Length.ToString();
                    break;
                case "fecha":
                    resultado = DateTime.Now.ToString();
                    break;
                case "vocales":
                    var array = texto.ToLower().ToArray<char>();

                    int contador = 0;

                    foreach (var letra in array)
                    {
                        if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u') contador++;
                    }

                    resultado = contador.ToString();

                    //////////////////////////////////////////////////////////////////////////////

                    char[] vocales = new char[] { 'a', 'e', 'i', 'o', 'u' };

                    int contador2 = 0;

                    foreach (var letra in array)
                    {
                        if (vocales.Contains(letra)) contador2++;
                    }

                    resultado = contador.ToString();

                    //////////////////////////////////////////////////////////////////////////////

                    char[] vocales2 = new char[] { 'a', 'e', 'i', 'o', 'u' };
                    resultado = array.Count(r => vocales2.Contains(r)).ToString();

                    break;
                default:
                    resultado = "Comando no valido";
                    break;
            }

            context.Response.ContentType = "text/plain";
            context.Response.Write(resultado);
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