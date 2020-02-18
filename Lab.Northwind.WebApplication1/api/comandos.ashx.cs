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


            context.Response.ContentType = "text/plain";
            context.Response.Write("Hola a todos");
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