import random

arr = [random.randint(0,100) for i in range(100)]
copied_arr = arr.copy()
reversed_arr = []

for indexes in range(len(arr)):
    max_index = arr.index(max(arr))
    
    reversed_arr.append(max(arr))
    
    arr[max_index] = 0

input("dizide işlem yapmak için [ENTER]")
input("-"*len("dizide işlem yapmak için [ENTER]")*2)
print(f"\nEşsiz sayilar\n\n{set(reversed_arr)}") #Eşsiz sayıları görmek için 
input()
print(f"Tum sayılar\n\n{reversed_arr}") #Tum sayıları görmek için 
input()
print(f"eski dizi\n\n{copied_arr}") #eski diziyi görmek için (orjinal)
input()
print(f"degistirilmis dizi\n\n{arr}") #degistirilmis diziyi görmek için 
input()
