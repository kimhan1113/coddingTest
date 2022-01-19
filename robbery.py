def solution(money):
    
    table = [0 for _ in range(len(money))]
    
    table[0] = money[0]
    table[1] = money[0]
    
    for i in range(2, len(money)-1):
        table[i] = max(table[i-1], table[i-2] + money[i])
    
    value = max(table)
    
    table = [0 for _ in range(len(money))]
    
    table[1] = money[1]
    
    for i in range(2, len(money)):
        table[i] = max(table[i-1], table[i-2] + money[i])
    
    return max(value, max(table))