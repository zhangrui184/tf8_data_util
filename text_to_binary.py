import sys
import struct

from tensorflow.core.example import example_pb2
file_path="D:\python project me\data\my_piont_play/train/train_small3.txt"
file_out_file="D:\python project me\data\my_piont_play/train/train_small3.bin"

def read_text_file(text_file):
    lines = []
    with open(text_file, "r",encoding="utf-8") as f:
    #with open(text_file, "r", encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines
def _text_to_binary():
   # inputs = open(file_path, 'r',encoding="utf-8").readlines()
    with open(file_out_file, 'wb') as  writer:
        lines = read_text_file(file_path)
        for i, new_line in enumerate(lines):
            if i % 2 == 0:
                article = lines[i]
            if i % 2 != 0:
                abstract = "%s %s %s" % ("<s>", lines[i], "</s>")

   # for inp in inputs:
                tf_example = example_pb2.Example()
      #  for feature in inp.strip().split('\t'):
       #     (k, v) = feature.split('=')
        #    tf_example.features.feature[k].bytes_list.value.extend([v])
                tf_example.features.feature['article'].bytes_list.value.extend([bytes(article, encoding='utf-8')])
                tf_example.features.feature['abstract'].bytes_list.value.extend([bytes(abstract, encoding='utf-8')])
                tf_example_str = tf_example.SerializeToString()
                str_len = len(tf_example_str)
                writer.write(struct.pack('q', str_len))
                writer.write(struct.pack('%ds' % str_len, tf_example_str))
        writer.close()
_text_to_binary()