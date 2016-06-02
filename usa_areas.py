# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:31:06 2016

@author: marioromero
"""

import areas

lados = [1,2,3,4,10,100,500]
for lado in lados:
    print("Area del cuadrado de lado {} es {}".format(lado,areas.cuadrado(lado)))
    
for radio in lados:
    print("Area del cirulo de radio {} es {}".format(radio,areas.circulo(radio)))
    
if __name__ == 'areas':
    import sys
    print ('Numero de parametros =', len (sys.argv))
    for s in sys.argv:
        print (s, '->', type(s))