from concurrent import futures
from tkinter import *

thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
class GUI(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        root.title("GUI Sample")
        color="#ffffff"
        root.configure(bg=color)
        e1=StringVar()
        e2=StringVar()
        e3=StringVar()
        c1=IntVar()
        c2=IntVar()
        c3=IntVar()
        Label(root,text="Entry#1",background=color).grid(column=1,row=1)
        Entry(root,textvariable=e1,background=color).grid(column=2,row=1)
        Label(root,text="Entry#2",background=color).grid(column=1,row=2)
        Entry(root,textvariable=e2,background=color).grid(column=2,row=2)
        Label(root,text="Entry#3",background=color).grid(column=1,row=3)
        Entry(root,textvariable=e3,background=color).grid(column=2,row=3)
        Checkbutton(root,text="CheckButton#1",variable=c1,background=color).grid(column=3,row=1)
        Checkbutton(root,text="CheckButton#2",variable=c2,background=color).grid(column=3,row=2)
        Checkbutton(root,text="CheckButton#3",variable=c3,background=color).grid(column=3,row=3)
        T=Text(root, height=15, width=70)
        T.grid(column=3,row=7)
        b1=Button(root,command= lambda: self.login0(T,e1,e2,e3,c1,c2,c3,b1,),text="RUN",background=color)
        b1.grid(column=1,row=7)
    def login0(self,T,e1,e2,e3,c1,c2,c3,b1):
        thread_pool_executor.submit(self.main,T,e1,e2,e3,c1,c2,c3,b1)
    def main(self,T,e1,e2,e3,c1,c2,c3,b1):
        #Your Instructions Here
        pass 


if __name__ == '__main__':

    root = Tk()
    main_frame = GUI()
    root.mainloop()
