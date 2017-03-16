import glob
import subprocess
import time
import os.path

"""
Ryan's Annotation program:

I'll set up a huge amount of files, so when you hit run the first one will play
    Run is either the little green triangle in the top right or Ctrl-Shift-F10

Type in your annotation and hit the return key and a new one will play

To replay append 1 <- (The number one) to your annotation

You can start typing as soon as the playing starts although you won't be able to see it, it'll still get recorded

If the file is just noise or incomprehensible type in <noise>

If the file doesn't play and there's an error like 'Under-Run' just hit enter and move to the next file.

You can stop anytime you like by either just leaving the program running, or hitting the red square (progress *should*
    be saved)

slang should be typed exactly as it is said i.e. 'gonna' 'wanna' ect. swearwords are important too!

As a general rule, incomplete annotations are worse than skipping one so keep that in mind, although you can let me know
    or write a message with {message} which I'll run into when I'm processing your annotations.



Please let me know if you hate using this program to annotate and I can hook you up with either improvements to this code
or some other options, If you find some other program online or something and you want to use let me know as well.
"""


output_file = '/home/ryan/output.txt'
file_dir = '/home/ryan/Desktop/ToSort/ffb/subset/'


def transcribe(filepath, string):
    subprocess.call('play ' + filepath, shell=True)
    print('Transcription:\n' + string + '\n')
    input = raw_input('Enter transcription:')
    string = string + ' ' + input
    if string[-1].rstrip() == '1':
        return transcribe(filepath, string[:-1])
    elif string[-1].rstrip() == '2':
        return '2'
    else:
        return string

if __name__ == '__main__':
    input = raw_input('Enter Name, and hit Enter to begin! [new feature!]')
    time = time.strftime("%d.%m.%Y")
    header = '#' + input + ' ' + time

    for wav in sorted(glob.glob(file_dir + '*.wav')):
        txt = '.'.join(wav.split('.')[:-1]) + '.txt'
        if not os.path.isfile(txt):
            # Begin transcription
            trans = transcribe(wav, '')
            if trans == '2':
                break
            f = open(txt, 'w')
            f.write(wav + '\t' + trans + '\n')
            f.close()

    subprocess.call('cat ' + file_dir + '*.txt' + ' > /home/ryan/' + header.replace(' ', '') + '.txt', shell=True)
