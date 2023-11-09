# keyword based recursive website checking
import requests 
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_url=set()
def get_page(url, keyword="nodejs"):
    try:
        response=requests.get(url)
    except:
        print("request failed" + url)
        return
    if response.status_code == 200:
        soup=BeautifulSoup(response.content, 'html.parser')
       #print((soup))
        tag=soup.find_all("a")
      # print((tag))
        urls=[]
        for t in tag:
            href=t.get("href")
            if href is not None:
                urls.append(href)
        #print(urls)
        for url2 in urls:
            if url2 not in visited_url:
                visited_url.add(url2)
                url_join=urljoin(url,url2)
                if keyword in url_join:
                    print(url_join)
                    get_page(url_join, keyword)
                else:
                    pass
get_page(input("give url"))
