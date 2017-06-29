import re


def pre_deal(emotion_set, text):
    # 过滤网址
    text = re.sub('''http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+''', '', text)
    # 过滤@微博名
    text = re.sub('''@[^ :\n\t]+''', '', text)
    # 过滤表情
    emotion = re.findall('''\[[\u4e00-\u9fa5 |a-zA-Z]*\]''', text)
    for emo in emotion:
        emotion_set.add(emo)
    text = re.sub('''\[[\u4e00-\u9fa5 |a-zA-Z]*\]''', '', text)
    # 过滤特定字符
    text = re.sub('''[【|】|(//:)|#|@|//]''', ' ', text)

    return text

weibo_file = '../output_data/weibo.txt'
dealed_weibo_file = "../output_data/dealed_weibo.txt"
emotion_dict = "../dict/emotion_dict.txt"

f_input = open(weibo_file, 'r', encoding='utf-8')
f_output = open(dealed_weibo_file, 'w', encoding='utf-8')
f_emotion = open(emotion_dict, 'w', encoding='utf-8')

dealed_weibo = []
emotion_set = set()

for text in f_input:
    dealed_weibo.append(pre_deal(emotion_set, text))

f_output.writelines(dealed_weibo)
for e in emotion_set:
    f_emotion.write(e + '\n')