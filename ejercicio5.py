# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:21:42 2022

@author: rodri
"""

hola=0
Alumnosr=int(input("digite lña cantidad alumnos en la clase de redes: "))
Alumnosc=int(input("digite lña cantidad alumnos en la clase de contabilidad: "))
Alumnosd=int(input("digite lña cantidad alumnos en la clase de diseño: "))

totala=Alumnosr+Alumnosc+Alumnosd

porR=(Alumnosr/totala)*100
porC=(Alumnosc/totala)*100
porD=(Alumnosd/totala)*100

print(f"el porcentaje de los alumnos de redes es  : {porR}%")
print(f"el porcentaje de los alumnos de contabilidad es  : {porC}%")
print(f"el porcentaje de los alumnos de diseño es  : {porD}%")