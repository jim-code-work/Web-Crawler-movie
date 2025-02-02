# 抓取 ptt 八卦版網頁原始碼 (HTML)

import urllib.request as req

def getdata(
    url):
    #  建立一個 Request 物件， 附加 Reuest Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as reponse:                              
        data=reponse.read().decode("utf-8")
        
    # 解析網頁原始碼，取得每篇文章標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")          # 使用 BeautifulSoup 協助我們解析 HTML 格式文件
    titles=root.find_all("div", class_="title")          # 尋找所有 class='title' 的 div 標籤

    for title in titles:
        if title.a != None:                             # 如果標題包含 a 標籤, 印出來
            print(title.a.string)
            
    # 抓取上一頁的連結      
    nextLink=root.find("a", string="‹ 上頁")            # 找到內文是 (< 上頁) (string資料) 的 a 標籤
    return nextLink["href"]  
    
# 主程序: 抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"

count=0
while count<3:
    pageURL="https://www.ptt.cc"+getdata(pageURL)
    count+=1
print(pageURL)