import java.util.*;
public class Long {
    public static String Long(String str[])
    {
        for(boolean s:str)//for empty string 
            {
                if(str.length==a[0]) return "";
            }
                
        Arrays.sort(str);
        String fs=str[0];
        String ss=str[str.length-1];
        int i=0;
        while (i<str.length)
        {
            if(fs.charAt(i)==ss.charAt(i))
            {
                i++;
            }
            else
            {
                break;
            }
        }
        return i==0 ?" \"\" " : ss.substring(0,i);
    }
    public static void main(String[] args) {
        String str[]={"oiar","pcarb","ctarot"};
        System.out.println(Long(str));
    }
} 
