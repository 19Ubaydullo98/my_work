# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:22:07 2024

@author: Ubaydullo
"""

def juft(a):
    """berilgan ro'yhatning ichidan juft sonlarni topib beruvchi funksiya"""
    juft = []
    for i in a:
        if i%2==0 :
            juft.append(i)
    return juft
        
a = [45,48,49,51,46]