# -*- coding: utf-8 -*-
"""
Author: LiGorden

Translation of laguage using google
"""
import pandas as pd
from google_trans_new import google_translator
from collections import Counter

# Import in data
data = pd.read_csv("Musical_instruments_reviews.csv")
data = data.loc[:, ['reviewText', 'overall']]

# Delete Null Samples
float_ind = list()
str_ind = list()
for ind in data.index:
    if type(data.loc[ind, 'reviewText']) == float:
        float_ind.append(ind)
    elif type(data.loc[ind, 'reviewText']) == str:
        str_ind.append(ind)
    else:
        print(str(i) + ': ' + str(type(data.loc[ind, 'reviewText'])))

# Delete blank samples
data.drop(labels=None, axis=0, index=float_ind, columns=None, inplace=True)
sentences = list(data.loc[:, 'reviewText'])
reviews = list(data.loc[:, 'overall'])

# -------------------------------------------------------------------------------------
# Balance the data
frequency = dict(Counter(reviews))
frequency_max = max(frequency.values())
repetition = {4: round(frequency_max/2084) - 1, 3: round(frequency_max/772) - 1,
              2: round(frequency_max/250) - 1, 1: round(frequency_max/217) - 1}

sentence_to_augment = data.drop(labels=None, axis=0,
                                index=data[data['overall'] == 5].index,
                                columns=None, inplace=False)
sentence_to_augment_4 = sentence_to_augment[sentence_to_augment['overall'] == 4]
sentence_to_augment_3 = sentence_to_augment[sentence_to_augment['overall'] == 3]
sentence_to_augment_2 = sentence_to_augment[sentence_to_augment['overall'] == 2]
sentence_to_augment_1 = sentence_to_augment[sentence_to_augment['overall'] == 1]

"""
# Using Google_Trans_New
# 32 language is used
language_list = ['cn', 'fr', 'ja', 'it', 'nl', 'de', 'el', 'ko', 'la',
                 'ru', 'es', 'th', 'tr', 'af', 'sq', 'am', 'ar', 'tl', 'ka',
                 'hi', 'hu', 'is', 'ig', 'id', 'ga', 'hy', 'az', 'eu', 'be',
                 'bn', 'bg', 'bs']

translator = google_translator()

# Augment 4 star review
sentences_augmented_4 = list()
for ind in sentence_to_augment_4.index:
    rating = sentence_to_augment_4.loc[ind, 'overall']
    repeat = repetition[rating]
    sentence = sentence_to_augment_4.loc[ind, 'reviewText']
    print('Original Sentence: ', sentence)
    for i in range(repeat):
        translate_text = translator.translate(sentence, lang_tgt=language_list[i])
        translate_text = translator.translate(translate_text, lang_tgt='en')
        print('Generated Sentence-', str(language_list[i]), ': ', translate_text)
        sentences_augmented_4.append([translate_text, rating])
        print('--------------------------------------------------------')

pd.DataFrame(sentences_augmented_4, columns=['reviewText', 'overall']).to_csv('sentence_augmented_4.csv')

# Augment 3 star review
translator = google_translator()
sentences_augmented_3 = list()
for ind in sentence_to_augment_3.index:
    print(ind)
    rating = sentence_to_augment_3.loc[ind, 'overall']
    repeat = repetition[rating]
    sentence = sentence_to_augment_3.loc[ind, 'reviewText']
    print('Original Sentence: ', sentence)
    for i in range(repeat):
        translate_text = translator.translate(sentence, lang_tgt=language_list[i])
        translate_text = translator.translate(translate_text, lang_tgt='en')
        print('Generated Sentence-', str(language_list[i]), ': ', translate_text)
        sentences_augmented_3.append([translate_text, rating])
        print('--------------------------------------------------------')

pd.DataFrame(sentences_augmented_3, columns=['reviewText', 'overall']).to_csv('sentence_augmented_3.csv')

# Augment 2 star review
translator = google_translator()
sentences_augmented_2 = list()
for ind in sentence_to_augment_2.index:
    rating = sentence_to_augment_2.loc[ind, 'overall']
    repeat = repetition[rating]
    sentence = sentence_to_augment_2.loc[ind, 'reviewText']
    print('Original Sentence: ', sentence)
    for i in range(repeat):
        translate_text = translator.translate(sentence, lang_tgt=language_list[i])
        translate_text = translator.translate(translate_text, lang_tgt='en')
        print('Generated Sentence-', str(language_list[i]), ': ', translate_text)
        sentences_augmented_2.append([translate_text, rating])
        print('--------------------------------------------------------')

pd.DataFrame(sentences_augmented_2, columns=['reviewText', 'overall']).to_csv('sentence_augmented_2.csv')
"""

