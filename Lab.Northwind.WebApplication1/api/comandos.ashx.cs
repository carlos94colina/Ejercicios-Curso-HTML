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
                    var array = texto.ToArray<char>();

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