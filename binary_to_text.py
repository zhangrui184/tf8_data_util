import sys
import struct

from tensorflow.core.example import example_pb2
file_path="D:\python project me\data\my_piont_play/train/train_bin3.bin"
file_out_file="D:\python project me\data\my_piont_play/train/train_bin_to_txt3.txt"
def _binary_to_text():
    reader = open(file_path, 'rb')
    writer = open(file_out_file, 'w')
   # with open(file_out_file,"w"):
    examples_txts = []
    while True:
        len_bytes = reader.read(8)
        if not len_bytes:
            sys.stderr.write('Done reading\n')
            return
        str_len = struct.unpack('q', len_bytes)[0]
        tf_example_str = struct.unpack('%ds' % str_len, reader.read(str_len))[0]
        tf_example = example_pb2.Example.FromString(tf_example_str)
        examples = []
        #for key in tf_example.features.feature:
        #    examples.append('%s=%s' % (key, tf_example.features.feature[key].bytes_list.value[0]))
        for key in tf_example.features.feature:
           # examples.append('%s' % (tf_example.features.feature[key].bytes_list.value[0]))
            examples.append(tf_example.features.feature[key].bytes_list.value[0])

        for exp in examples:
            examples_txt=exp.decode()
            examples_txts.append(examples_txt)

       # writer.write('%s\n' % '\t'.join(examples_txts))
        writer.write('%s\n' % '\n'.join(examples_txts))
       # writer.write('%s\n' % '\t'.join(examples))
   # reader.close()
    #writer.close()

_binary_to_text()