using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Lab.Northwind.WebApplication1.models;
using Newtonsoft.Json;

namespace Lab.Northwind.WebApplication1.api
{
    /// <summary>
    /// Descripción breve de productos
    /// </summary>
    public class productos : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            var db = new ModelNorthwind();
            db.Configuration.LazyLoadingEnabled = false;

            var desc = context.Request.Params["desc"];
            //if (desc == null) desc = "";

            var productos = db.Products
                .Where(r => r.ProductName.Contains(desc))
                .ToList();


            context.Response.ContentType = "text/plain";
            context.Response.Write(JsonConvert.SerializeObject(productos));
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