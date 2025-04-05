import java.util.*;

class Solution {
    public int minuteToSecond(String s) { // 문자열->초
        String[] split_s = s.split(":");
        int mm = Integer.parseInt(split_s[0]);
        int ss = Integer.parseInt(split_s[1]);
        return mm * 60 + ss;
    }
    public String secondToMinute(int time) { // 초->문자열
        int mm = time / 60;
        int ss = time % 60;
        return String.format("%02d:%02d", mm, ss);
    }
    public int openingSkip(int op_start, int pos, int op_end) { // 오프닝 건너뛰기 확인
        if (op_start <= pos && pos <= op_end) {
            return op_end;
        }
        else {
            return pos;
        }
    }
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int videoLen = minuteToSecond(video_len);
        int position =  minuteToSecond(pos);
        int opStart = minuteToSecond(op_start);
        int opEnd = minuteToSecond(op_end);
        
        for (String command: commands) {
            position = openingSkip(opStart, position, opEnd);
            
            if (command.equals("prev")) {
                position = Math.max(0, position - 10);
            }
            else if (command.equals("next")) {
                position = Math.min(videoLen, position + 10);
            }
            position = openingSkip(opStart, position, opEnd);
        }
        return secondToMinute(position);
    }
}