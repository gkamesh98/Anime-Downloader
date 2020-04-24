import urllib.request
from bs4 import BeautifulSoup
import requests
import threading
import tkinter
import os
from tkinter import *

def chunkdownload(store,name,downurl,sizeb):
    printname = name.split('/')
    printname = printname[len(printname)-1]
    printname = printname.replace('.mp4','')
    lb = Label(store,text = printname ,font= ("device",10),bg = "#FFFFFF",fg = "#696969",)
    lb.grid(row = 0 ,column = 0,ipadx=100)
    lb2=Label(store,text = str(round(sizeb/(1024*1024),2)),font= ("device",10),bg = "#FFFFFF",fg = "#800000",)
    lb2.grid(row = 0 ,column = 1,ipadx=100)
    fsize = 0

    try:
        fsize = os.path.getsize(name)
    except Exception:
        pass
    sizeb = sizeb - fsize
    lb3=Label(store,text = str(round(sizeb/(1024*1024),2)),font= ("device",10),bg = "#FFFFFF",fg = "#39FF14",)
    lb3.grid(row = 0 ,column = 2,ipadx=100)


    head = {'User-Agent': 'Mozilla/5.0','Range': 'bytes=%d-' %fsize}

    try:
        f=requests.get(downurl,headers=head,stream=True)
    except Exception:
        lb2.configure(text = "Failed")
        lb3.configure(text = "Failed")

    cs = 64*1024

    cs = min(cs,sizeb)

    with open(name,"ab") as l:
        for chunk in f.iter_content(chunk_size=cs):
            l.write(chunk)
            sizeb = sizeb - cs
            cs = min(cs,sizeb)
            #print(name+" "+str(sizeb))
            lb3.configure(text = str(round(sizeb/(1024*1024),2)))
    try:
        f.close()
    except Exception:
        pass


def begindownload(root, aname , ep , loc):
    store = Frame(root)
    store.configure(background="#000000")
    url = "https://www.animefreak.tv/watch/"+aname+"/episode/episode-"+str(ep)
    req = urllib.request.Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    try:
        h = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(h,'lxml')
    except Exception:
        pass
    finally:
        try:
            h.close()
        except Exception:
            pass
    b = soup.body.find('div',class_='vmn-video').find_all('script')
    s = str(b[1]).split('\"')
    downurl=s[1].replace(" ","%20")
    n = url.split('/')
    name =loc +"/" + n[4]+" "+n[6]+".mp4"
    sizeb=0
    try :
        k = urllib.request.urlopen(downurl).info()
        sizeb = int(k['Content-Length'])
        size = int(k['Content-Length'])/(1024*1024)
    except Exception:
        pass
    finally:
        try:
            k.close()
        except Exception:
            pass
    threading.Thread(target=chunkdownload,args=(store,name,downurl,sizeb)).start()
    store.pack()
