import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s: scoville) {
            pq.add(s);
        }
        
        int min = pq.peek();
        while (min < K) {
            if (pq.size() >= 2) {
                int first = pq.poll();
                int second = pq.poll();
                int newScoville = first + second * 2;
                pq.add(newScoville);
                min = pq.peek();
                answer ++;
            }
            else return -1;
        }
        return answer;
    }
}