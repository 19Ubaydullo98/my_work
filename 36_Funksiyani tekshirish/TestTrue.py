# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:12:13 2024

@author: Ubaydullo
"""

import unittest

from Mantiqiy import tub

class Tub_son(unittest.TestCase):
    def test_tub(self):
        self.assertTrue(tub(11))
        
    def test_tub(self):
        self.assertFalse(tub(11))
unittest.main()