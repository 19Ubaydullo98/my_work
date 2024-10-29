# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:37:42 2024

@author: Ubaydullo
"""
# MODULNI O'ZINI CHAQIRISH
import Inkapsulatsiya_31

avto1 = Inkapsulatsiya_31.Avto("GM", "Matiz", "white", 2016, 5400, 1000)
avto2 = Inkapsulatsiya_31.Avto("GM", "cobalt", "white", 2020, 10400)
avto3 = Inkapsulatsiya_31.Avto("GM", "spark", "black", 2018, 7400, 6000)

# BIR NECHTA KLASSLARNI IMPORT QILISH####MODULNI O'ZINI BITTA KLASSNI IMPORT QILISH
from Inkapsulatsiya_31 import Avto

avto1 = Avto("GM", "Matiz", "white", 2016, 5400, 1000)
avto2 = Avto("GM", "cobalt", "white", 2020, 10400)
avto3 = Avto("GM", "spark", "black", 2018, 7400, 6000)

# MODULDAGI BARCHA KLASSLARNI IMPORT QILISH
from Inkapsulatsiya_31 import * 
avto1 = Inkapsulatsiya_31.Avto("GM", "Matiz", "white", 2016, 5400, 1000)
avto2 = Inkapsulatsiya_31.Avto("GM", "cobalt", "white", 2020, 10400)
avto3 = Inkapsulatsiya_31.Avto("GM", "spark", "black", 2018, 7400, 6000)