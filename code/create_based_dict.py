doc_count_file = "../output_data/doc_count.txt"
neg_file = "../dict/negative.txt"
pos_file = "../dict/positive.txt"
based_neg_file = "../dict/based_neg_dict.txt"
based_pos_file = "../dict/based_pos_dict.txt"
doc_count_file = "../output_data/doc_count.txt"

word_count = open(doc_count_file, 'r', encoding='utf-8').readlines()
neg_words = open(neg_file, 'r', encoding='utf-8').read().split('\n')
pos_words = open(pos_file, 'r', encoding='utf-8').read().split('\n')
doc_count = open(doc_count_file, 'r', encoding='utf-8')



# bnf = open(based_neg_file, 'w', encoding='utf-8')
# bpf = open(based_pos_file, 'w', encoding='utf-8')

based_neg_words = []
based_pos_words = []

for w in word_count:
    word = w.split('\t')[0].strip()
    df = float(w.split('\t')[1].strip())
    if df >= 0.01:
        if word in neg_words:
            based_neg_words.append(word+'\n')
        if word in pos_words:
            based_pos_words.append(word+'\n')

print(len(based_neg_words))
print(len(based_pos_words))
# bnf.writelines(based_neg_words)
# bpf.writelines(based_pos_words)
