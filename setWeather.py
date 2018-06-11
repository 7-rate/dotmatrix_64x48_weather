import requests
from xml.etree import ElementTree
import mojimoji
import time
import json
import datetime

# 自分の環境に合わせる
MAZO_IP = '192.168.11.7'
WEATHER_URL = 'https://rss-weather.yahoo.co.jp/rss/days/5610.xml'

"""
example:

【 9日（土） 加賀（金沢） 】 曇り - 25℃/20℃ - Yahoo!天気・災害
↓
・<今日>くもり　最高気温：25度　最低気温：20度
or
・<明日>くもり　最高気温：25度　最低気温：20度

caution:
曇は表示できないため、「くもり」に変換する
"""
def conversionToXmlStr(isToday, xmlStr):
    xmlStr = xmlStr.replace("曇り", "くもり")
    xmlStr = xmlStr.replace("曇", "くもり")
    xmlStr = xmlStr.replace("℃", "度")
    
    xmlStrs = xmlStr.split(' ')

    retStr = ""
    if isToday:
        retStr += '<今日>'
    else:
        retStr += '<明日>'
    temps = xmlStrs[6].split('/')
    retStr += xmlStrs[4]
    retStr += '　最高気温：'+temps[0]
    retStr += '　最低気温：'+temps[1]
    retStr += '　'

    return retStr

MAZO_URL = 'http://admin:admin@{}/settings/ui_marquee'.format(MAZO_IP)

while True:
    responseXml = requests.get(WEATHER_URL)

    tree = ElementTree.fromstring(responseXml.text)

    now = datetime.datetime.now()
    if now.hour >= 0 and now.hour < 18:
        weatherInfo = tree[0][6][0].text
        weatherStr = conversionToXmlStr(True, weatherInfo)
    else:
        weatherInfo = tree[0][7][0].text
        weatherStr = conversionToXmlStr(False, weatherInfo)

    print(weatherStr)
    payload = {'ui_marquee': weatherStr}
    print(MAZO_URL)
    requests.post(MAZO_URL, data=payload)

    time.sleep(1800)