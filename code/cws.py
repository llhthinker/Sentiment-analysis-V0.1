import urllib.request as ur
import urllib
import time
import jieba
import re
from pyltp import Segmentor

#
# def cws_ltp_api(text):
#     url_get_base = "http://api.ltp-cloud.com/analysis/"
#     args = {
#         'api_key': '71k1y3M3t8rTRTxGHf7TrkVkYE3GVl7v9YunYpOT',
#         'text': text,
#         'pattern': 'ws',
#         'format': 'plain'
#     }
#     result = ur.urlopen(url_get_base, urllib.parse.urlencode(args).encode(encoding='utf-8')) # POST method
#     content = result.read().strip()
#     return content.decode('utf-8')
#
# def cws_jieba(text):
#     seg_list = jieba.cut(text, cut_all=False)
#     return " ".join(seg_list)

if __name__ == "__main__":
    cws_model = "F:\\ltp_data\\cws.model"
    weibo_data = "../output_data/dealed_weibo.txt"
    cws_weibo = "../output_data/cws_weibo.txt"
    f = open(weibo_data, 'r', encoding='utf-8')
    out_f = open(cws_weibo, 'w', encoding='utf-8')
    cws_weibo_list = []
    segmentor = Segmentor()
    print("loading weibo and cws model...")
    segmentor.load(cws_model)
    dealed_weibo = f.readlines()
    f.close()
    print("cws...")
    start_time = time.time()
    for text in dealed_weibo:
        words = segmentor.segment(text)
        text = " ".join(words)
        cws_weibo_list.append(text+"\n")
        # print(text)
    end_time = time.time()
    print("time cost of cws: %.2fs" % (end_time-start_time))
    segmentor.release()
    start_time = time.time()
    out_f.writelines(cws_weibo_list)
    end_time = time.time()
    print("time cost of writing: %.2fs" % (end_time-start_time))
    out_f.close()
