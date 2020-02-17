using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo.ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numero = new List<int>();
            List<Persona> gente = new List<Persona>();

            Dictionary<string, string> dicc = new Dictionary<string, string>();

            dicc.Add("100", "Lunes");
            dicc.Add("200", "Martes");
            dicc.Add("AAA", "Miercoles");
            dicc.Add("ZAS", "Jueves");

            Console.WriteLine(dicc["100"]);
            dicc["AAA"] = "Viernes";

            foreach (var clave in dicc.Keys)
            {
                Console.WriteLine("Clave: {0} -  Valor: {1}", clave, dicc[clave]);
            }

            Console.ReadKey
                
                ();



            var p1 = new Persona() { Nombre = "Borja", Apellido1 = "Cabeza" };

            gente.Add(p1);
            gente.Add(new Persona() { Nombre = "Borja", Apellido1 = "Cabeza" });
            gente.Add(new Persona() { Nombre = "Borja", Apellido1 = "Cabeza" });
            gente.Add(new Persona() { Nombre = "Borja", Apellido1 = "Cabeza" });
            gente.Add(new Persona() { Nombre = "Borja", Apellido1 = "Cabeza" });
            gente.Add(new Persona() { Nombre = "Borja", Apellido1 = "Cabeza" });

            gente[1].Nombre = "Ana";

            Console.WriteLine(gente[0].Nombre);
            Console.WriteLine(gente[1].Nombre);

            Console.ReadKey();


            // Añadir Elementos a una Lista
            numero.Add(1000);
            numero.Add(10);
            numero.Add(56);
            numero.Add(23);
            numero.Add(12);

            var array = new int[] { 12, 45, 12, 3422, 0 };
            numero.AddRange(array);

            //Elimnar elemento de la lista
            numero.RemoveAt(3);

            //Recorremos la colección
            foreach (var valor in numero)
            {
                Console.WriteLine(valor);
            }

            Console.ReadKey();


            //////////////////////////////////////////

            Persona persona = new Persona() { Nombre = "Borja", Apellido1 = "Cabeza" };
            int numero1 = 10;

            Console.WriteLine("Nombre: " + persona.Nombre);
            Console.WriteLine("Valor:" + numero1.ToString());

            Prueba(persona, out numero1);

            Console.WriteLine("Nombre: " + persona.Nombre);
            Console.WriteLine("Valor:" + numero1.ToString());

            Console.ReadKey();
        }

        static void Prueba(Persona p, out int n)
        {
            p.Nombre = "Ana";
            
            n = 30;
        }
    }

    public class Persona
    {
        public string Nombre { get; set; }
        public string Apellido1 { get; set; }
    }
}
