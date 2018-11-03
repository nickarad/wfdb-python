import wfdb
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

from os import listdir, mkdir, system
from os.path import isfile, isdir, join, exists

# ********** Save annotation files in a list *************
dir_ann = 'mitdbCSV/'#'mitdb/'
annotations = [f for f in listdir(dir_ann) if isfile(join(dir_ann, f)) if(f.find('.txt') != -1)]

annotations.sort() # ==> Sort the list
print(annotations[0]) # ==> print the list
# ---------------------------------------------------------

test = pd.read_csv(dir_ann + annotations[0]) # --> test variable is pandas dataframe
x = test.values.tolist() # --> convert test dataframe to list
# x = x[0]
print(x[0:4])