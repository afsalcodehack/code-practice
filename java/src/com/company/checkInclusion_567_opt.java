package com.company;

import java.util.HashMap;

public class checkInclusion_567_opt {

    public static void main(String[] args) {
        checkInclusion_567_opt service = new checkInclusion_567_opt();
        //System.out.println(service.checkInclusion("dinitrophenylhydrazine","acetylphenylhydrazine"));
        System.out.println(service.checkInclusion("ab","eidbaooo"));
        System.out.println(service.checkInclusion("ab","eidboaoo"));
    }


    public boolean checkInclusion(String s2, String s1) {
        HashMap<Character , Integer> s1_map = new HashMap<Character, Integer>();
        HashMap<Character , Integer> s2_map = new HashMap<Character, Integer>();
        for (int i = 0; i < s2.length(); i++) {
            if(s2_map.containsKey(s2.charAt(i))){
                int currentValue = s2_map.get(s2.charAt(i));
                s2_map.put(s2.charAt(i) , currentValue + 1);

            }else{
                s2_map.put(s2.charAt(i) , 1);
            }

        }

        for (int i = 0; i < s1.length(); i++) {

            if(!s2_map.containsKey(s1.charAt(i)))
                return false;

            if(s1_map.containsKey(s1.charAt(i))){
                int currentValue = s1_map.get(s1.charAt(i));
                s1_map.put(s1.charAt(i) , currentValue + 1);

                if(s2_map.get(s2.charAt(i)) < s1_map.get(s2.charAt(i)))
                    return false;


            }else{
                s2_map.put(s1.charAt(i) , 1);
            }
        }

        return true;
    }
}
