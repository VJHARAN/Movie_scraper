import requests as req
from bs4 import BeautifulSoup
    
url="https://www.1tamilmv.fi/"
page=req.get(url)

soup=BeautifulSoup(page.content,'html.parser')

movies_container=soup.find(id='elCmsPageWrap')

movies_texts=movies_container.find_all('span', string=lambda text: 'rips' not in text.lower() and 'malayalam' in text.lower() )

for m in movies_texts:
    print(m.text)
    print("\n")
