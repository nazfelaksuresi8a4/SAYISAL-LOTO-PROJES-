import numpy as np

arr = [1,5,7,2,6,9,2,6,2,10]

reversed_arr = []
unreversed_arr =  []

def main():
    for nexts in range(len(arr)):
        
        reversed_val = (arr[arr.index(sorted(arr,reverse=True)[nexts])])
        
        unreversed_val = (arr[arr.index(sorted(arr,reverse=False)[nexts])])

        
        reversed_arr.append(reversed_val)
        unreversed_arr.append(unreversed_val)

    print(f'Orjinal dizi: \n{np.reshape(arr,(5,2))}')
    print()
    print(f'Büyükten küçüğe sıralı dizi: \n{np.reshape(reversed_arr,(5,2))}')
    print()
    print(f'Küçükten küçüğe sıralı dizi: \n{np.reshape(unreversed_arr,(5,2))}')
    
main()


#reshape kullanımı np.reshape(array,(5,2)) 5 = Satir 2 = Sütun yan yana row
