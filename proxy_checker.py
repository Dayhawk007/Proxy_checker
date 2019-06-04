import requests
from bs4 import  BeautifulSoup
from threading import  Thread
from termcolor import colored
tit=""
valid=open("valid.txt","w")
prox=open("proxies.txt","r")
def proxy_():
    with requests.session() as r:
        for proxy in prox.readlines():
            try:
                res=r.get(r"https://google.com",proxies={"http":"http://"+proxy[:-1],"https":"https://"+proxy[:-1]})
                sop=BeautifulSoup(res.content,features="html.parser")
                for k in sop.find_all("title"):
                    tit=k.string
                    if(tit=="Google"):
                        valid.write(tit)
                        print(proxy[:-1]+"-valid")
                        valid.flush()
            except:
                print(proxy[:-1]+" -invalid")

x=Thread(target=proxy_)
x.start()