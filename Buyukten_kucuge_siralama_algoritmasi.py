arr = [1,5,7,2,6,9,2,6,2,10]

reversed_arr = []
unreversed_arr =  []

def main():
    for nexts in range(len(arr)):
        
        reversed_val = (arr[arr.index(sorted(arr,reverse=True)[nexts])])
        unreversed_val = (arr[arr.index(sorted(arr,reverse=False)[nexts])])

        
        reversed_arr.append(reversed_val)
        unreversed_arr.append(unreversed_val)

    print(f'Orjinal dizi: {arr}')
    print()
    print(f'Büyükten küçüğe sıralı dizi: {reversed_arr}')
    print()
    print(f'Küçükten küçüğe sıralı dizi: {unreversed_arr}')
    
main()
