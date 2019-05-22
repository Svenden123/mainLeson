import requests
import xml.etree.ElementTree as ET


urlJson = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/' \
          '3.1.formats.json.xml/newsafr.json'
response = requests.get(urlJson)
dataJson = response.json()['rss']['channel']['items']

urlXML = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/' \
         'master/3.1.formats.json.xml/newsafr.xml'
response = requests.get(urlXML)

tree = ET.fromstring(response.text)

dataXML = list()
for i, item in enumerate(tree[0].findall('item')):
    dataXML.append([
            item[0].text, item[2].text
        ])

isJson = input("Сортировать JSON ? (1-да, 2-нет)")

fullText = ''
for e, item in enumerate(dataJson if isJson == '1' else dataXML):
    if isJson == '1':
        fullText += item['title'] + ' '
        fullText += item['description']
    else:
        fullText += item[0] + ' '
        fullText += item[1]


freq = dict()
for i in fullText.split():
    f = freq.get(i, 0)
    freq[i] = f + 1

freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
print(freq)
