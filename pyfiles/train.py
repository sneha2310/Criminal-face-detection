from os import path
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="TRAIN DATASET", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\uptrain.png")
        img_top = img_top.resize((1530,790),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top )
        f_lbl.place(x=0, y=55, width=1530, height =790)


        b1_1 = Button(self.root, text="Training",command=self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), bg="Red", fg="white")
        b1_1.place(x=620, y=400, width=300, height =50)

    def train_classifier(self):
        data_dir= ("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]
        for image in path:
            img = Image.open(image).convert('L')  #Gray Scale
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            print(id)
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #+++++++++++++++++++++++++++++++++++++++Train classifier+++++++++++++++++++++++++++++++
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!!")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()