
positive_word = set()
negative_word = set()

def create_word_set(word_set, infiles, outfile):
    out_f = open(outfile, 'w', encoding='utf-8')
    for f in infiles:
        f = open(f, 'r', encoding='utf-8')
        for w in f:
            word_set.add(w.strip()+'\n')
    out_f.writelines(word_set)

negative_files = ["../dict/negative1.txt",
                  "../dict/negative2.txt",
                  "../dict/negative3.txt",
                  ]
positive_files = ["../dict/positive1.txt",
                  "../dict/positive2.txt",
                  "../dict/positive3.txt",
                  ]
negative_dict = "../dict/negative.txt"
positive_dict = "../dict/positive.txt"

create_word_set(negative_word, negative_files, negative_dict)
create_word_set(positive_word, positive_files, positive_dict)
