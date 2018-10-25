import wfdb
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

dir_rec = 'mitdb/100'
start = 000
end = 3000

signals, fields = wfdb.rdsamp(dir_rec,sampfrom=start,sampto=end)
print(signals)
print(fields)

print(len(signals))

MLII = signals[:,0]
V1 = signals[:,1]
print(MLII)
print(V1)

plt.plot(MLII)
plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()