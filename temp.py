#STUDENT ATTENDANCE ANALYSIS
from matplotlib import pyplot as pt
import numpy as np
ROLL_NO=[1,2,3,4,5,6,7,8,9,10]
ATTENDANCE=[89,87,75,69,98,91,95,77,67,100]
a=np.array(ROLL_NO)
b=np.array(ATTENDANCE)
pt.plot(a,b)
pt.show()