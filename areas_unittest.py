# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:38:17 2016

@author: marioromero
"""

import areas 
import unittest

# UNIDADES DE TEST
class Areas(unittest.TestCase):
    def test_cuadrado(self):
        self.assertEqual(areas.cuadrado(2), 4)
        
    def test_circulo(self):
        self.assertEqual(areas.circulo(1), areas.pi)
    
suite = unittest.TestLoader().loadTestsFromTestCase(Areas)
unittest.TextTestRunner(verbosity=2).run(suite)