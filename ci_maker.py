import os
import jieba

def cn_ci(dir_path):
    all_text = ""
    for file_name in os.listdir(dir_path):
        if file_name.find(".txt") != -1:
            file_path = "/".join([dir_path, file_name])
            with open(file_path, "rb") as f:
                all_text = f.read()#.decode("utf-8")
            with open(file_path, "w",encoding='utf-8') as f:
                terms = jieba.cut(all_text)
                f.write(' '.join(terms))

#cn_ci("cn_texts")
