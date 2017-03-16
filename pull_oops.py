f = open('fcb_sorry.txt')
start = []
end = []
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

for line in f:
	if len(line.split()) > 2: 
		if is_number(line.split()[1]):
			print(line)
			start.append(str(float(line.split()[1]) - 0.5))
			end.append(str(float(line.split()[2]) + 0.5))

g = open('fcb_sorry_labels.txt', 'w')
for x in range(0, len(start)):
	g.write(start[x] + '\t' + end[x] + '\t' + 'sorry\n')

