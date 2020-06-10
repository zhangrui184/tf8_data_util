#replace <s> and </s>，remove the " " to ""，jion the token to sentence
#help binary_to_text2.py，can run but not use finally
import sys


#in_file="D:\python project me\data\my_piont_play/train/train_bin_to_txt3.txt"
#out_file="D:\python project me\data\my_piont_play/train/train_bin_to_txt3_none.txt"

def replace(in_file,out_file):
    sents = []
    with open(in_file, "r") as f1:
        for line in f1.readlines():
            line1 = line.replace("<s>", "")
            line2 = line1.replace("</s>", "")
            sents.append(line2)
    with open(out_file, "w") as f2:
        for sent in sents:
            f2.write(sent)
    sys.stderr.write('Done replacing\n')
def jion(in_file,out_file):
    sents=[]
    with open(in_file, "r") as f1:
        for line in f1.readlines():
            line1 = line.replace(" ", "")
            sents.append(line1)
    with open(out_file,"w") as f2:
        for sent in sents:
            f2.write(sent)
    sys.stderr.write('Done jioning\n')