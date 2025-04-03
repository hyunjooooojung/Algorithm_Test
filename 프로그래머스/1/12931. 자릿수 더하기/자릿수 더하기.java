import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String num_string = Integer.toString(n);
        for (int i=0; i<num_string.length(); i++) {
            answer += Integer.parseInt(num_string.substring(i, i+1));
        }
        
        // while(n > 0){
        //     answer += n % 10;
        //     n /= 10;
        // }
        return answer;
    }
}