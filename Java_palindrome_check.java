import java.util.*;
class Main {
    public static boolean palindrome(String s)
    {
        String rev=new StringBuilder(s). reverse().toString();
        return rev.equals(s);
    
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        System.out.println("value ");
        String st=sc.nextLine();
        if(palindrome(st))
        {
            System.out.println("palindrome");
        }
        else
        {
            System.out.println("not palindrome");
        }
        
    }
}
