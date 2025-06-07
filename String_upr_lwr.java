class UpperLowerCase {

    public void display(String str, int p) {
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (p == 1 && Character.isUpperCase(ch)) {
                System.out.println(ch);
            } else if (p != 1 && Character.isLowerCase(ch)) {
                System.out.println(ch);
            }
        }
    }
    public void display(String str,char chr){
        for(int i=0;i<str.length();i++){
            char ch = str.charAt(i);
            if(chr=='v'){
                char ch1 = Character.toLowerCase(ch);
                if(ch1=='a' || ch1=='e' || ch1=='o' || ch1=='i' || ch1=='u'){
                    System.out.println(ch);
                }
            }
            else
            {
                System.out.println(ch);
            }
        }
    }

    public static void main(String[] args) {
      UpperLowerCase ob = new UpperLowerCase();
      //ob.display("COMPuteR", 8);
      ob.display("COMPUTER", 'v');
    }
}
