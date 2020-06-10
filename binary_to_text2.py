#.bin to .txt directly
import sys
import struct
import replace_s_to_none as replace
from tensorflow.core.example import example_pb2
#file_path="/home/ddd/data/cnndailymail3/finished_files/train.bin"
#file_out_file="/home/ddd/data/cnndailymail3/finished_files/original/train/train_bin_to_txt.txt"
file_path="/home/ddd/data/cnndailymail3/finished_files/test.bin"
file_out_file="/home/ddd/data/cnndailymail3/finished_files/original/test_bin_to_txt.txt"
def _binary_to_text():
    reader = open(file_path, 'rb')
    writer = open(file_out_file, 'w')
    examples_txts = []
    while True:
        len_bytes = reader.read(8)
        if not len_bytes:
            sys.stderr.write('Done reading\n')
            writer.write('%s\n' % '\n'.join(examples_txts))
            return
        str_len = struct.unpack('q', len_bytes)[0]
        tf_example_str = struct.unpack('%ds' % str_len, reader.read(str_len))[0]
        tf_example = example_pb2.Example.FromString(tf_example_str)
        examples = []

        for key in tf_example.features.feature:
            examples.append(tf_example.features.feature[key].bytes_list.value[0])

        #for exp in examples:
        #    examples_txt=exp.decode()
        #    examples_txt_none=examples_txt.replace("<s>", "")
         #   examples_txt_none=examples_txt_none.replace("</s>", "")
         #   examples_txt_none=examples_txt_none.replace(" ", "")
         #   examples_txts.append(examples_txt_none)
         #   sys.stderr.write('already replace the %s s sentences\n' % ''.join(str(len(examples_txts))))
        for exp in examples:
            exp = exp.decode()
            exp = exp.replace("<s>", "")
            exp = exp.replace("</s>", "")
            exp = exp.replace(" ", "")
            examples_txts.append(exp)
            if len(examples_txts)%100000 ==0 :
               sys.stderr.write('already replace the %s s sentences\n' % ''.join(str(len(examples_txts))))


_binary_to_text()
