# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:17:14 2022

@author: rodri
"""

#Haga un programa en Python que permita ingresar el dinero invertido por
#tres personas para formar una empresa. Cada una de ellas invierte una
#cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
#al total de la inversión.

hugo=int(input("ingrese el monto invertido por Hugo:  "))
cris=int(input("ingrese el monto invertido por Cristian: "))
rodri=int(input("ingrese el monto invertido por Rodrigo:  "))

totalinv=hugo+cris+rodri
print(f"el valor total invertido por las tres peronas es igual a : ${totalinv:,}")
porh=(hugo/totalinv)*100
print(f"el porcentaje del valor  invertido por Hugo es igual a : {porh}%")
porc=(cris/totalinv)*100
print(f"el porcentaje del valor  invertido por Cristian es igual a  : {porc}%")
porR=(rodri/totalinv)*100
print(f"el porcentaje del valor  invertido por Rodrigo es igual a  : {porR}%")