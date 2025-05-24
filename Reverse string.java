import java.util.*;

public class Main {
  void rev(String a)
  {
    String r="";
    for(int i=a.length()-1;i>=0;i--)
    {
      r=r+a.charAt(i);
    }
      System.out.print(r);
    
  }
  
    public static void main(String[] args) {
      //System.out.println("Hello, World!");
      Scanner m = new Scanner(System.in);
      System.out.println("en ");
      String r=m.nextLine();
      Main ob = new Main();
      
//String ob = new StringBuilder(r).reverse().toString();
//System.out.print(ob);
      ob.rev(r);
  }
}
