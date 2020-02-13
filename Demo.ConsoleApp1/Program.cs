using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Colegio;
using Universidad;
using Alumno = Universidad.Alumno;

namespace Demo.ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Alumno[] alumnos = new Alumno[5];

            alumnos[2] = new Alumno() { nombre = "Ana María", Apellido1 = "Sanz" };


            Console.ReadKey();

            ///////////////////////////////////////////////////////////7


            Alumno alumno = new Alumno();
            alumno.nombre = "Borja";
            alumno.Apellido1 = "Cabeza";

            Alumno alumno1 = new Alumno()
            {
                nombre = "Borja",
                Apellido1 = "Cabeza",
                Edad = 46
            };

            var alumno2 = new Alumno()
            {
                nombre = "Borja",
                Apellido1 = "Cabeza",
                Edad = 46
            };

            object alumno3 = new Alumno()
            {
                nombre = "Borja",
                Apellido1 = "Cabeza",
                Edad = 46
            };

            dynamic alumno4 = new Alumno()
            {
                nombre = "Borja",
                Apellido1 = "Cabeza",
                Edad = 46
            };

            Console.WriteLine("Nombre: {0}", alumno.nombre);
            Console.WriteLine("Nombre: {0}", alumno1.nombre);
            Console.WriteLine("Nombre: {0}", alumno2.nombre);
            //Console.WriteLine("Nombre: {0}", alumno3.nombre);
            Console.WriteLine("Nombre: {0}", ((Alumno)alumno3).nombre);
            Console.WriteLine("Tipo: {0}", alumno3.GetType().ToString());
            Console.WriteLine("Nombre: {0}", alumno4.nombre);

            Console.ReadKey();
        }
    }
}

namespace Colegio
{
    public class Alumno { }

}

namespace Universidad
{
    public class Alumno
    {
        public string nombre;
        public string Apellido1 { get; set; }
        public string Apellido2 { get; set; }
        public byte Edad { get; set; }
        public void Limpiar()
        { }
        public bool MayorDeEdad()
        {
            return true;
        }

        public Alumno()
        { }

        ~Alumno()
        { }

    }
}