import glob
import subprocess

d = open('kwd_list.kws', 'w')
missed_list = []
overshoot_list = []
true_list = []

for x in range(-12, 15):
	d = open('kwd_list.kws', 'w')
	d.write('shit ' + '/1e' + str(x) + '/\n')
	d.write('shoot ' + '/1e' + str(x) + '/\n')	
	d.write('fuck ' + '/1e' + str(x) + '/\n')
	d.write('damn ' + '/1e' + str(x) + '/\n')
	d.write('dang ' + '/1e' + str(x) + '/\n')
	d.write('oops ' + '/1e' + str(x) + '/\n')
	d.write('sorry ' + '/1e' + str(x) + '/\n')
	d.close()
	subprocess.call('for f in *.wav; do  pocketsphinx_continuous -infile $f -kws kwd_list.kws -hmm /usr/local/share/pocketsphinx/model/hmm/en-us-8khz/ -samprate 8000 -time yes -logfn "${f%.wav}.log" > "${f%.wav}.txt"; done', shell = True)
	missed = 0
	overshoot = 0
	true = 0
	for files in glob.glob('*.txt'):
		line_count = 0
		for line in files:
			line_count += 1
		if line_count < 2:
			missed += 1
		elif line_count > 2:
			overshoot += 1
		else:
			true += 1
	missed_list.append(missed)
	overshoot_list.append(overshoot)
	true_list.append(true)
for x in range(0, 27):
	print(str(x - 12) + ' missed = ' + str(missed_list[x]) + '\tovershoot = ' + str(overshoot_list[x]) + '\ttrue = ' + str(true_list[x]) + '\n')
