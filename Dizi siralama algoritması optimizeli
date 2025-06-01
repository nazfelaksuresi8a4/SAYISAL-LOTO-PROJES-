import numpy as np
import random 
arr = [random.randint(0,100) for z in range(10)]

reversed_arr = []
unreversed_arr =  []

def main():
    for nexts in range(len(arr)):
        
        reversed_val = (arr[arr.index(sorted(arr,reverse=True)[nexts])])
        
        unreversed_val = (arr[arr.index(sorted(arr,reverse=False)[nexts])])

        
        reversed_arr.append(reversed_val)
        unreversed_arr.append(unreversed_val)

    print(f'Orjinal dizi: \n\n{np.reshape(arr,(len(arr)//2,2))}')
    print()
    print(f'Büyükten küçüğe sıralı dizi: \n\n{np.reshape(reversed_arr,(len(arr)//2,2))}')
    print()
    print(f'Küçükten küçüğe sıralı) dizi: \n\n{np.reshape(unreversed_arr,(len(arr)//2,2))}')
    
main()
