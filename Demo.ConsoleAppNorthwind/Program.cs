using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Demo.ConsoleAppNorthwind.Models;

namespace Demo.ConsoleAppNorthwind
{
    class Program
    {
        static void Main(string[] args)
        {
            var db = new ModelNorthwind();

            //SELECT * FROM dbo.Customers ORDER BY Country, City
            var clientes4 = db.Customers
                .OrderBy(r => r.Country)
                .ThenBy(r => r.City)
                .ToList();

            foreach (var item in clientes4)
            {
                Console.WriteLine("{0} - {1} - {2} ({3})",
                    item.CustomerID, item.CompanyName, item.City, item.Country);
            }

            Console.ReadKey();


            //SELECT CustomerID, CompanyName, City FROM dbo.Customers WHERE Country = 'USA'
            var clientes3 = db.Customers
                .Where(r => r.Country == "USA")
                .Select(r => new { r.CustomerID, r.CompanyName, r.City })
                .ToList();

            foreach (var item in clientes3)
            {
                Console.WriteLine("{0} - {1} - {2}",
                    item.CustomerID, item.CompanyName, item.City);
            }

            Console.ReadKey();

            //SELECT * FROM dbo.Customers WHERE CustomerID = 'ANATR'
            var cliente = db.Customers
                .Where(r => r.CustomerID == "ANATR")
                .FirstOrDefault();

            if (cliente == null) Console.WriteLine("Cliente no encontrado");
            else Console.WriteLine(cliente.CompanyName);

            Console.ReadKey();

            //SELECT * FROM dbo.Customers WHERE Country = 'Spain'
            var clientes2 = db.Customers
                .Where(r => r.Country == "Spain")
                .ToList();

            foreach (var item in clientes2)
            {
                Console.WriteLine("{0} - {1} - {2}",
                    item.CustomerID, item.CompanyName, item.Country);
            }

            Console.ReadKey();


            //SELECT * FROM dbo.Customers
            var clientes = db.Customers.ToList();

            foreach (var item in clientes)
            {
                Console.WriteLine("{0} - {1} - {2}",
                    item.CustomerID, item.CompanyName, item.Country);
            }

            Console.ReadKey();


        }
    }
}
