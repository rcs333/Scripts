import subprocess
import glob

main_directory = '/home/ryan/Desktop/RawAudio/'

for x in [9]:
	directory = main_directory + 'd6532718_' + str(x) + '/*.wav'
	for s in sorted(glob.glob(directory)):
		subprocess.call('echo \'' + s + '\' >> d6532718_' + str(x) + '_times.txt', shell=True)
        	subprocess.call('sox ' + s + ' -n stat 2>&1 | sed -n \'s#^Length (seconds):[^0-9]*\\([0-9.]*\\)$#\\1#p\' >> d6532718_' + str(x) + '_times.txt', shell=True)
		

