import java.util.*;
// 풍선 번호가 담긴 배열 a에서 풍선 i가 최후까지 남을 수 있으려면:

// 왼쪽에 있는 풍선들 중 a[i]보다 작은 값이 없어야 하고
// 오른쪽에 있는 풍선들 중 a[i]보다 작은 값이 없어야 함.

// 즉, a[i]보다 작은 풍선이 양쪽 모두에 있으면 살아남을 수 없음
// 맨 앞의 풍선과 맨 뒤의 풍선은 좌측과 우측 값이 각각 없기 때문에, 무조건 남을 수 밖에 없다.

class Solution {
    public int solution(int[] a) {
        int n = a.length;
        int[] leftMin = new int[n];
        int[] rightMin = new int[n];
        
        // 왼쪽 최소값 배열
        int min = Integer.MAX_VALUE;
        for (int i=0; i<n; i++) {
            min = Math.min(min, a[i]);
            leftMin[i] = min;
        }
        
        // 오른쪽 최소값 배열
        min = Integer.MAX_VALUE;
        for (int i=n-1; i>=0; i--) {
            min = Math.min(min, a[i]);
            rightMin[i] = min;
        }
        
        int answer = 0;
        for (int i=0; i<n; i++) {
            // 양쪽 모두 a[i]보다 작은 풍선이 없을 경우만 생존 가능
            if (a[i] <= leftMin[i] || a[i] <= rightMin[i]) {
                answer++;
            }
        }
        return answer;
    }
}