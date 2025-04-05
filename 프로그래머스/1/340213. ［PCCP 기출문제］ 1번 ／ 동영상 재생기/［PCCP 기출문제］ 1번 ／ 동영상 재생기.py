def solution(video_len, pos, op_start, op_end, commands):
    def minute_to_second(string):
        mm, ss = map(int, string.split(":"))
        return mm * 60 + ss
    
    def second_to_minute(time):
        mm = str(time // 60).zfill(2)
        ss = str(time % 60).zfill(2)
        
        return f"{mm}:{ss}"
        
    pos = minute_to_second(pos)
        
    for command in commands:
        if minute_to_second(op_start) <= pos <= minute_to_second(op_end):
            pos = minute_to_second(op_end)
            
        if command == "prev":
            pos = max(0, pos-10)
        if command == "next":
            pos = min(minute_to_second(video_len), pos+10)
        
        if minute_to_second(op_start) <= pos <= minute_to_second(op_end):
            pos = minute_to_second(op_end)
    
    return second_to_minute(pos)