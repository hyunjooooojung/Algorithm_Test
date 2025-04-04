class Solution {
    public int[] solution(String s) {
        int change = 0, zero = 0;
        
        while (!s.equals("1")) {
            change ++;
            
            // 0 제거
            int originalLength = s.length();
            s = s.replace("0", "");
            int ones = s.length();
            // 제거된 0의 개수
            zero += (originalLength - ones);
            
            s = Integer.toString(ones, 2);
        }
        int[] answer = new int[]{change, zero};
        return answer;
    }
}