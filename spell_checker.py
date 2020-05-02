import os
import collections
import pypinyin
#import jieba
import difflib
from radical import Radical

def getBushou(word):
    radical = Radical()
    res=radical.get_radical(word)
    return res

def cn_ci(dir_path):
    all_text = ""
    for file_name in os.listdir(dir_path):
        if file_name.find(".txt") != -1:
            file_path = "/".join([dir_path, file_name])
            with open(file_path, "rb") as f:
                all_text += f.read().decode("utf-8")

    #terms = jieba.cut(all_text)
    terms=all_text.split(' ')

    return [ci for ci in ','.join(terms).split(',') if ci not in ['', " "]]

def cn_train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

CNWORDS = cn_train(cn_ci("cn_texts"))

def cn_hanzi():
    with open("zi_data.txt", "rb") as f:
        hanzi = f.read().decode("utf-8")
        return hanzi

cn_hanzi_str = cn_hanzi()

def cn_edits1(ci):
    splits     = [(ci[:i], ci[i:]) for i in range(len(ci)   + 1)]
    deletes    = [a + b[1:] for a, b in splits if b if a + b[1:] in CNWORDS]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1 if a + b[1] + b[0] + b[2:] in CNWORDS]
    replaces   = [a + c + b[1:] for a, b in splits for c in cn_hanzi_str if b if a + c + b[1:] in CNWORDS]
    inserts    = [a + c + b     for a, b in splits for c in cn_hanzi_str if a + c + b in CNWORDS]
    return set(deletes + transposes + replaces + inserts)

def cn_known_edits2(ci):
    return set(e2 for e1 in cn_edits1(ci) for e2 in cn_edits1(e1) if e2 in CNWORDS)

def getPiny(ci):
    outs=''
    for item in pypinyin.lazy_pinyin(ci):
        outs=outs+item
    return outs

def cheaklike(ci,yuan):
    seq = difflib.SequenceMatcher(None,ci,yuan)
    return seq.ratio()

def cn_correct(ci):
    candidates = cn_edits1(ci) or cn_known_edits2(ci)
    if(ci in candidates):
        return ci
    tid=getPiny(ci)
    tbu=getBushou(ci[0])
    maxi=-1
    maxv=0
    for i in candidates:
        nowid=getPiny(i)
        nowbu=getBushou(i[0])
        temp=cheaklike(nowid,tid)*0.9+cheaklike(nowbu,tbu)*0.1
        if(temp>maxv):
            maxv=temp
            maxi=i
            #print(i+': '+str(maxv))

    if(maxv>0.85):
        return maxi
    try:
        return max(candidates, key=CNWORDS.get)
    except:
        return ci

#print(len(list(CNWORDS.items())[0][0]))

#while(True):
    #print(cn_correct(input('Word: ')))
