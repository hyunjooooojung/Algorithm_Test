import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Map<String, Boolean> map = new HashMap<>();
        for(String phone_number: phone_book) {
            map.put(phone_number, true);
        }
        
        for (String phone_number: phone_book) {
            for (int i=1; i<phone_number.length(); i++) {
                String prefix = phone_number.substring(0, i);
                if (map.containsKey(prefix)) {
                    return false;
                }
            }
            
        }
        return true;
    }
}