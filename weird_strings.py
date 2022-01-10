

strings = "abc eFc"

answer = ""


string_list = strings.split(" ")

for j in range(len(string_list)):
    for i in range(len(string_list[j])):
        num = i+1
        if num % 2 == 1:
            convert_char = string_list[j][i].lower()
            answer += convert_char
        else:
            convert_char = string_list[j][i].upper()
            answer += convert_char
    answer += " "        
        
print(answer)        
        