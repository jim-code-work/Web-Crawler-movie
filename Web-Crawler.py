# 抓取 ptt 電影版網頁原始碼 (HTML)

import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

#  建立一個 Request 物件， 附加 Reuest Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
})

with req.urlopen(request) as reponse:                              
    data=reponse.read().decode("utf-8")
    
# 解析網頁原始碼，取得每篇文章標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")          # 尋找所有 class='title' 的 div 標籤

for title in titles:
    if title.a != None:                             # 如果標題包含 a 標籤, 印出來
        print(title.a.string)
        