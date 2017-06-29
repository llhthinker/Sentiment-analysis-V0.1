import math


based_neg_file = "../dict/based_neg_dict.txt"
based_pos_file = "../dict/based_pos_dict.txt"
neg_file = "../dict/negative.txt"
pos_file = "../dict/positive.txt"
candidate_word_file = "../output_data/candidate_word.txt"
doc_count_file = "../output_data/doc_count.txt"


unuse_word_table_file = "../output_data/unuse_word_table.txt"
unuse_word_table = open(unuse_word_table_file, 'r', encoding='utf-8').read().split(' ')

bnf = open(based_neg_file, 'r', encoding='utf-8')
bpf = open(based_pos_file, 'r', encoding='utf-8')

candidate_word = open(candidate_word_file, 'r', encoding='utf-8').read().split('\n')
neg_words = open(neg_file, 'r', encoding='utf-8').read().split('\n')
pos_words = open(pos_file, 'r', encoding='utf-8').read().split('\n')

doc_count = open(doc_count_file, 'r', encoding='utf-8')
doc_count_dict = {}
for dc in doc_count:
    word = dc.split('\t')[0].strip()
    freq = float(dc.split('\t')[1].strip())
    doc_count_dict[word] = freq

cws_weibo_file = '../output_data/weibo.txt'
cws_weibo = open(cws_weibo_file, 'r', encoding='utf-8').read().split('\n')
print(len(cws_weibo))

def PMI(word1, words, cws_weibo):
    pmi = 0
    p_word1 = doc_count_dict[word1]
    n = len(cws_weibo)
    for w in words:
        p_w = doc_count_dict[w]
        count = 0
        for cw in cws_weibo:
            if word1 in cw and w in cw:
                count += 1
        p_word1_w = count * 1.0 / n
        if p_word1_w != 0 and p_word1*p_w != 0:
            pmi += math.log(n*p_word1_w/(p_word1*p_w), 2)
    return pmi

def SO_PMI(word1, Pwords, Nwords, cws_weibo):
    p_pmi = PMI(word1, Pwords, cws_weibo)
    n_pmi = PMI(word1, Nwords, cws_weibo)
    return p_pmi - n_pmi


based_neg_word_list = []
based_pos_word_list = []
for neg_word in bnf:
    based_neg_word_list.append(neg_word.split('\t')[0].strip())
    based_neg_word_list.append(neg_word.split('\t')[1].strip())
for pos_word in bpf:
    based_pos_word_list.append(pos_word.split('\t')[0].strip())
    based_pos_word_list.append(pos_word.split('\t')[1].strip())

field_neg_set = set()
field_pos_set = set()

for cw in candidate_word[:10]:
    if cw in unuse_word_table:
        print(cw + ' is unuse word')
        continue
    if cw in pos_words or cw in neg_words:
        print(cw + " is exist")
        continue
    so_pmi = SO_PMI(cw, based_pos_word_list, based_neg_word_list, cws_weibo=cws_weibo)
    print(so_pmi)
    #print(cw)
    if  so_pmi > 0:
        print(cw + ' is pos')
        field_pos_set.add(cw+"\n")
    elif so_pmi < 0:
        print(cw + ' is neg')
        field_neg_set.add(cw+"\n")
    else:
        print(cw + ' is neutral')
        continue

field_neg_file = "../dict/field_neg_dict.txt"
field_pos_file = "../dict/field_pos_dict.txt"

field_neg = open(field_neg_file, 'w', encoding='utf-8')
field_pos = open(field_pos_file, 'w', encoding='utf-8')

field_neg.writelines(field_neg_set)
field_pos.writelines(field_pos_set)

