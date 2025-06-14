import java.util.*;

class Vivek
{
    int a;
    public Vivek(int b)
    {
        a=b;
    }
    public boolean prime(int n)
    {
        for(int i=2; i<=n/2 ; i++)
        {
            if(n%i == 0)
            {
                return false;
            }
        }
          
        return true;  
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        System.out.println("Enter two no = ");
        int num=sc.nextInt();
        int num2=sc.nextInt();
        Vivek ob=new Vivek(num); 
        
      boolean r=ob.prime(num);
      boolean r2=ob.prime(num2);
        
        if(r&& r2 && Math.abs(num-num2)==4)
        //(num-num2==4 || num2-num ==-4))
        {
            System.out.println("Entered number is prime ");
        }
        else
        {
            System.out.println("Entered no is not prime ");
        }
        
    }
}
