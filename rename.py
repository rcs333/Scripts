lines = []
with open("filename.txt") as f:
    for line in f:
        lines.append(line[0:19])

print(lines)
newlines = []
for line in lines:
    newlines.append('file \''+line+'\'')
print(newlines)

b = open("blank.txt", 'w')
for line in newlines:
    b.write(line+'\n')