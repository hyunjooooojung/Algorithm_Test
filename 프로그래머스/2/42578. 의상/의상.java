import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        
        Map<String, Integer> clothType = new HashMap<>();
        
        for (int i=0; i<clothes.length; i++) {
            clothType.put(clothes[i][1], clothType.getOrDefault(clothes[i][1], 0) + 1);
        }
        // for (String[] c: clothes) {
        //     String type = c[1];
        //     clothType.put(type, clothType.getOrDefault(type, 0) + 1);
        // }
        
        int answer = 1;
        // 각 종류마다 (입는 수 + 안 입는 수) = 개수 + 1
        for (int count: clothType.values()) {
            answer *= (count + 1);
        }
        // 아무것도 안 입는 경우 제외
        return answer-1;
    }
}