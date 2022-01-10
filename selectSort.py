




arr = [1,5,3,10,7,2,5]

for i in range(len(arr)-1):
    min = i
    for j in range(i+1,len(arr)):
        if arr[min] > arr[j]:
            min = j
    
    arr[min], arr[i] = arr[i], arr[min]        
    

print(arr)    