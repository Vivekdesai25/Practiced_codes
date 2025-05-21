import java.util.*;

public class Main {
    public static void main(String[] args) {
      Scanner sc=new Scanner (System.in);
      System.out.println("Enter Any charector");
     char ch = sc.next().charAt(0);
     int ascii_value = (int)ch;
     System.out.println("ASCII value of given charector is  "+ascii_value);
     System.out.println("\n\n");
     System.out.println("Enter Any number from 0 to 127");
     int v=sc.nextInt();
     char ASCII_no = (char)v;
     System.out.println("ASCII charector of given number is "+ASCII_no);
  }
}

/* 
Above code in python
a=int(input("en no  "))
b=input("en char  ")
print ("ascii char",chr(a))
print("ascii no",ord(b))
*/
