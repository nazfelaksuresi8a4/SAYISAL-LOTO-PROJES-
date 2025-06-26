#https://www.lotobil.com/Sayisal-Loto-Butun-Sonuc-Listesi#

#/storage/emulated/0/Download/sayisalloto.csv

import colorama
import time as _t
from colorama import Back,Fore,Style
import numpy as np
import pandas as pd
import os as _o
import sys as _s

return_index = 0
choose_data = []
year_arr = []
columns = ["tarih:","no:","S1","S2","S3","S4","S5","S6","  durum:"]

#b-g#

def select_option():
    action_choose = int(input('\n\n1-ÇIK\n2-TEKRAR BAŞLAT\n\n$>> '))

    if(action_choose == 1):
        try:
            if int(device_info) == 0:
                _o.system('cls')
        except:
            if int(device_info) == 1:
                _o.system('clear')
        finally:
                _s.exit()

    if(action_choose == 2):
        try:
            if int(device_info) == 0:
                _o.system('cls')
        except:
                if int(device_info) == 1:
                    _o.system('clear')
        finally:
                Choose.choose_function()

def quest_device():
    change_os = input('Cihazınızı seçin:\n\n0-Pc\n1-Mobil\n\n$> ')

    if(change_os.isdigit()):

        if(int(change_os) == 0):

            _o.system('cls')
            return change_os

        elif(int(change_os) == 1):

            _o.system('clear')
            return change_os

    elif change_os == '' or device_info == ' ':
        quest_device()

    else:
        quest_device()



device_info = quest_device()


data_frame = pd.read_csv(r"C:\Users\alper\Desktop\Top secret game\sayisalloto.csv")

class all_year_datas:
    def all_year_data():
        for vals in data_frame.values:
            print(vals) 
        print(Fore.RESET)

        #data_struct.all_datas()

class data_struct:
    def all_datas():
        
        year_arr.clear()

        print(Fore.LIGHTRED_EX,Style.BRIGHT)

        choose_option = input("\n\nHangi yilin verilerini istersiniz?\n\n>> ") 

        if int(choose_option) == 101:
            all_year_datas.all_year_data()
            
            input('Devam etmek için [ENTER]')
            

        else:
            print('pass')

        def recursive_stat():
                        action_choose = int(input('\n\n1-ÇIK\n2-BAŞA DÖN\n3-TEKRAR BAŞLAT\n\n$>> '))

                        if(action_choose == 1):
                            try:
                                if int(device_info) == 0:
                                    _o.system('cls')
                            except:
                                if int(device_info) == 1:
                                    _o.system('clear')
                            finally:
                                _s.exit()

                        elif(action_choose == 2):
                            try:
                                if int(device_info) == 0:
                                    _o.system('cls')
                            except:
                                if int(device_info) == 1:
                                    _o.system('clear')
                            finally:
                                data_struct.all_datas()

                        elif(action_choose == 3):
                            try:
                                if int(device_info) == 0:
                                    _o.system('cls')
                            except:
                                if int(device_info) == 1:
                                    _o.system('clear')
                            finally:
                                Choose.choose_function()

        def recursive():
            if int(choose_option) == 101:
                recursive_stat()

            if choose_option.startswith(' ') or choose_option == ' ' or choose_option == '':

                try:
                    if int(device_info) == 0:
                        print('BU ALAN BOŞ KALAMAZ')
                        _t.sleep(0.5)
                        _o.system('cls')
                        new_struct_win = data_struct.all_datas()

                        #print(new_struct_win)
                
                except:
                    if int(device_info) == 1:
                        print('BU ALAN BOŞ KALAMAZ')
                        _t.sleep(0.5)
                        _o.system('cls')
                        new_struct_unix = data_struct.all_datas()

                        print(new_struct_unix)

        def main_algorithm_object():

            for data_index in range(len(data_frame.values)):

                if str(data_frame.values[data_index][0]).startswith(str(choose_option)):
                    year_arr.append(data_frame.values[data_index])
                        
            try:		
                print(Fore.RESET,Style.RESET_ALL)

                print(pd.DataFrame(data=year_arr,columns=(columns[f] for f in range(len(data_frame.columns)))))
                        #nonerror hashhes#
                input('Devam etmek için [ENTER]')

            except Exception as maths_except:
                print(f"bir hata olustu\n\nHATA: {maths_except}")
                print(Fore.RESET,Style.RESET_ALL)
            try:
                if int(device_info) == 0:
                    _o.system("clear")
                    recursive_stat()
                    print(Fore.RESET,Style.RESET_ALL)

            except:
                if int(device_info) == 1:
                    _o.system("cls")
                    recursive_stat()	
                    print(Fore.RESET,Style.RESET_ALL)	


        main_algorithm_object()

