# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:15:46 2019

@author: Dell
"""
from matplotlib import pyplot as pt
import numpy as np
ROLL_NO=[1,2,3,4,5,6,7,8,9,10]
ATTENDANCE=[100,78,89,80,85,95,98,89,86,96]
a=np.array(ROLL_NO)
b=np.array(ATTENDANCE)
pt.plot(a,b)
pt.show() 