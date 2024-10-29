# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:40:25 2024

@author: Ubaydullo
"""

import unittest 
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name("alijon", "valiyev")
        self.assertEqual(name, "Alijon Valiyev")
        # asserEqual  tenglikni tekshirish
        
    def test_otasining_ismi(self):
        name = get_full_name("alijon", "valiyev","Olimovich")
        self.assertEqual(name, "Alijon Olimovich Valiyev")
unittest.main()   # bu orqali shunga So'nggi qatorda unittest klassinini chaqiramiz, 
# # bu esa o'z navbatida biz yuqorida yozgan testni chaqiradi. 
        
# print(get_full_name("shokir", "jalilow", "islamov"))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        