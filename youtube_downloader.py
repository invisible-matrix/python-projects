from pytube import YouTube

from tkinter import*

root=Tk()
root.geometry("300x400")
root.title("youtube video downloader")

def youtube ():
    a=var.get()
    ytv=YouTube(a).streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first()
    ytv.download(r"E:\E-books")
    print("entry box :",a)


l1 = Label(root,text= "paste video link",fg="red",font=("bold",20))
l1.place(x=70,y=20)

var = StringVar()
e1 = Entry(root,textvariable=var,width=60)
e1.place(x=80,y=80)

b1 = Button(root,text="download",command=youtube,bg="green",width=20,fg="white")
b1.place(x=80,y=120)

root.mainloop()


# this was done in spyder IDE , if some one is taking this project save it in .py format