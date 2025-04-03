import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        List<Integer> result = new ArrayList<>();
        
        int prev = -1; // arr는 0~9만 포함하니까 -1로 초기화
        
        for (int a: arr) {
            if (a != prev) {
                result.add(a);
                prev = a;
            }
        }
        
        int[] answer = new int[result.size()];
        for (int i=0; i<result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}