class Choose():
    def choose_function():
        colorama.init() 

        print(Fore.GREEN,Style.BRIGHT)

        choose_input = input(f'1-Bütün çekiliş listesi(ARŞİV)\n2-En çok çıkan sayılar\n3-Tahmin al\n4-Tek-çift oranı\n5-Tek-çift dağılımı\n6-Asal sayılar çok çıkanlar\n{len('Asal sayılar en çok çıkanlar')*'-'}\n$>> ')
        
        print(Fore.RESET,Style.RESET_ALL)

        try:
            choose_data.append(int(choose_input))

            print(choose_data)
        except:
            _o.system("clear")
            Choose.choose_function()
        	
        Cli_side()
        try:
            return int(choose_input)   
            
        except:
            _o.system('cls')
            Choose.choose_function()
            

class Cli_side():
    def __init__(self):

        self.user_choose = choose_data.pop()

        print("Eger tum verileri gormek isterseniz 101 sayisini tuslayin...")

        if self.user_choose == 1:
            try:
                print(data_struct.all_datas())	
            except: 
                pass

            finally:
                action_choose_zero = int(input('\n\n1-ÇIK\n2-BAŞA DÖN\n3-TEKRAR BAŞLAT\n\n$>> '))

                if(action_choose_zero == 1):
                    if int(device_info) == 0:
                        _o.system('cls')
                    if int(device_info) == 1:   
                        _o.system('clear') 

                if(action_choose_zero == 2):
                    if int(device_info) == 0:
                        _o.system('cls')
                        data_struct.all_datas()
                    if int(device_info) == 1:
                        _o.system('clear')
                        data_struct.all_datas()

                if(action_choose_zero == 3):
                    try:
                        if int(device_info) == 0:
                            _o.system('cls')
                        if int(device_info) == 1:
                            _o.system('clear')

                    except:
                        pass ##empty##

                    finally:
                        print('MERHABAAA')
        
        elif self.user_choose == 2:
            class quest_class:
                def quest_year():
                    year_input = input('Hangi yıla ait sayı analizi istersiniz??\n\n>> ')

                    return_index = 0

                    if year_input == '' or  year_input == ' ':
                        if int(device_info) == 0:
                            _o.system('cls')
                            return year_input
                        
                        elif int(device_info) == 1:
                            _o.system('clear')
                            return year_input
                    
                        else:
                            return_index = 0

                    try:
                        f = float(year_input)

                        if f.is_integer():
                            return_index = 1

                        else:
                            pass

                    except:
                        return False
                    
                    finally:
                        if return_index == 0:
                            return False
                        
                        elif return_index == 1:
                            return int(year_input)

            def quest_all():
                year = quest_class.quest_year()
                
                
                real_count_data = []
                value_data = []

                value_count_data = []
                val_dat = []

                third_value_count_data_arr = []
                third_value_data_arr = []

                if year == False:

                    if int(device_info) == 0:
                        _o.system('cls')
                        quest_class.quest_year()
                    
                    elif int(device_info) == 1:
                        _o.system('clear')
                        quest_class.quest_year()

                
                elif year == 101:
                    for data_indexes in range(len(data_frame.values)):
                        value_data.append(data_frame.values[data_indexes][2:7])                    

                    for matris_length in range(len(value_data)):
                        for vals in range(len(value_data[matris_length])):       
                            value_count_data.append(value_data[matris_length])
                        

                    for x in range(len(value_count_data)):
                        for meta_value in range(len(value_count_data[x])):
                            real_count_data.append(value_count_data[x][meta_value])
                    
                    for valcoin in range(len(value_data)):
                        for valco in range(len(value_data[valcoin])):
                            val_dat.append(value_data[valcoin][valco])
                    try:
                        maximum_input = input(f'kaçıncı kolona kadar en fazla çıkan sayıları bulmak istersiniz??\n\n0 ile {len(data_frame.values)} arasında\n\n$>> ')

                        for count_data in range(len(val_dat)):
                            print(f'Sayı:{val_dat[count_data]}  Kaç defa geçti: {val_dat.count(val_dat[count_data])}')

                        val_dat_copy = val_dat.copy()
                        print('\n\nEn Fazla çıkan sayılar kısmı\n\n')

                        for lens in range(int(maximum_input)):    
                            third_value_data_arr.append(val_dat_copy[lens])
                            third_value_count_data_arr.append(val_dat_copy.count((val_dat_copy[lens])))

                        for main_count_vals in zip(third_value_data_arr,third_value_count_data_arr):
                            print(f'sayı & kaç kere geçti: {main_count_vals}')


                    except:
                        print(Fore.LIGHTBLACK_EX,'\nSayım Türü: HEPSİNİ SAY\nSayım sonucu: BASARİSİZ\n\nSayım tamamlanırken bir hata oluştu...')                

                    finally:
                        quest_action_second_input_3 = input('\n\n1-PROGRAMI KAPAT\n2-İŞLEMİN BAŞINA DÖN\n3-PROGRAMIN BAŞINA DÖN\n\n>>> ')

                        if str(quest_action_second_input_3).isdigit():
                                if int(quest_action_second_input_3) == 1:
                                    try:
                                        if int(device_info) == 0:
                                            _s.exit()
                                            _o.system('cls')
                                        
                                        elif int(device_info) == 1:
                                            _s.exit()
                                            _o.system('clear')          

                                    except:
                                        x1 = 0

                                if int(quest_action_second_input_3) == 2:
                                    try:
                                        if int(device_info) == 0:     
                                            _o.system('cls')
                                            quest_all()

                                        elif int(device_info) == 1:               
                                            _o.system('clear')
                                            quest_all()
                                    except:
                                        x2 = 1

                                if int(quest_action_second_input_3) == 3:
                                    try:
                                        if int(device_info) == 0:     
                                            _o.system('cls')
                                            Choose.choose_function()

                                        elif int(device_info) == 1:
                                            _o.system('clear')
                                            Choose.choose_function()
                                    except:
                                        x2 = 2                  

                else:
                    third_value_data_arr_2 = []
                    third_value_count_data_arr_2 = []

                    for data_indexes in range(len(data_frame.values)):
                        if str(data_frame.values[data_indexes][0]).startswith(str(year)):
                            value_data.append(data_frame.values[data_indexes][2:7])
                    
                    for matris_length in range(len(value_data)):
                        for vals in range(len(value_data[matris_length])):       
                            value_count_data.append(value_data[matris_length])
                        

                    for x in range(len(value_count_data)):
                        for meta_value in range(len(value_count_data[x])):
                            real_count_data.append(value_count_data[x][meta_value])
                    
                    for valcoin in range(len(value_data)):
                        for valco in range(len(value_data[valcoin])):
                            val_dat.append(value_data[valcoin][valco])

                    maximum_input_2 = input(f'kaçıncı kolona kadar en fazla çıkan sayıları bulmak istersiniz??\n\n0 ile {len(data_frame.values)} arasında\n\n$>> ')
                            
                    try:
                        for count_data in range(len(val_dat)):
                            print(f'Sayı:{val_dat[count_data]}  Kaç defa geçti: {val_dat.count(val_dat[count_data])}')

                        val_dat_copy_2 = val_dat.copy()
                        print('\n\nEn Fazla çıkan sayılar kısmı\n\n')

                        for lens_2 in range(int(maximum_input_2)):    
                            third_value_data_arr_2.append(val_dat_copy_2[lens_2])
                            third_value_count_data_arr_2.append(val_dat_copy_2.count((val_dat_copy_2[lens_2])))

                        for main_count_vals_2 in zip(third_value_data_arr_2,third_value_count_data_arr_2):
                            print(f'sayı & kaç kere geçti: {main_count_vals_2}')

                    except:
                        print(Fore.LIGHTBLACK_EX,'\nSayım Türü: BELİRLİ YILIN SAYILARINI SAY\nSayım sonucu: BASARİLİ\n\nSayım tamamlandı sonuçları inceleyebilirsiniz..') 

                    finally:
                        third_value_data_arr_2.clear()
                        third_value_count_data_arr_2.clear()
                        
                        quest_action_second_input_4 = input('\n\n1-PROGRAMI KAPAT\n2-İŞLEMİN BAŞINA DÖN\n3-PROGRAMIN BAŞINA DÖN\n\n>>> ')

                        if int(device_info) == 0:
                            _o.system('cls')

                        if str(quest_action_second_input_4).isdigit():
                                if int(quest_action_second_input_4) == 1:
                                    try:
                                        if int(device_info) == 0:     

                                            _o.system('cls')
                                            _s.exit()

                                        elif int(device_info) == 1:
                
                                            _o.system('clear')
                                            _s.exit()
                                            
                                    except:
                                        pass

                                if int(quest_action_second_input_4) == 2:
                                    try:
                                        if int(device_info) == 0:     

                                            _o.system('cls')
                                            quest_all()

                                        elif int(device_info) == 1:
                    
                                            _o.system('clear')
                                            quest_all()
                                    except:
                                        pass

                                if int(quest_action_second_input_4) == 3:
                                    try:
                                        if int(device_info) == 0:     

                                            _o.system('cls')
                                            Choose.choose_function()

                                        elif int(device_info) == 1:
                    
                                            _o.system('clear')
                                            Choose.choose_function()
                                    except:
                                        pass
                
        elif self.user_choose == 3:
            meta_data_array = []

            for metadata_vals in data_frame.values:
                vals = metadata_vals[2:7]
                for val in vals:
                    meta_data_array.append(val) 

            def merge_sort(metadata_arr):
                if len(metadata_arr) <= 1:
                    return metadata_arr
            
                middle = len(metadata_arr) // 2

                left = merge_sort(metadata_arr[:middle])
                right = merge_sort(metadata_arr[middle:])

                return merge_function(left, right)
            
            def merge_function(*args):
                metadata_results = []
                i = j = 0

                while i < len(args[0]) and j < len(args[1]):
                    if args[0][i] < args[1][j]:
                        metadata_results.append(args[0][i])
                        i += 1
                    
                    else:
                        metadata_results.append(args[1][j])
                        j += 1
                    
                metadata_results.extend(args[0][i:])
                metadata_results.extend(args[1][j:])

                return metadata_results
            try:
            
                h = []
                f = []

                merge_sort_results = merge_sort(meta_data_array)

                x = input('Kaç tane tahmin istersiniz?\n\n>> ')

                if x.isdigit():
                    str_to_int_x = int(x)
                
                else:
                    print('Yanlis bir girdi verdiniz lütfen tekrar başlayın.....')
                    _t.sleep(4)
                    select_option()
                    

                for y in range(x):  
                    h.append(list(set(merge_sort_results))[y])
                    f.append(meta_data_array.count(list(set(merge_sort_results))[y]))

                for x,y in zip(h,f):
                    print(f'|| Sayı: {h} || Kaç defa gecti: {f}')
                
                print('\n\nAlabileceğiniz en iyi tahminler yukarıda verilmiştir....')

            
            except Exception as kernel:
                print(kernel)

            finally:
                select_option()
            
        elif self.user_choose == 4:
            print('4')
            
        elif self.user_choose == 5:
            print('5')

        elif self.user_choose == 6:
            print('6')

        try:
            quest_all()

        except:
            pass
Choose.choose_function()
