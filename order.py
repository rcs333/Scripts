# Super important script referenced in Ryan's kaldi data prep 
text_lines = []
seg_lines = []
u2s_lines = []

text = open('text')
for line in text:
	text_lines.append(line)
text.close()

seg = open('segments')
for line in seg:
	seg_lines.append(line)
seg.close()

u2s = open('utt2spk')
for line in u2s:
	u2s_lines.append(line)
u2s.close()

for x in range(0, len(text_lines)):
	old_utt = u2s_lines[x].split()[0]
	spk_id = u2s_lines[x].split()[1]
	utt_id = spk_id + '-' + old_utt
	u2s_lines[x] = utt_id + ' ' + spk_id

	seglist = seg_lines[x].split()
	seglist[0] = utt_id
	seg_lines[x] = ' '.join(seglist)
	
	textlist = text_lines[x].split()
	textlist[0] = utt_id
	text_lines[x] = ' '.join(textlist)

new_text = open('new_text', 'w')
new_seg = open('new_segments', 'w')
new_u2s= open('new_utt2spk', 'w')

for x in range(0, len(text_lines)):
	new_text.write(text_lines[x] + '\n')
	new_seg.write(seg_lines[x] + '\n')
	new_u2s.write(u2s_lines[x] + '\n')
new_text.close()
new_seg.close()
new_u2s.close()
