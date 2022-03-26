from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(START_URL)
soup=bs(page.text,'html.parser')
startable=soup.find('table')

temp_list=[]
tablerows=startable.find_all('tr')
for tr in tablerows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)

starnames=[]
stardistance=[]
starmass=[]
starradius=[]
lump=[]

l=len(temp_list)
print(l)
for i in range(1,98):
    starnames.append(temp_list[i][1])
    stardistance.append(temp_list[i][3])
    starmass.append(temp_list[i][5])
    starradius.append(temp_list[i][6])
    lump.append(temp_list[i][7])
df=pd.DataFrame(list(zip(starnames,stardistance,starmass,starradius,lump)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
df.to_csv('brightStars.csv')
