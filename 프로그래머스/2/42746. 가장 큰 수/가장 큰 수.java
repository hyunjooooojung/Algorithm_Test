import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        List<String> stringNumbers = new ArrayList<>();
        // 숫자를 문자열로 변환
        for (int num: numbers) {
            stringNumbers.add(String.valueOf(num));
        }
        
        // 문자열 정렬
        stringNumbers.sort((a, b) -> (b + a).compareTo(a + b));
        
        // "0"이 맨 앞에 오면 전체 0
        if (stringNumbers.get(0).equals("0")) return "0";
        
        StringBuilder sb = new StringBuilder();
        for (String s: stringNumbers) {
            sb.append(s);
        }
        return sb.toString();
    }
}