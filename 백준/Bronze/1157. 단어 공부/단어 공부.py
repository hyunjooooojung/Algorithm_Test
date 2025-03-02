string = input().lower()
set_string_list = list(set(string))

answer = [] 
for s in set_string_list:
    answer.append(string.count(s))

if answer.count(max(answer)) >= 2:
    print("?")
else:
    print(set_string_list[(answer.index(max(answer)))].upper())