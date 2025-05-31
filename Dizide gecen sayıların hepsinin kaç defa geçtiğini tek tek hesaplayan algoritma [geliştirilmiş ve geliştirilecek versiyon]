#dizideki tum sayilarin kac kere gectigini hesaplayip yazan python algoritmasi#

import random
from time import sleep

x = [random.randint(0,100) for f in range(1500)]

frequency = {0}

f_arr = []
nums = []
num_counts = []
                                                         
for f in range(len(x)):                                                         
    f_arr.append(f"Sayı: {x[f]} Kaç kere geçti: {x.count(x[f])}")
    
    #print(f"Sayı: {x[f]} Kaç kere geçti: {x.count(x[f])}")

for g in range(len(f_arr)):
    nums.append(int(str(f_arr[g]).replace("Sayı: ", "  ").replace("Kaç kere geçti: ","  ").split(" ")[2]))
    num_counts.append(int(str(f_arr[g]).replace("Sayı: ", "  ").replace("Kaç kere geçti: ","  ").split(" ")[5]))

###sayıların yanına dizi içinde kaç defa geçtiğini yazan algoritma  {TAMAMLANACAK}###
x_max = max(num_counts) 

print(nums[num_counts.index(x_max)])

print(x_max)


#bu versiyon hem sayıların kaç defa geçtiğini hesaplayıp hemde hangi sayı oldugunun ayırt edebilen versiyonudr#
