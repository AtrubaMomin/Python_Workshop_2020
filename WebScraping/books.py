from bs4 import BeautifulSoup
import requests
import pandas as pd
npo_book={}
book_no=0
for i in range(1,51):
    url=f'http://books.toscrape.com/catalogue/page-{i}.html'
    source=requests.get(url).text
    soup=BeautifulSoup(source,'lxml')
    books=soup.find_all('article',class_="product_pod")
    for book in books:
        title=book.h3.a.attrs['title']
        print(title)
        price=book.find('div',class_="product_price").p
        print(price.text)
        img_source=book.img.attrs['src']
        img_url=f'http://books.toscrape.com/{img_source}'
        print(img_url)
        book_no+=1
        npo_book[book_no]=[title,price,img_url]
        print("Title : ",title,"\nPrice : ",price,"\nImage Link : ",img_url)
print("\nTotal Books : ",book_no)
npo_book_df=pd.DataFrame.from_dict(npo_book, orient='index', columns=['Book Title','Price','Image Link'])
npo_book_df.head()
npo_book_df.to_csv('npo_book.csv')

