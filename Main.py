from googlesearch import search
import numpy as np
from bs4 import BeautifulSoup
import requests
query = "nlp"
links = []
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    links = np.append(links, j)
res = requests.get(links[0])
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
string = []
for i in soup.find_all('p'):
    # print(i.text, i.next_sibling)
    string = np.append(string, i.text)
punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
newString = ""
for x in string:
    if x not in punctuation:
        newString = newString + x
print(newString)

