from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

data = pd.read_csv('Sgcarmart_Webscraping_Data.csv')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

car_names=data.Name.tolist()

urls=data.Link.tolist()

limits = data.Limit.tolist()

for i in range(len(car_names)):
    car_count=0
    car_name=car_names[i]
    url=urls[i]
    limit=limits[i]
    #pulling html from website
    source = requests.get(url).text
    #parsing the website for depre
    soup = BeautifulSoup(source, features="html.parser")
    article=soup.find('div',{"id":"contentblank"})
    depre=article.findAll(style="width:101px;")
    name=article.findAll(style="width:186px;padding-left:4px;")
    
    #looping through each depre to check for matches
    z = 0
    for d in depre:
        n = name[z].a.text
        
        p = d.text.strip()
        x = re.sub(r"[^0-9]","",p)
        x = int(x)
        z+=1
        
        if (x <= limit):
            print(n)
            if (n.endswith("(OPC)")!=True):
                car_count+=1

    if car_count > 0:
        print(car_name + ": " + str(car_count))
        
input("Press enter to exit")
