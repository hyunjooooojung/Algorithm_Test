import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int total = brown + yellow; // 전체 카펫 넓이(=전체 격자 개수)
        
        for (int i=3; i<brown; i++) {
            if (total % i == 0) {
                int j = total / i;
                if ((i-2) * (j-2) == yellow) {
                    answer[0] = i;
                    answer[1] = j;
                }
            }
        }
        return answer;
    }
}