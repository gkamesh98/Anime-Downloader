import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import threading
import Downloader

def startdownload(root):
    if len(e1.get()) == 0:
        tkinter.messagebox.showinfo(title="details", message="please mention name of the anime")
    if len(e2.get()) == 0:
        tkinter.messagebox.showinfo(title="details", message="please mention episode details")
    if len(e3.get()) == 0:
        tkinter.messagebox.showinfo(title="details", message="please mention download loaction")
    name = e1.get()
    name = name.replace(" ","-")

    episode_list = []
    episode = e2.get()
    if episode.find(',') != -1:
        episode_list = episode.split(",")
    elif episode.find('-') != -1:
        e = episode.split("-")
        episode_list  = list(range(int(e[0]),int(e[1])))
        episode_list.append(int(e[1]))
    else:
        episode_list.append(int(episode))
    #print(name)
    #print(episode_list)
    location = e3.get()
    location = location.replace('\\','/')
    #print(location)
    #t = threading.Thread(target=Downloader.download,args=(name,episode_list,location))
    #t.start()
    for ep in episode_list:
        t= threading.Thread(target = Downloader.begindownload,args = (root,name,ep,location))
        t.start()

    root.mainloop()

def finddir():
    newdir = tkinter.filedialog.askdirectory()
    e3.delete(first = 0,last = len(e3.get()))
    e3.insert(tkinter.END,newdir)

root = tkinter.Tk()
root.geometry("800x500+200+100")
root.title("Anime downloader")
root.configure(background = "#000000")

require = Frame(root)
require.configure(background = "#000000")

lbl = Label(require,text = "Name of anime",font = ("Verdana", 18),bg = "#000000",fg = "#FFFFFF",bd = 30,)
lbl.grid(row = 0 ,column = 0)

ans1 = StringVar()
e1 = Entry(require,font = ("Verdana", 16),textvariable = ans1,)
e1.grid(row = 0,column = 1)

lb2 = Label(require,text = "episodes",font = ("Verdana", 18),bg = "#000000",fg = "#FFFFFF",bd = 30)
lb2.grid(row=1,column =0)

ans2 = StringVar()
e2 = Entry(require,font = ("Verdana", 16),textvariable = ans2,)
e2.grid(row =1, column = 1)

lb4 = Label(require,text = "Download location",font = ("Verdana", 18),bg = "#000000",fg = "#FFFFFF",bd = 30)
lb4.grid(row=2,column =0)

ans3 = StringVar()
e3 = Entry(require,font = ("Verdana", 16),textvariable = ans3,)
e3.grid(row =2, column = 1)
e3.insert(tkinter.END,"C:/")

bro = Button(require,text = "Browse",font = ("Comic sans ms", 11),width = 16,bg = "#000000",fg = "#ffffff",relief = GROOVE,command = finddir,)
bro.grid(row = 2,column = 2)


require.pack(pady = 20)

downloader = tkinter.Tk()
downloader.geometry("800x600+200+100")
downloader.title("Anime downloader Status")
downloader.configure(background = "#FFFFFF")

headers = Frame(downloader)
headers.configure(background = "#FFFFFF")
lb1 = Label(headers,text = "name",bg = "#FFFAFA",fg="#000000",font= ("device",10),)
lb1.grid(row = 0,column= 0,ipadx=100)
lb2 = Label(headers,text = "actual",bg = "#FFFAFA",fg="#8B0000",font= ("device",10),)
lb2.grid(row = 0,column= 1,ipadx=100)
lb3 = Label(headers,text = "remaing",bg = "#FFFAFA",fg="#008B00",font= ("device",10),)
lb3.grid(row = 0,column= 2,ipadx=100)
headers.pack()

btn = Button(root,text = "submit",font = ("Comic sans ms", 16),width = 16,bg = "#4c4b4b",fg = "#6ab04c",relief = GROOVE,command = lambda: startdownload(downloader))
btn.pack(pady = 20)



lb3 = Text(root,font = ("Verdana", 10),bg = "#000000",fg = "red",bd=0,)
lb3.pack()

text = "note:for download of episode mention \'-\' for sequence of episodes, for specific episodes \',\' ,for single episode mention just episode number. And for mentioning anime name properly and completely by mentioning season by giving space."
lb3.insert(tkinter.END,text)

downloader.mainloop()
root.mainloop()
