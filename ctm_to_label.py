__author__ = 'Ryan Shean'


int2words = open('words.txt')
dictionary = []
counter = 0

for words in int2words.readlines():
    dictionary.append(words.split(None, 1)[0])

raw = open("ENG_M.ctm")
out = open("output.txt", 'w')
for words in raw.readlines():
    line = words.split()
    line[4] = dictionary[int(line[4])]
    out.write(line[2] + " " + line[3] + ' ' + line[4] + '\n')


