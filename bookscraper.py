import requests
from bs4 import BeautifulSoup
URL="https://books.toscrape.com/"
req=requests.get(URL)
source_code=req.content
soup=BeautifulSoup(source_code,'lxml')
print(soup)
article=soup.find_all('article')
for  i in article:
    h3=i.find('h3')
    name=(h3.find('a').text)
    price=i.find('div',class_="product_price")
    price=price.find('p')
    price=price.text[1:]
    price=float(price)
    if price<50:
        with open('books.txt','a')as file:
            file.write(name+":"+str(price)+ "\n")
            
