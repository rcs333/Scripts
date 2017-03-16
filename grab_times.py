# Honestly no idea what this does. 
def pull_times(filename, linenumber):
    f = open(filename)
    count = 1
    for thing in f:
        if count == linenumber:
            return thing
        count += 1


d = open('timestamps.txt', 'w')

for line in open('filenames.txt'):
    label_file = line.split('-')[0]
    print(label_file + '.txt.label')
    label_line_num = line.split('-')[1].split('.')[0]
    print(label_line_num)
    new_line = pull_times(label_file + '.txt.label', int(label_line_num))
    d.write(label_file + '\t' + new_line)
