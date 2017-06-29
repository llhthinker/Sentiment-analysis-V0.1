import csv
import time
import re

def get_weibos_by_name(name):
    input_file = '../input_data/data_new.csv'
    start_time = time.time()
    weibos = {}
    count = 0
    with open(input_file, encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[8] == name:
                new_weibo = row[2]+'\n'
                send_time = row[3]
                weibos[send_time] = new_weibo
                count = count + 1
    weibo_list = sorted(weibos.items(), key=lambda d:d[0])
    end_time = time.time()
    print("time cost of get weibos: %.2fs" % (end_time-start_time))
    print("weibo count: ", count)
    return weibo_list

name="qetina"
for weibo in get_weibos_by_name(name):
    print(weibo)
