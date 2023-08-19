using System;
namespace Productnum
{
    class Product {         
        public static void Main(string[] args)
        {
            	Console.WriteLine("Enter first value");
 		int userName = Convert.ToInt32(Console.ReadLine());
		Console.WriteLine("Enter second value");
      		int userName1 = Convert.ToInt32(Console.ReadLine());
		Console.WriteLine("Enter third value");
      		int userName2 = Convert.ToInt32(Console.ReadLine());
		Console.WriteLine("Enter fourth value");
      		int userName3 = Convert.ToInt32(Console.ReadLine());
		int pro = userName *userName1 *userName2 *userName3 ;
		System.Console.WriteLine("product is "+pro);

        }
    }
}