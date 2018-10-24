import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

test = pd.read_csv("arrhythmia.data") # --> test variable is pandas dataframe
x = test.values.tolist() # --> convert test dataframe to list
x = x[0]
print(x)
print("=================================================")
# ========= Print new List ========
# x.pop(0)
print(x)
print("=================================================")
# x = np.array(x).reshape(28, 28); # Convert 1x784 list to 28x28 array
# print(x)
# ========= Plot List ========
plt.plot(x)
plt.show()
