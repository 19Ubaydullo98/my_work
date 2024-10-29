# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:04:40 2024

@author: Ubaydullo
"""

def tub(n):
    if n==2 or n == 3: return True
    if n%2 ==0 or n<2 : return False
    javob = []
    for i in range(3, n, 2):
        if n%i==0:
            javob.append(False)
        else:
            javob.append(True)
            
    if False in javob :
        return False
    else:
        return True
    
