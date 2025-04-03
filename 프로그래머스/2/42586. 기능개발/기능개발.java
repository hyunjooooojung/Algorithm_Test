import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answerList = new ArrayList<>();
        
        // 각 작업이 완료되기까지 걸리는 일수 계산
        int[] days = new int[progresses.length];
        for (int i = 0; i < progresses.length; i++) {
            days[i] = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
        }

        // 배포 단위 계산
        int count = 1;
        int current = days[0];
        
        for (int i=1; i<days.length; i++) {
            if (days[i] <= current) {
                count ++; 
            }
            else {
                answerList.add(count);
                current = days[i];
                count = 1;
            }
        }
        answerList.add(count);

        // List -> int[]
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}