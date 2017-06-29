# max_df = 0.06, min_df = 1.7274767265698012e-06
import re

doc_count_file = "../output_data/doc_count.txt"
unuse_word_table_file = "../output_data/unuse_word_table.txt"
candidate_word_file = "../output_data/candidate_word.txt"


max_df = 0.06
min_df = 5.182430179709404e-06 # or 1.7274767265698012e-06

doc_count = open(doc_count_file, 'r', encoding='utf-8').readlines()
unuse_word_table = open(unuse_word_table_file, 'r', encoding='utf-8').read()

candidate_word = open(candidate_word_file, 'w', encoding='utf-8')

candidate_word_list = []

filter_re = "[0-9a-zA-Z]"

for word_count in doc_count:
    word_count = word_count.split('\t')
    word = word_count[0].strip()
    if re.search(filter_re, word) is not None:
        continue
    df = float(word_count[1].strip())

    if df > min_df and df < max_df:
        if word_count[0].strip() not in unuse_word_table:
            candidate_word_list.append(word_count[0].strip()+"\n")

candidate_word.writelines(candidate_word_list)