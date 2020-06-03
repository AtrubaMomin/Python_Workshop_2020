program on scraping
from bs4 import BeautifulSoup
import requests
import pandas as pd
url='https://boston.craigslist.org/search/sof'
npo_job={}
job_no=0
while(True):
    response=requests.get(url).text
    soup=BeautifulSoup(response,'lxml')
    jobs=soup.find_all('p',{"class":"result-info"})

    for job in jobs:
        title=job.find('a',{"class":"result-title"}).text
        date=job.find('time',{"class":"result-date"}).text
        link=job.a.attrs['href']
        link_url=f'{link}'
        job_no+=1
        npo_job[job_no]=[title,date,link_url]
        print("Job Title:",title,"\nDate:",date,"\nLink:",link_url,"\n------")
        
    url_tag=soup.find('a',{'title':'next page'})
    if url_tag.get('href'):
        url='https://boston.craigslist.org' + url_tag.get('href')
        print ('url')

    else :
        break

print("Total Jobs :",job_no)

npo_job_df=pd.DataFrame.from_dict(npo_job, orient='index', columns=['Job Title','Date','Link'])
npo_job_df.head()
npo_job_df.to_csv('npo_job.csv')
