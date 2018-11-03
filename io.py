import wfdb
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from IPython.display import display
from wfdb import processing

dir_rec = 'mitdb/205'
start = 7000
end = 10000

signals, fields = wfdb.rdsamp(dir_rec,sampfrom=start,sampto=end)
ann = wfdb.rdann(dir_rec, 'atr', sampfrom=start,sampto=end)
print("***************************************************************")
print(ann)
print(signals)
print(fields)
print("***************************************************************")
# display(signals)

print(len(signals))
print("***************************************************************")
MLII = signals[:,0]
V1 = signals[:,1]
print(MLII)
print("***************************************************************")
print(V1)
print("***************************************************************")

plt.plot(MLII)
plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()
# ************** QRS Detectors *****************
xqrs = processing.XQRS(sig=signals[:,0], fs=fields['fs'])
xqrs.detect()
wfdb.plot_items(signal=signals, ann_samp=[xqrs.qrs_inds])
print(xqrs)