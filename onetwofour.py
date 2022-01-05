
print(7%3)

def solution(n):
    answer = ''
    while n>0:
        n -= 1
        answer = '125'[n%3] + answer
        print(answer)
        n //= 3
        print(n)
    
    return answer

print('123'[1])
# solution(7)
    