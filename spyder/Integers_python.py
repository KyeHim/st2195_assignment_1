# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:32:56 2022

@author: tanky
"""

# Print integers 1 to 10 without a loop

print(1,2,3,4,5,6,7,8,9,10)

# Print integers 1 to 10 using a loop

for i in range(1,11):
    print(i)
    
for i in range(1,11):
    print(i, end = " ")

j = 1
while(j <= 10):
    print(j)
    j = j + 1