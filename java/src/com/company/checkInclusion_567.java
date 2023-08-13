package com.company;

public class checkInclusion_567 {

    public static void main(String[] args) {
        checkInclusion_567 service = new checkInclusion_567();
        System.out.println(service.checkInclusion("dinitrophenylhydrazine","acetylphenylhydrazine"));
    }

    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()) return false;
        return  Permute(s1, s2,0,s1.length()-1);
    }


    public boolean  Permute(String s1,String s2, int pos , int len){
        if(pos >= len  ) {
            System.out.println(s1);
            if(s2.contains(s1)){
                return true;
            } else {
                return false;
            }
        } else{
            for (int i = pos; i <= len; i++) {
                s1 = swap(s1, pos, i);
                boolean result = Permute(s1, s2,pos +1,len);

                if(result == true) {
                    return result;
                }
                s1 = swap(s1 , pos, i);

            }
        }
        return false;
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
