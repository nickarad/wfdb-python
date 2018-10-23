# https://github.com/mondejar/ecg-classification.git

from os import listdir, mkdir, system
from os.path import isfile, isdir, join, exists

dir = 'mitdb'#'mitdb/'
#Create folder
dir_out = dir + 'CSV/'
if not exists(dir_out):
	mkdir(dir_out)

records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.dat') != -1)]
#print records

for r in records:

	command = 'rdsamp -r ' + dir + r[:-4] + ' -c -H -f 0 -v >' + dir_out + r[:-4] + '.csv'
	print(command)
	system(command)

system(command_annotations)