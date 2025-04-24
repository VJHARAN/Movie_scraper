import requests as req
from bs4 import BeautifulSoup
import re

url="https://www.1tamilmv.fi/"
page=req.get(url)

user_input=input("Input movie name or year to search: ")
soup=BeautifulSoup(page.content,'html.parser')

movies_container=soup.find(id='elCmsPageWrap')

movies_text=movies_container.find_all('span',string=lambda text: user_input in text.lower())
parent_list=[span_element.parent for span_element in movies_text]
for item in parent_list:
    title=item.find('span')
    print(title.text)
    links=item.find_all('a',href=lambda text : '1tamilmv' in text.lower())
    for link in links:
        link_url = link["href"]
        print(f"Open here: {link_url}"+"\n"*2)
  
 



