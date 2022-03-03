# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:10:04 2022

@author: rodri
"""

taller1=float(input("digite la nota del taller 1: "))
taller2=float(input("digite la nota del taller 2: "))
taller3=float(input("digite la nota del taller 3: "))
notat=((taller1+taller2+taller3)/3)*0.5
examen=float(input("digite la nota del examen: "))
notae=examen*0.3
proyecto=float(input("digite la nota del proyecto: "))
notap=proyecto*0.2
notaf=(notat+notae+notap)


print(f"el 50% de los 3 talleres es igual  : {notat}")
print(f"el el 30% de lo examen es : {notae}")
print(f"el 20% del proyecto es igual : {notap}")
print(f"la nota final del curso es : {notaf}") 
   