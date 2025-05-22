def gcd(a,b):
  if(b==0):
    return a
  return gcd(b,a%b)
a=int(input ("en 1st no "))
b=int(input("en 2nd no "))
r=gcd(a,b)
print("GCD is ",r)

'''
*******************************************
import java.util.*;

public class Main {
  public static int gcd(int a,int b){
    if(a==0) return b;
    if(b==0) return a;
    while(b!=a)
    {
      if(a>b) return a=a-b;
      else return b=b-a;
    }
    return a;
  }
    public static void main(String[] args) {
      int r = gcd(10,15);
      System.out.println("gcd is "+ " "+r);
     
  }
}
***********************************************
------------------or --------------------------
while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
-----------------------------------------------------
'''
