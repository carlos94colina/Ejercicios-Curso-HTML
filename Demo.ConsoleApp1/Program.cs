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
            Alumno alumnoDemo = new Alumno()
            {
                nombre = "Borja",
                Apellido1 = "Cabeza",
                Edad = 19
            };

            float[] notas = new float[] { 5.98F, 6.74F, 10F, 5.09F, 8.99F, 7.0F };

            Console.WriteLine("Mayor de Edad: " + alumnoDemo.MayorDeEdad(21));
            Console.WriteLine("Media: " + alumnoDemo.CalcularMedia(notas));

            Console.ReadKey();

            ////////////////////////////////////////////////////////////////

            Alumno[] alumnos = new Alumno[5];
            alumnos[2] = new Alumno() { nombre = "Ana María", Apellido1 = "Sanz" };

            var alumnos2 = new Alumno[] {
                new Alumno() { nombre = "Ana María", Apellido1 = "Sanz" },
                new Alumno() { nombre = "María", Apellido1 = "Ruiz" },
                new Alumno() { nombre = "Carlos", Apellido1 = "Sánchez" },
                new Alumno() { nombre = "Julian", Apellido1 = "García" }
            };

            for (var c = 0; c < alumnos2.Length; c++)
            {
                Console.WriteLine("Posición: {0} - Valor: {1}", 
                    
                    
                    c, alumnos2[c].nombre + " " + alumnos2[c].Apellido1);
            }

            foreach (var item in alumnos2)
            {
                Console.WriteLine("Valor: {0}", item.nombre + " " + item.Apellido1);
            }




            var dias = new string[] {
                "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"
            };

            for (var c = 0; c < dias.Length; c++)
            {
                Console.WriteLine("Posición: {0} - Valor: {1}", c, dias[c]);
            }

            foreach(var dia in dias)
            {
                Console.WriteLine("Valor: {0}", dia);
            }




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
        { 
        
        }
        public bool MayorDeEdad(int limite)
        {
            if (Edad >= limite) return true;
            else return false;
        }

        public float CalcularMedia(float[] notas)
        { 
            float media = 0;

            foreach (var n in notas)
            {
                media += n;
                //media = media + n;
            }

            media = media / notas.Length;

            return media;
        }

        public Alumno()
        { }

        ~Alumno()
        { }

    }
}