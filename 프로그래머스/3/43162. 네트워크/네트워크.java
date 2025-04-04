import java.util.*;

class Solution {
    public void dfs(int[][] computers, int[] visited, int v) {
        visited[v] = 1;
        
        for (int i=0; i<computers.length; i++) {
            if (visited[i] == 0 && computers[v][i] == 1) {
                dfs(computers, visited, i);
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n+1];
        // System.out.println(Arrays.toString(visited));
        
        for (int i=0; i<n; i++) {
            if (visited[i] == 0) {
                dfs(computers, visited, i);
                answer ++;
            }
        }
        return answer;
    }
}