import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        
        int n = maps.length;
        int m = maps[0].length;
        
        int[][] visited = new int[n][m]; // 최단거리 저장하는 visited
        visited[0][0] = 1; // 시작 지점
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {0, 0});
        
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            
            for (int i=0; i<dx.length; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (0<=nx && nx<n && 0<=ny && ny<m && visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                    queue.offer(new int[]{nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        if (visited[n-1][m-1] == 0) {
            return -1;
        }
        else{
            return visited[n - 1][m - 1];
        }
    }
}