import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
def page(offset):
    url = "http://maoyan.com/board/4?offset="+offset
    response = requests.get(url,headers=headers)
    html = response.text
    infos = re.findall(r'<dd>(.*?)</dd>',html,re.S)
    file = open("猫眼电影.txt","a+",encoding="utf-8")
    for info in infos:
        xuhao = re.findall(r'<i class="board-index board-index-\d+">(.*?)</i>',info,re.S)[0].strip()
        img = re.findall(r'<img data-src="(.*?)".*?/>',info,re.S)[0].strip()
        name = re.findall(r'<p class="name"><a.*?">(.*?)</a>',info,re.S)[0].strip()
        star = re.findall(r'<p class="star">(.*?)</p>',info,re.S)[0].strip()
        date = re.findall(r'<p class="releasetime">(.*?)</p>',info,re.S)[0].strip()
        score1 = re.findall(r'<i class="integer">(.*?)</i>',info,re.S)[0].strip()
        score2 = re.findall(r'<i class="fraction">(.*?)</i>',info,re.S)[0].strip()
        score = score1+score2
        print(xuhao,img,name,star,date,score)
        di = {
            "xuhao":xuhao,
            "img":img,
            "movieName":name,
            "star":star[3:],
            "date":date[5:],
            "score":score
        }
        print(di)
        # file.write(xuhao+"\t"+img+"\t"+name+"\t"+star+"\t"+date+"\t"+score+"\n\n")
        file.write(str(di)+"\n\n")
    file.close()

for i in range(10):
    page(offset=str(i*10))





