import java.util.*;
import java.lang.*;
class Pnumber{
    int a;
    public Pnumber(int c)
    {
        this.c=a;
    }
    public int cal()
    {
        int m=0;
        for (int i=1;i<=a/2;i++)
        {
            if(a%i == 0)
            {
                m=m+i;
            }
        }
        return m;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        System.out.println("enter number = ");
        int v=sc.nextInt();
        Pnumber od= new Pnumber(v);
        int r=od.cal();
        
        if(r==v)
        {
            System.out.println("Its a perfect number");
        }
        else
        {
            System.out.println("Given no is not perfect number");
        }
       
    }
}
