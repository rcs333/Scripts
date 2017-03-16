__author__ = 'Ryan Shean'
# This is like some gargabe script that I used for sphinx maybe? Probobly won't need to use unlesss you're outputting CTM files and need to extract them from audio using audacity labels

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


