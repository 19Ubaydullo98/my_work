# -*- coding: utf-8 -*-
"""
Created on Sat May 18 05:26:48 2024

@author: Ubaydullo
"""

import unittest
from circle import getArea, getPeremetr

class Test(unittest.TestCase):
    def test_area(self):
        name  = getArea(15)
        self.assertEqual(name, 706.85775)
        self.assertAlmostEqual(getArea(10), 314.159)

   # def test_peremetr 
unittest.main()
