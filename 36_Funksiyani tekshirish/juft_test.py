# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:25:41 2024

@author: Ubaydullo
"""
import unittest 
from juft_son import juft
class juft_son(unittest.TestCase):
    def juft(self):
        a = [45,78,64,31,49]
        self.assertEqual(juft(a), [45,78,64])
        
unittest.main()


        
