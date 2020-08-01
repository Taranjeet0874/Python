#STUDENT ATTENDANCE ANALYSIS
from matplotlib import pyplot as pt
import numpy as np
ROLL_NO=[1,2,3,4,5,6,7,8,9,10]
ATTENDANCE=[70,75,89,80,84,78,100,92,93,95]
a=np.array(ROLL_NO)
b=np.array(ATTENDANCE)
pt.plot(a,b)
pt.show()