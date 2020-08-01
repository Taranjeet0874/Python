# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:04:06 2019

@author: Dell
"""

import numpy as np
l=[1,2,3,4]
arr=np.array(l)
print(arr)
print(arr.ndim)
print(arr.shape)
a=arr.reshape(2,2)

print(a)
print(a.ndim)