# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 18:44:49 2021

@author: MuhammadYusuf
theme:Funksiyaga ro'yxat uzatish
Eslatib o'taman ushbu kod ustozim AnvarNazrullaevdan olingan
"""
def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting:")
        baholar[ism]=baho
    return baholar


talabalar=['ali','vali','hasan','husan']
baholar=bahola(talabalar)
print(baholar)
