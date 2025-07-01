
      /*
      class{
      method{
      str =" " + str;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch==' ') //not for 2 space
            {
              char ch1 = str.charAt(i+1);
                System.out.print(ch1);
            } 
        }
    }
    
   ---------- or----------
    while(sc.hasNext()); in input scanner class
*/
class UpperLowerCase {

public void display(String str) {
String[] words=str.trim().split("\\s+");//more than 2 space 
for(String v : words)
{
  System.out.print(v.charAt(0));
}
}
    
    public static void main(String[] args) {
      UpperLowerCase ob = new UpperLowerCase();

      ob.display("   vivek      govind desai");
    }
}
----------------last word print ---------
      class UpperLowerCase {

public void display(String str) {
String[] words=str.trim().split("\\s+");
for(String v : words)
{
  String lw=words[words.length-1];
if (v==lw)
 {
   System.out.print(" "+v);
  }
else
{
char k=v.charAt(0);
   System.out.print(Character.toUpperCase(k)+" ");
}

}
}
    
    public static void main(String[] args) {
      UpperLowerCase ob = new UpperLowerCase();

      ob.display("   vivek      Govind Desai");
    }
}

