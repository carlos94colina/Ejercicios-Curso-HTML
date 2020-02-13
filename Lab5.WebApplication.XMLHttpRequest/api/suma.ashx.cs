using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Lab5.WebApplication.XMLHttpRequest.api
{
    /// <summary>
    /// Descripción breve de suma
    /// </summary>
    public class suma : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            decimal numero1 = Convert.ToDecimal(context.Request.Params["n1"]);
            decimal numero2 = Convert.ToDecimal(context.Request.Params["n2"]);

            context.Response.ContentType = "text/plain";
            context.Response.Write(numero1 + numero2);
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