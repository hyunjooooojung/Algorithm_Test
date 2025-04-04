import java.util.*;

class Solution {
    public int solution(int n) {
        String n_3 = Integer.toString(n, 3);
        String reverse = "";
        for (int i=n_3.length()-1; i>=0; i--) {
            reverse += n_3.charAt(i);
        }
        int answer = Integer.parseInt(reverse, 3);
        
        return answer;
    }
}