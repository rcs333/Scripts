import glob
import subprocess
list = glob.glob('/home/ryan/kws_test/wav/*.wav')
total = 1 * len(list)
count = 0
for audio_file in list:
   subprocess.call('./kaldi/src/online2bin/online2-wav-nnet2-latgen-faster --do-endpointing=false\   --online=false \
    --config=nnet_a_gpu_online/conf/online_nnet2_decoding.conf \
    --max-active=7000 --beam=15.0 --lattice-beam=6.0 \
    --word-symbol-table=graph/words.txt \
    nnet_a_gpu_online/final.mdl graph/HCLG.fst "ark:echo utterance-id1 utterance-id1|" "scp:echo utterance-id1 ' + audio_file + '|" \
    ark:' + audio_file + '.transcript', shell=True)
   count += 1
   print(str(count) + ' of + ' + str(total))

