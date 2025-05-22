def gcd(a,b):
  if(b==0):
    return a
  return gcd(b,a%b)
a=int(input ("en 1st no "))
b=int(input("en 2nd no "))
r=gcd(a,b)
print("GCD is ",r)

'''
import java.util.*;

public class Main {
  public static int gcd(int a,int b){
    if(b==0) return a;
    else return gcd(b,a%b);
  }
    public static void main(String[] args) {
      int r = gcd(10,15);
      System.out.println("gcd is "+ " "+r);
     
  }
}
'''
