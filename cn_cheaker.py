from spell_checker import cn_correct
import jieba
import jieba.posseg as pseg

m_list=['你','那','为','了','呢','太','呀','很','真','是','吗','我','有','也','他','她','您','它','给','让','请','对','将','这','每','帮','能','在']
bd_list=['"','"','“','”','。','.',',','，','!','！','?','？',';','；','、','：',':','《','》']

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

def de_correct(cx_q,cx_h):
    if((cx_q=='d' or cx_q=='a') and cx_h=='v'):
        return '地'
    if(cx_q=='v' and cx_h=='a'):
        return '得'
    return '的'

def cn_sen_correct(res,cx):
    out=''
    next_b=False
    for i in range(len(res)):
        if(next_b):
            next_b=False
            continue
        if(len(res[i])<2 and i<len(res)):
            if(res[i]=='的' or res[i]=='地' or res[i]=='得'):
                if(i+1==len(res)):
                    out=out+de_correct(cx[i-1],'')
                else:
                    out=out+de_correct(cx[i-1],cx[i+1])
                continue
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
    inText=input('input: ')
    res=list(jieba.cut(inText))
    print(cn_sen_correct(res,[x.flag for x in pseg.cut(inText)]))
