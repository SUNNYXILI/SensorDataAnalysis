#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:01:31 2019

@author: lixi
"""


print("welcome to sensor data analyzer v1.5", " ")
filename="sensordata"
print(f"Enter the file to analyze: {filename}")


f=open("sensordata.txt")
lines=f.read().split("\n")


temps=[]
for line in lines:
    if float(line)>=200 or float(line)<=-200:
        print("Ignoring out of range temp: ", float(line))
    else:
        temps.append(float(line))

print("\n*****Feature #1******:")       
print("\nsearching for the spikes...")

for i in range(1,len(temps)-1):
    avg=(temps[i-1]+temps[i+1])/2
    if 1.5*avg <= temps[i]:
        print("Detected spike", temps[i-1],",",temps[i],"and",temps[i+1])
print("\n*****Feature #2******:")  
total=0
above=[]
below=[]
count=len(temps)
for temp in temps:
    total=total+temp
        
print("\ntotal:", total)
ave=total/count
print("average:", ave)

for each in temps:
    if each>ave:
        above.append(each)
    else:
        below.append(each)
        
countabove=len(above)
countbelow=len(below)
print(countabove, "entries are above the average." )
print(countbelow, "entries are below the average.")  

print("\n*****Feature #3******:")  
        
import matplotlib.pyplot as plt
plt.plot(temps)
plt.show()

print("\n*****Feature #4******:")  
max1=print("Max. Temp. (1):", max(temps))  
temps.remove(max(temps))
max2= print("Max. Temp. (2):", max(temps))   
min1=print("Min. Temp. (1):", min(temps))
temps.remove(min(temps)) 
min2=print("Min. Temp. (2):", min(temps))
  

print("Ave. Temp. ", ave)     

     
         
    
    
    