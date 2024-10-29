# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:03:44 2024

@author: Ubaydullo
"""

import unittest
from katta_kichik import eng_katta

class katta(unittest.TestCase):
    def eng_kattasi(self):
        katta = eng_katta(45, 72, 65)       
        self.assertEqual(katta,'72')
unittest.main()

