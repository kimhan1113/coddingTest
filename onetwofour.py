


def solution(n):
    answer = ''
    while n>0:
        n -= 1
        answer = '125'[n%3] + answer
        # print(answer)
        n //= 3
        # print(n)
    
    return answer


a = 1234

print(type(repr(a)))
# print('123'[1])
# solution(7)
    
    
    
    
def solution_(n):
    
    answer = ''
    
    while(n>0):
        n -=1
        answer = '124'[n%3] + answer
        n //= 3
        
    return answer


# print(solution_(4))
    
    
    
    
    
    
    
    
    