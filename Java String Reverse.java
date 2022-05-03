import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String rs = "";
        int i = A.length() - 1 ;
        while (i>=0){
            rs = rs + A.charAt(i);
            i--;
            
        }
        if(rs.equals(A)){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        
        /* Enter your code here. Print output to STDOUT. */
        
    }
}



