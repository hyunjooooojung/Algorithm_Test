import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] scores = new int[3]; // 각각의 점수 저장
        
        int[] number1 = {1, 2, 3, 4, 5};
        int[] number2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] number3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for (int i=0; i<answers.length; i++) {
            if (number1[i % number1.length] == answers[i]) scores[0]++;
            if (number2[i % number2.length] == answers[i]) scores[1]++;
            if (number3[i % number3.length] == answers[i]) scores[2]++;
        }
        System.out.println(Arrays.toString(scores));
        
        int maxScore = Arrays.stream(scores).max().getAsInt();
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i=0; i<scores.length; i++) {
            if (scores[i] == maxScore) {
                list.add(i+1);
            }
        }
        int[] result = new int[list.size()];
        for (int i=0; i<list.size(); i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}