"""
# Using youdao translate package
import json
import requests


def translate(word):
    def get_response(word):
        # 有道词典 api
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        # 传输的参数，其中 i 为需要翻译的内容
        key = {
            "type": "AUTO",
            "i": word,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        # key 这个字典为发送给有道词典服务器的内容
        response = requests.post(url, data=key)
        # 判断服务器是否相应成功
        if response.status_code == 200:
            # 然后相应的结果
            return response.text
        else:
            print("有道词典调用失败")
            # 相应失败就返回空
            return None

    response = get_response(word)
    if response:
        result = json.loads(response)
        return result['translateResult'][0][0]['tgt']
    else:
        return word, None


tgt = translate("开玩笑啦!")
tgt = translate(tgt)
print(tgt)  # 翻译的结果：A joke!


# Augment 1 star review
sentences_augmented_1 = list()
for ind in sentence_to_augment_1.index:
    rating = sentence_to_augment_1.loc[ind, 'overall']
    repeat = repetition[rating]
    sentence = sentence_to_augment_1.loc[ind, 'reviewText']
    print('Original Sentence: ', sentence)
    for i in range(repeat):
        _, tgt = translate(sentence)
        _, tgt = translate(tgt)
        print('Generated Sentence-', str(language_list[i]), ': ', translate_text)
        sentences_augmented_1.append([translate_text, rating])
        print('--------------------------------------------------------')

pd.DataFrame(sentences_augmented_1, columns=['reviewText', 'overall']).to_csv('sentence_augmented_1.csv')

# Augment 2 star review
translator = google_translator()
sentences_augmented_2 = list()
for ind in sentence_to_augment_2.index:
    rating = sentence_to_augment_2.loc[ind, 'overall']
    repeat = repetition[rating]
    sentence = sentence_to_augment_2.loc[ind, 'reviewText']
    print('Original Sentence: ', sentence)
    for i in range(repeat):
        translate_text = translator.translate(sentence, lang_tgt=language_list[i])
        translate_text = translator.translate(translate_text, lang_tgt='en')
        print('Generated Sentence-', str(language_list[i]), ': ', translate_text)
        sentences_augmented_2.append([translate_text, rating])
        print('--------------------------------------------------------')

pd.DataFrame(sentences_augmented_2, columns=['reviewText', 'overall']).to_csv('sentence_augmented_2.csv')
"""

# Using Baidu Translater
import http.client
import hashlib
import urllib
import random
import json
import time

# 百度appid和密钥需要通过注册百度【翻译开放平台】账号后获得
appid = '20211210001024164'  # 填写你的appid
secretKey = 'FTQepLOWwtjHrgIXTLkj'  # 填写你的密钥

httpClient = None


# Define function of Baidu Trans
def baidu_trans(sentence, fromlang='auto', tolang='auto', myurl='/api/trans/vip/translate'):
    salt = random.randint(32768, 65536)
    sign = appid + sentence + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(sentence) + '&from=' + fromlang + \
               '&to=' + tolang + '&salt=' + str(salt) + '&sign=' + sign
    myurl_back = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(sentence) + '&from=' + fromlang + \
               '&to=' + 'en' + '&salt=' + str(salt) + '&sign=' + sign
    # 建立会话，返回结果
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        # 翻译
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)  # ['trans_result'][0]['dst']

        return result['trans_result'][0]['dst']

    except Exception as e:
        print('Error in translate into another language')

    finally:
        if httpClient:
            httpClient.close()

    """
    try:
        # 回译
        httpClient.request('GET', myurl_back)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return result['trans_result'][0]['dst']
    """


language_list = ['zh', 'fra', 'jp', 'ru', 'nl', 'de', 'el', 'kor', 'spa',
                 'th', 'ara', 'it', 'pt', 'pl', 'bul', 'est', 'dan', 'fin', 'cs',
                 'rom', 'slo', 'swe', 'hu', 'vie']

