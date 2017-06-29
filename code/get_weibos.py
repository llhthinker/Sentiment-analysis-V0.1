import csv
import time
import re

input_file1 = '../input_data/data.csv'
input_file2 = '../input_data/data_new.csv'

output_file = '../output_data/weibo.txt'


if __name__ == "__main__":
    start_time = time.time()
    out_data = open(output_file, 'w', encoding='utf-8')
    weibo = set()
    count = 0
    with open(input_file1, encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # print(row)
            # break
            new_weibo = row[1]+'\n'
            if new_weibo not in weibo:
                weibo.add(new_weibo)
                count = count + 1

    with open(input_file2, encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            new_weibo = row[2]+'\n'
            if new_weibo not in weibo:
                weibo.add(new_weibo)
                count = count + 1
    end_time = time.time()
    print("time cost of get weibos: %.2fs" % (end_time-start_time))
    print("weibo count: ", count)
    print("writing...")
    start_time = time.time()
    out_data.writelines(weibo)
    out_data.close()
    end_time = time.time()
    print("time cost of write file: %.2fs" % (end_time-start_time))
