using System;
namespace Fibo
{
    class Fibo {         
        public static void Main()
        {
          int x=0,y=1,z,i,num=23;    
             
         Console.Write(x+" "+y+" "); 
         for(i=2;i<num;++i)   
         {    
          z=x+y;    
          Console.Write(z+" ");    
          x=y;    
          y=z;    
         }    
      }  
   }  
        }
    