len(set(language_list))

for ind, val in repetition.items():
    if val >= 14:
        repetition[ind] = 14

"""
# Trial
text = sentence_to_augment_2.loc[15, 'reviewText']
text = baidu_trans(text, fromlang='auto', tolang='zh')
time.sleep(0.25)
text = baidu_trans(text, fromlang='auto', tolang='en')
time.sleep(0.25)
print(text)
"""
# Augment 1 star review
sentences_augmented_1 = list()
cur_ind = list(sentence_to_augment_1.index)[0]
last_ind = list(sentence_to_augment_1.index)[-1]
while True:
    try:
        for ind in sentence_to_augment_1.index:
            cur_ind = ind
            rating = sentence_to_augment_1.loc[ind, 'overall']
            repeat = repetition[rating]
            sentence = sentence_to_augment_1.loc[ind, 'reviewText']
            print('Original Sentence: ', sentence)
            for i in range(repeat):
                time.sleep(0.5)  # 两次调用API间需要设定响应时间, 否则会报错
                translate_text = baidu_trans(sentence, fromlang='auto', tolang=language_list[i])
                time.sleep(0.5)
                translate_text = baidu_trans(translate_text, fromlang='auto', tolang='en')
                print('Generated Sentence -', str(language_list[i]), ': ', translate_text)
                sentences_augmented_1.append([translate_text, rating])
                print('--------------------------------------------------------')

        if cur_ind == last_ind:
            break
    except:
        sentence_to_augment_1 = sentence_to_augment_1.loc[cur_ind:, ]
        continue

pd.DataFrame(sentences_augmented_1, columns=['reviewText', 'overall']).to_csv('sentence_augmented_1.csv')

# Augment 2 star review
sentences_augmented_2 = list()
cur_ind = list(sentence_to_augment_2.index)[0]
last_ind = list(sentence_to_augment_2.index)[-1]
while True:
    try:
        for ind in sentence_to_augment_2.index:
            cur_ind = ind
            rating = sentence_to_augment_2.loc[ind, 'overall']
            repeat = repetition[rating]
            sentence = sentence_to_augment_2.loc[ind, 'reviewText']
            print('Original Sentence: ', sentence)
            for i in range(repeat):
                time.sleep(0.4)  # 两次调用API间需要设定响应时间, 否则会报错
                translate_text = baidu_trans(sentence, fromlang='auto', tolang=language_list[i])
                time.sleep(0.4)
                translate_text = baidu_trans(translate_text, fromlang='auto', tolang='en')
                print('Generated Sentence -', str(language_list[i]), ': ', translate_text)
                sentences_augmented_2.append([translate_text, rating])
                print('--------------------------------------------------------')

        if cur_ind == last_ind:
            break
    except:
        sentence_to_augment_2 = sentence_to_augment_2.loc[cur_ind:, ]
        continue

pd.DataFrame(sentences_augmented_2, columns=['reviewText', 'overall']).to_csv('sentence_augmented_2_4439.csv')

# Augment 3 star review
sentences_augmented_3 = list()
cur_ind = list(sentence_to_augment_3.index)[0]
last_ind = list(sentence_to_augment_3.index)[-1]
while True:
    try:
        for ind in sentence_to_augment_3.index:
            cur_ind = ind
            rating = sentence_to_augment_3.loc[ind, 'overall']
            repeat = repetition[rating]
            sentence = sentence_to_augment_3.loc[ind, 'reviewText']
            print('Original Sentence: ', sentence)
            for i in range(repeat):
                time.sleep(0.5)  # 两次调用API间需要设定响应时间, 否则会报错
                translate_text = baidu_trans(sentence, fromlang='auto', tolang=language_list[i])
                time.sleep(0.5)
                translate_text = baidu_trans(translate_text, fromlang='auto', tolang='en')
                print('Generated Sentence -', str(language_list[i]), ': ', translate_text)
                sentences_augmented_3.append([translate_text, rating])
                print('--------------------------------------------------------')

        if cur_ind == last_ind:
            break
    except:
        sentence_to_augment_3 = sentence_to_augment_3.loc[cur_ind:, ]
        continue

pd.DataFrame(sentences_augmented_3, columns=['reviewText', 'overall']).to_csv('sentence_augmented_3.csv')

