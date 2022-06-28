from bs4 import BeautifulSoup
import requests

url = ''

result = requests.get(url)
doc = BeautifulSoup(result.text, 'lxml')

print(doc.prettify())
# Beautiful way to print neated nested tags

div = doc.find_all()
# 'tag/tags', class_= ,'class', id='id'

div = div[0]
# list

print(div.text())
# print content inside tag