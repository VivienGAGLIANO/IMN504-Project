# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 00:30:43 2022

@author: Lilian
"""
import matplotlib.pyplot as plt 
orbit1 = []
orbit2 = []
orbit3 = []
orbit4 = []

with open('C:/Users/Lilian/Documents/Projet GIT/IMN504-TP3 + projet/orbit1.txt') as f:
    for line in f:
        data = line.split("\n")
        orbit1.append(float(data[0]))

with open('C:/Users/Lilian/Documents/Projet GIT/IMN504-TP3 + projet/orbit2.txt') as f:
    for line in f:
        data = line.split("\n")
        orbit2.append(float(data[0]))
        
with open('C:/Users/Lilian/Documents/Projet GIT/IMN504-TP3 + projet/orbit3.txt') as f:
    for line in f:
        data = line.split("\n")
        orbit3.append(float(data[0])) 
        
with open('C:/Users/Lilian/Documents/Projet GIT/IMN504-TP3 + projet/orbit4.txt') as f:
    for line in f:
        data = line.split("\n")
        orbit4.append(float(data[0]))
        
figure, axis = plt.subplots(2, 2)
plt.figure(figsize=(20, 20))
axis[0, 0].plot(orbit1)
axis[0, 0].set_title("planet 1 : 71")
axis[0, 1].plot(orbit2)
axis[0, 1].set_title("planet 2 : -58")
axis[1, 0].plot(orbit3)
axis[1, 0].set_title("planet 3 : -44.8")
axis[1, 1].plot(orbit4)
axis[1, 1].set_title("planet 4: 28.85")
plt.show()