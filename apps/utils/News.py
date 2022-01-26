import requests
import pandas as pd
from bs4 import BeautifulSoup

def requestPage(URL):
    req = requests.get(url=URL)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "html5lib")
        return soup
    else:
        raise Exception("Failed to load page")

def get_all_news():
    newsList = []
    URL = "https://katadata.co.id/"
    soup = requestPage(URL)
    article = soup.select('article')
    for x in range(len(article)):
        title = article[x].select_one('h2 a')
        link = article[x].select_one('a')
        img_src = article[x].select_one('img')
        if title is not None:
            newsList.append(
                {
                    "title": title.text.strip(),
                    "link": link['href'],
                    "img_src": img_src['src'],
                    "author": "",
                    "publisheddate": "",
                    "content": ""
                }
            )
        
        
    
    return newsList

def get_news_detail():
    all_links = get_all_news()
    fullPar = ""
    listPar = []
    for x in range(len(all_links)):
        detailNews = requestPage(all_links[x]['link'])
        content = detailNews.select('article div.detail-body.mb-4 p')
        author = detailNews.select('div.detail-author-name')
        publisheddate = detailNews.select('div.detail-date')
        all_links[x]['author'] = author[0].text.strip("Oleh \n")
        all_links[x]['publisheddate'] = publisheddate[0].text
        
        fullContent = detailNews.find_all('p')
        for y in range(0, len(fullContent)):
            parag = fullContent[y].text.replace("Dapatkan informasi terkini dan terpercaya seputar ekonomi, bisnis, data, politik, dan lain-lain, langsung lewat email Anda.", "")
            listPar.append(parag)
            fullPar = " ".join(listPar)
            all_links[x]['content'] = fullPar
        fullPar = ""
        listPar = []
            
    return all_links

get_news_detail()