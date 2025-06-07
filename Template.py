#https://www.lotobil.com/Sayisal-Loto-Butun-Sonuc-Listesi#

#/storage/emulated/0/Download/sayisalloto.csv

import colorama
import time as _t
from colorama import Back,Fore,Style
import numpy as np
import pandas as pd
import os as _o
import sys as _s

choose_data = []
year_arr = []
columns = ["tarih:","no:","S1","S2","S3","S4","S5","S6","  durum:"]

#b-g#

def quest_device():
    change_os = input('Cihazınızı seçin:\n\n0-Pc\n1-Mobil\n\n$> ')

    return change_os

device_info = quest_device()

if(device_info.isdigit()):

    if(int(device_info) == 0):

        _o.system('cls')

    elif(int(device_info) == 1):

        _o.system('clear')




data_frame = pd.read_csv(r"C:\Users\alper\Desktop\Top secret game\sayisalloto.csv")

class data_struct():
    def all_datas():
        
        year_arr.clear()

        print(Fore.LIGHTRED_EX,Style.BRIGHT)

        choose_option = input("\n\nHangi yilin verilerini istersiniz?\n\n>> ") 

        def recursive():
            if choose_option.startswith(' ') or choose_option == ' ' or choose_option == '':

                try:
                    if int(device_info) == 0:
                        print('BU ALAN BOŞ KALAMAZ')
                        _t.sleep(0.5)
                        _o.system('cls')
                        new_struct_win = data_struct.all_datas()

                        print(new_struct_win)
                
                except:
                    if int(device_info) == 1:
                        print('BU ALAN BOŞ KALAMAZ')
                        _t.sleep(0.5)
                        _o.system('cls')
                        new_struct_unix = data_struct.all_datas()

                        print(new_struct_unix)

                finally:

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

        if choose_option.startswith(' ') or choose_option == ' ' or choose_option == '':

            recursive()

            return 0

        for data_index in range(len(data_frame.values)):

            if str(data_frame.values[data_index][0]).startswith(choose_option):
                year_arr.append(data_frame.values[data_index])
                    
        try:		
            print(Fore.RESET,Style.RESET_ALL)

            return(pd.DataFrame(data=year_arr,columns=(columns[f] for f in range(len(data_frame.columns)))))
                    #nonerror hashhes#
        except Exception as maths_except:
            print(f"bir hata olustu\n\nHATA: {maths_except}")
            print(Fore.RESET,Style.RESET_ALL)
        try:
            if int(device_info) == 0:
                _o.system("clear")
                data_struct.all_datas()
                print(Fore.RESET,Style.RESET_ALL)

        except:
            if int(device_info) == 1:
                _o.system("cls")
                data_struct.all_datas()	
                print(Fore.RESET,Style.RESET_ALL)	

         
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
        #ALTTAKİ OROSPUNUN EVLADI VARYA O SONUNDA .pop OLAN CİBİLİYETİNE KAYDIĞIM HEH İŞTE ONU DÜZELTECEN PATLICAN KAFALI BİR KULLANICI ÇIKIP SİSTEM İNPUTUNU BOŞ VERİRSE KOD PATLIYOR AMK

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
                    if int(device_info) == 1:
                        _o.system('clear')

                if(action_choose_zero == 3):
                    try:
                        if int(device_info) == 0:
                            _o.system('cls')
                        if int(device_info) == 1:
                            _o.system('clear')

                    except:
                        pass ##empty##

                    finally:
                        Choose.choose_function()
        
        elif self.user_choose == 2:
            @staticmethod
            def quest_year():
                year_input = input('Hangi yıla ait sayı analizi istersiniz??\n\n>> ')

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
                        return True
                    
            print(quest_year())

                

        elif self.user_choose == 3:
            print('3')

        elif self.user_choose == 4:
            print('4')
        
        elif self.user_choose == 5:
            print('5')

        elif self.user_choose == 6:
            print('6')


Choose.choose_function()
        
    
    
