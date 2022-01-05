
def solution(n):
    answer = ''
    while n>0:
        n -= 1
        answer = '125'[n%3] + answer
        n //= 3
    
    return answer

print(solution(7))    
    