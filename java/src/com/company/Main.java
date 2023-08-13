package com.company;

public class Main {

    public static void main(String[] args) {
        Main service = new Main();
        String str=  "eidboaoo";
        service.Permute(str, 0,str.length()-1 );
    }
     

    public void  Permute(String str, int pos , int len){
        if(pos >= len) {
            System.out.println(str);
            return;
        }

        for (int i = pos; i <= len; i++) {
            str = swap(str, pos, i);
            Permute(str, pos +1,len);
            str = swap(str , pos, i);
        }


    }



    private String swap(String str ,int i ,int j){
        char temp;
        char[] charArray = str.toCharArray();
        temp = charArray[i] ;
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }
}
