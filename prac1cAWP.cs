using System;
namespace Student
{
    class Student {         
        public static void Main()
        {
            Console.WriteLine("Enter no of students ");
		int nostu = Convert.ToInt32(Console.ReadLine());
		for (int i = 0; i < nostu; i++){

  		Console.WriteLine("Enter Student_id value");
 		int stid = Convert.ToInt32(Console.ReadLine());

  		Console.WriteLine("Enter Student name ");
 		string Name = Console.ReadLine();

  		Console.WriteLine("Enter course name value");
 		string c_Name = Console.ReadLine();

  		Console.WriteLine("Enter Date od birth-");
 		string dateb = Console.ReadLine();
		
		System.Console.WriteLine("this is-"+Name+"'s data "+" his/her student id is-"+stid+". In course-"+c_Name+" Dob is-"+dateb);
		
		}
		
        }
    }
}