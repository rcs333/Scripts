# Okay this file is actually one you'll need. It takes in a cleaned transcript file like produced by our annotators /fileloc/ transcript
# and it produces the files - this script is referenced in the nuclino documentation so have fun
d = open('/home/ryan/final_cleaned_3.txt')
text = open('text', 'w')
wav = open('wav.scp', 'w')
u2s = open('utt2spk', 'w')
pre_seg = open('preseg', 'w')
x = 0

for line in d:
    x += 1
    count = str(x).zfill(5)
    ext_file_name = line.split()[0]

    transcript = ' '.join(line.split()[1:])
    rec_id = ext_file_name.split('/')[-1].split('.wav')[0]
    spk_id = rec_id
    utt_id = rec_id + '-' + rec_id
    text.write(utt_id + '\t' + transcript + '\n')
    wav.write(rec_id + '\t' + ext_file_name + '\n')
    u2s.write(utt_id + '\t' + spk_id + '\n')
    pre_seg.write(utt_id + '\t' + rec_id + '\t' + '0.0' + '\n')


