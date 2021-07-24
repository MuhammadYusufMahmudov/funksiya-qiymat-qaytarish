# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 23:17:24 2021

@author: MuhammadYusuf Mahmudov 
theme:funksiya qiymatini qaytarish
"""


"""1-MISOL"""
# def toliq_ism_yasash(ism,familya):
#     """To'liq ism qaytaruvchi funfsiya"""
#     toliq_ism=f"{ism} {familya}"
#     return toliq_ism


# talaba1=toliq_ism_yasash('olim','hakimov')
# talaba2=toliq_ism_yasash('hakim','olimov')
# print(f"Darsga kelmagan talabalar:{talaba1.title()} va {talaba2.title()}")


"""2-MISOL"""

# def toliq_ism_yasash(ism,familya,otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism=f"{ism} {otasining_ismi} {familya}"
#     else:
#         toliq_ism=f"{ism} {familya}"
#     return toliq_ism.title()    
# talaba1=toliq_ism_yasash('hakim','olimov')
# talaba2=toliq_ism_yasash('olim','hakimov','abrorovich')

"""3-MISOL"""

# def avto_info(kompaniya,model,rangi,karobka,yili,narhi=None):
#     avto={'kompaniya':kompaniya,
#           'model':model,
#           'rang':rangi,
#           'karobka':karobka,
#           'yil':yili,
#           'narh':narhi}
#     return avto

# avto1=avto_info('GM','Malibu','Qora','avtomat','2019')
# avto2=avto_info('GM','Gentra','Oq','mexanika','2018',15000)

# avtolar=[avto1,avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto ['narh']:
#         narh=avto['narh']
#     else:
#         narh="Noma'lum"
#     print(f"{avto['rang']} {avto['model']}.Narhi:{narh}")


"""4-MISOL"""

# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))    
        
"""5-MISOL"""

def avto_info(kompaniya,model,rangi,karobka,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'karobka':karobka,
          'yil':yili,
          'narh':narhi}
    return avto

print("Saytimizdagi avtomoshinalarni shakllantiramiz")
avtolar=[]
while True:
    print("\n Quydagi ma;lumotlarni kiriting ",end='')
    kompaniya=input("Ishlab chiqaruvchi:")
    model=input("Modeli:")
    rangi=input("Rangi:")
    karobka=input("Karobka:")
    yili=input("Ishlab chiqarilgan yili:")
    narhi=input("Narhi:")
#Foydalanuvchi kiritgan ma'lumotdan avto_info yordamida Lug'atda shakllantirib
#har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya,model,rangi,karobka,yili,narhi))    
#Yana avtomashina qo'shish-qo'shmaslikni so'raymiz    

    javob=input("Yana avtomashina qo'shasizmi? (yes/no):")
    if javob =='no':
        break
print("\n Salondagi avtomashinalar:")
for avto in avtolar:
    if  avto['narh']:
        narh=avto['narh']
    else:
        narh="Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()},{karobka}.Narhi:{narh}")

    
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    