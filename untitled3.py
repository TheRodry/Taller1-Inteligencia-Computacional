# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:39:42 2022

@author: rodri
"""

vendedor=int(input("digite el valor del sueldo base: "))
totalv=int(input("digite el valor de las ventas totales: "))
comision=totalv*0.15
sueldot=vendedor+comision

print(f"el valor del sueldo base es : ${vendedor:,}") 
print(f"el valor de la comision es: ${comision:,}")
print(f"el valor total de pago es :${sueldot:,} ")

