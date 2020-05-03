from spell_checker import cn_correct
import jieba

m_list=['你','那','为','的','了','呢','太','呀','很','真','是','吗','我','有','也','地','他','她','它','给','让','请','将','这','帮','能','在']
bd_list=['"','"','“','”','。','.',',','，','!','！','?','？',';','；','、','：',':']

def cheakBD(word):
    for i in bd_list:
        if(i==word):
            return True
    return False

def cheakM(word):
    for i in m_list:
        if(i==word):
            return False
    return True

def cheekEn(word):
    if((word>='a' and word<='z') or (word>='A' and word<='Z')):
        return True
    return False

def cn_sen_correct(res):
    out=''
    next_b=False
    for i in range(len(res)):
        if(next_b):
            next_b=False
            continue
        if(len(res[i])<2 and i<len(res)):
            if(cheakBD(res[i]) or res[i]==' ' or cheekEn(res[i])):
                out=out+res[i]
                continue
            if(i<len(res)-1 and cheakM(res[i]) and cheakM(res[i+1]) and not cheakBD(res[i+1])):
                out=out+cn_correct(res[i]+res[i+1])
                next_b=True
            #elif(cheakM(res[i+1]) and len(res[i+1])>1):
                #out=out+res[i]+cn_correct(res[i+1])
            else:
                out=out+res[i]
        elif(i==0 or len(res[i])>=2):
            out=out+cn_correct(res[i])
    return out

while(1):
    res=list(jieba.cut(input('input: ')))
    print(cn_sen_correct(res))
