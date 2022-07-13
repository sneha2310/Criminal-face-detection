from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector


class developer1:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #####

        title_lbl = Label(self.root,text="DEVELOPER", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\developer.png")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top )
        f_lbl.place(x=0, y=55, width=1530, height =720)
        #frame

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\logo.png")
        img_top1 = img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top1 )
        f_lbl.place(x=1300, y=60, width=200, height =200)

        #developer info
        logo_frame = Label( main_frame,text="INFORMATION:",bd=2,bg="white", font=('times new roman',15,"bold"))
        logo_frame.place(x=0,y=10)

        logo_frame = Label( main_frame,text="Developer:",bd=2,bg="white",relief=RIDGE, font=('times new roman',12,"bold"))
        logo_frame.place(x=0,y=60)

        logo_frame = Label( main_frame,text="-Meet Singh Chouhan",bd=2,bg="white", font=('times new roman',12,"bold"))
        logo_frame.place(x=15,y=85)

        logo_frame = Label( main_frame,text="-Sagar Sankare",bd=2,bg="white", font=('times new roman',12,"bold"))
        logo_frame.place(x=15,y=110)

        logo_frame = Label( main_frame,text="-Sneha Vishwakarma",bd=2,bg="white", font=('times new roman',12,"bold"))
        logo_frame.place(x=15,y=135)

        logo_frame = Label( main_frame,text="-Swapnil Sanap",bd=2,bg="white", font=('times new roman',12,"bold"))
        logo_frame.place(x=15,y=160)

       
       
if __name__ == "__main__":
    root = Tk()
    obj = developer1(root)
    root.mainloop()