from typing import List, Any

from bs4 import BeautifulSoup as BS
import pandas as pd
import time
import requests
import urllib.request

pd.set_option('display.width', 1000)

df = pd.read_csv("URL4.csv")
URL_List = df['URL']
# URRL is the list
User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0"
Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
Accept_Encoding = "gzip, deflate, br"
Accept_Language = "en-US,en;q=0.5"

header = {"User-Agent":User_Agent,"Accept":Accept}
#Beatufulk Soup type stuff


cells = []

Ranking = [1,2,3,4,5,6,7,8,9,10]

RANKs = []
RANK2 = []
RANK3 = []
DISTRICTs = []
SCOREs = []
LEANs = []
# variables

HOMEs =[]
# District

# def adding_ranking(kep):


for URL in URL_List:
    req = urllib.request.Request(URL, headers=header)
    html = urllib.request.urlopen(req)
    soup = BS(html, 'html.parser')
    tables = soup.find_all("div",class_="cantor-list")

    RANK2.append(Ranking)

    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')


            if len(cells) > 0:
                RANK = cells[0]
                RANKs.append(RANK.text.strip())

                DISTRICT = cells[1]
                DISTRICTs.append(DISTRICT.text.strip())

                SCORE = cells[2]
                SCOREs.append(SCORE.text.strip())

                LEAN = cells[3]
                LEANs.append(LEAN.text.strip())




## df1 = pd.DataFrame(RANKs, index = FALSE, columns=['Rank'])
## df1['District'] = DISTRICTs
## df1['Similarity Scores'] = SCOREs
## df1['Polling Ave'] = LEANs
## df2 = pd.DataFrame(cells, columns=['fuck','me','please','thanks'])

df3 = pd.DataFrame({'Rank':RANKs,'Similar Score':SCOREs,'Lean':LEANs,'Similar District':DISTRICTs})
print(cells[0])
print(cells[1])
print(RANK2)

def write_vars_to_file(_f, **vars):
    for (name, val) in vars.items():
        _f.write("%s = %s\n" % (soup, repr(val)))

df3.to_csv(r'Sup52341s.csv')

## print(df1)
# print(SCOREs)
## print(df3)
