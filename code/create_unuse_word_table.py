def create_unuse_word_table(files):
    unuse_word_table = set()
    for f in files:
        unuse_word_list = open(f, 'r', encoding='utf-8').readlines()
        for word in unuse_word_list:
            word = word.split('\t')[0].strip()
            unuse_word_table.add(word+'\n')
    return unuse_word_table

files = ["../input_data/diy_unuse_word.txt",]

unuse_word_table_file = "../dict/unuse_word_table.txt"
unuse_word_table = open(unuse_word_table_file, 'w', encoding='utf-8')
unuse_word_table.writelines(create_unuse_word_table(files))