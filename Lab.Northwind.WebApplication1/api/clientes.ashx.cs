using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Lab.Northwind.WebApplication1.models;
using Newtonsoft.Json;

namespace Lab.Northwind.WebApplication1.api
{
    public class clientes : IHttpHandler
    {
        public void ProcessRequest(HttpContext context)
        {
            //Params id - Identificador del cliente
            //            Si el identificador es igual ALL devolvemos todos loc clientes

            string id = context.Request.Params["id"];
            if (id != null) id = id.ToLower();

            var db = new ModelNorthwind();
            db.Configuration.LazyLoadingEnabled = false;    //Bloquea la carga de las propiedades virtuales

            if (id == "all")
            {
                List<Customers> clientes = db.Customers
                    .ToList();

                string clientesJSON = JsonConvert.SerializeObject(clientes);

                context.Response.ContentType = "text/plain";
                context.Response.Write(clientesJSON);
            }
            else
            {
                List<Customers> cliente = db.Customers
                    .Where(r => r.CustomerID == id)
                    .ToList();

                string clientesJSON = JsonConvert.SerializeObject(cliente);

                context.Response.ContentType = "text/plain";
                context.Response.Write(clientesJSON);
            }  
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