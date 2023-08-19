using System;
namespace sting
{
    class stnopr {         
        public static void Main()
        {
            	Console.WriteLine("Enter First name ");
		string fname = Console.ReadLine(); 
		Console.WriteLine("Enter Second name ");
		string sname = Console.ReadLine();
		Console.WriteLine("Enter Third name ");
		string lname = Console.ReadLine();
		string name = fname + sname +lname;
		System.Console.WriteLine("Full name is "+name);
		System.Console.WriteLine("Short name is "+" "+fname[0]+sname[0]+lname);
		Console.WriteLine("The length of the txt string is: " + name.Length);

        }
    }
}