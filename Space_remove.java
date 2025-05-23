class UpperLowerCase {

    public void display(String str) {
      /*
      
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
*/
String[] words=str.trim().split("\\s+");
for(String v : words)
{
  System.out.print(v.charAt(0));
}
}
    
    public static void main(String[] args) {
      UpperLowerCase ob = new UpperLowerCase();
      //ob.display("COMPuteR", 8);
      ob.display("   vivek      govind desai");
    }
}
