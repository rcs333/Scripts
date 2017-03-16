# This is some code that I'm honestly not sure what it does - I'm pretty sure it has something to do with creating a list of file names and durations
import subprocess

for line in open('wav.scp'):
	name = line.split()[0]
	loc = line.split()[1]
	# print(loc)
	# subprocess.call('l=$(ffprobe -i ' + loc + ' -show_entries format=duration -v quiet -f csv="p=0") ', shell=True)
	subprocess.call('echo "' + name + '-' + name + '" "' + name + '" "0.00" $(ffprobe -i ' + loc + ' -show_entries format=duration -v quiet -of csv="p=0") >> segmentsV3', shell=True)  
