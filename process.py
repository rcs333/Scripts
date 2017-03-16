f = open('truth.txt')

fline = ''

for line in f:
	fline += line

l = fline.split('/media/')
f = open('d.txt', 'w')
for s in l:
	f.write(s + '\n')

