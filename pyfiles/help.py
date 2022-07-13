from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector


class help1:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="Help Desk", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\help.png")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top )
        f_lbl.place(x=0, y=55, width=1530, height =720)

        #developer info
        dev_frame = Label(f_lbl,text="For any kind of help, mail it on the following mails:",bd=2,bg="white", font=('times new roman',15,"bold"))
        dev_frame.place(x=1000,y=150)

        dev_frame = Label(f_lbl,text="EMAIL: meetschouhan18@gmail.com",bd=2,bg="white", font=('times new roman',15,"bold"))
        dev_frame.place(x=1000,y=200)

        dev_frame = Label(f_lbl,text="sagarsankere@gmail.com",bd=2,bg="white", font=('times new roman',15,"bold"))
        dev_frame.place(x=1070,y=240)

        dev_frame = Label(f_lbl,text="sneha2310v@gmail.com",bd=2,bg="white", font=('times new roman',15,"bold"))
        dev_frame.place(x=1070,y=280)

        dev_frame = Label(f_lbl,text="swapnilsanap@gmail.com",bd=2,bg="white", font=('times new roman',15,"bold"))
        dev_frame.place(x=1070,y=320)
        

if __name__ == "__main__":
    root = Tk()
    obj = help1(root)
    root.mainloop()