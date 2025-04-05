import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int a=0; a<commands.length; a++) {
            int i = commands[a][0], j = commands[a][1], k = commands[a][2];
            
            int[] cutArray = Arrays.copyOfRange(array, i-1, j); // 1번
            Arrays.sort(cutArray); // 2번
            answer[a] = cutArray[k-1];         
        }
        return answer;
    }
}