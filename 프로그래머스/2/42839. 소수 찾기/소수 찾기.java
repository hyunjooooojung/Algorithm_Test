import java.util.*;

class Solution {
    static Set<Integer> set;
    static int[] visited = new int[7];
    
    public int solution(String numbers) {
        int answer = 0;
        
        set = new HashSet<>();
        dfs(numbers, "", 0);
        for (int s: set) {
            if (isPrime(s)) answer++;
        }
        return answer;
    }
    
    public void dfs(String numbers, String s, int depth) {
        if (depth > numbers.length()) return;
        
        for (int i=0; i<numbers.length(); i++) {
            if (visited[i] == 0) {
                visited[i] = 1; // 방문처리
                set.add(Integer.parseInt(s + numbers.charAt(i)));
                dfs(numbers, s + numbers.charAt(i), depth+1);
                visited[i] = 0;
            }            
        }
    }
    public boolean isPrime(int n) {
        // 소수 판별 
        if (n < 2) {
            return false;
        }
        
        for (int i=2; i<(int) Math.sqrt(n) + 1; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}