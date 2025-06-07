arr = [i for i in range(11)]
copied_arr = arr.copy()
reversed_arr = []

for indexes in range(len(arr)):
    max_index = arr.index(max(arr))
    
    reversed_arr.append(max(arr))
    
    arr[max_index] = 0
    
print(arr)   
print(copied_arr) 
print(reversed_arr)    
