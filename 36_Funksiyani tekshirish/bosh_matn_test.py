# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:20:51 2024

@author: Ubaydullo
"""
import unittest
from bosh_harf import bosh_harf

class bosh_letter(unittest.TestCase):
    def letter(self):
        a = ["ali"]
    
        self.assertEqual(bosh_harf(a), ["Ali"])

unittest.main()    
    
    
    


