public class Check {
  int a,b;
  public  Check(int i,int j)
  {
    a=i;
    b=j;
  }
public boolean cal(Check x){
  
    if(x.a ==a && x.b==b) return true;
    
    else return false;
}

  public static void main (String [] args)
  {
    
 Check ob1= new Check(10,20);
 Check ob2= new Check(-2,-6);
 Check ob3= new Check(10,20);
//Check ob3= new Check(ob1); also same but different memory 
 System.out.println("ob1==ob2 "+ob1.cal(ob2));
 System.out.println("ob1==ob3 "+ob1.cal(ob3));
 }
}
