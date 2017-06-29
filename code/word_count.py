if __name__ == "__main__":
    cws_weibo_file = "../output_data/cws_weibo.txt"
    doc_count_file = "../output_data/doc_count.txt"
    f_cws_weibo = open(cws_weibo_file, 'r', encoding='utf-8')
    f_doc_count = open(doc_count_file, 'w', encoding='utf-8')

    cws_weibo = f_cws_weibo.readlines()
    doc_freq = {}
    for text in cws_weibo:
        word_list = text.split(' ')
        word_set = set(word_list)
        for word in word_set:
            word = word.strip()
            if word in doc_freq:
                doc_freq[word] += 1
            else:
                doc_freq[word] = 1

    sorted_doc_freq = sorted(doc_freq.items(), key=lambda x: x[1], reverse=True)
    doc_freq_list = []
    for d in sorted_doc_freq:
        doc_freq_list.append(d[0].strip()+"\t"+str(d[1]/len(cws_weibo))+"\n")

    f_doc_count.writelines(doc_freq_list)


