from os import path
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import cv2
import mysql.connector
import os
import requests
import numpy as np
from time import strftime
from datetime import datetime
from tkinter import messagebox
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Face_recognition:
    def __init__(self,root):
        print('New')
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white", fg="BLACK")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\FACE1.png")
        img_top = img_top.resize((1530,790),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top )
        f_lbl.place(x=0, y=55, width=1530, height =790)

        b1_1 = Button(f_lbl, text="FACE RECOGNITION",command=self.face_recog, cursor="hand2", font=("times new roman", 25, "bold"), bg="RED", fg="white")
        b1_1.place(x=240, y=350, width=350, height =50)
    #******************Attendence*******************2
    #def mark_attendence(self,i,g,n,d):
    def mark_attendence(self,i,g,n,d):
        with open("sneha.csv","r+",newline='\n') as f:
            name_list=[]
            mydataList = f.readlines()
            for line in mydataList:
                entry= line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (g not in name_list) and (n not in name_list) and (d not in name_list)): 
            #if((g not in name_list) and (n not in name_list) and (d not in name_list)): 
                now = datetime.now()
                #d1=now.strftime("%d/%m/%Y")
                #dtString= now.strftime("%H:%M:%S")
                #f.writelines(f"\n{n},{d},{g},Available,{i}")
                f.writelines(f"\n{n},{d},{g},Available,{i}")

    #****************FACE RECOGNITION**********************
    
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)
            flag=False
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                #confidence1=int((100*(1-predict/300)))
                #confidence = "  {0}%".format(round(100 - predict))
                confidence = int(round(100 - predict))
                #print(confidence)
                print(confidence)
                conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='face_recognizer')
                my_cursor = conn.cursor()

                # my_cursor.execute("Select Name from student where Id="+str(id))
                # n=my_cursor.fetchone()
                # n="".join(str(n))

                # my_cursor.execute("Select Gender from student where Id="+str(id))
                # g=my_cursor.fetchone()
                # g="".join(str(g))

                # my_cursor.execute("Select Description from student where Id="+str(id))
                # d=my_cursor.fetchone()
                # d="".join(str(d))

                # my_cursor.execute("Select Id from student where Id="+str(id))
                # i=my_cursor.fetchone()
                # i="".join(str(i))
                
                count=1
                if(int(confidence)>50):
                    flag = True
                    
                    #root=Tk()
                    
                    #root.mainloop()
                    my_cursor.execute("Select Name from student where Id="+str(id))
                    n=my_cursor.fetchone()
                    n="".join(str(n))

                    my_cursor.execute("Select Gender from student where Id="+str(id))
                    g=my_cursor.fetchone()
                    g="".join(str(g))

                    my_cursor.execute("Select Description from student where Id="+str(id))
                    d=my_cursor.fetchone()
                    d="".join(str(d))

                    my_cursor.execute("Select Id from student where Id="+str(id))
                    i=my_cursor.fetchone()
                    i="".join(str(i))
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Gender:{g}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Description:{d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),3)
                    #tkinter.messagebox.showinfo('Popup Window(Title)','This is a pop up window')
                    

                    self.mark_attendence(i,g,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Not Criminal",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]
            return coord,flag
        def recognize(img,clf,faceCascade):
            coord,flag = draw_boundary(img,faceCascade,1.2,10,(255,25,255),"Face",clf)
            
            return img,flag
            
        faceCascade = cv2.CascadeClassifier(r"C:\Users\smita\OneDrive\Desktop\Project\Project\haarcascade_frontalface_default.xml")
        print("Yr")
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\smita\OneDrive\Desktop\Project\Project\classifier.xml")

        video_cap =cv2.VideoCapture(0)

        while True:
            ret,img =video_cap.read()
            img,flag=recognize(img,clf,faceCascade)
            print(flag)
            cv2.imshow("Welcome to face recognition",img)
            if flag == True:
                #print("1")
                #root=Tk()
                #import urllib.parse
                #s = urllib.parse.quote('https://www.google.com/maps/place/Prestige+Institute+of+Engineering+Management+%26+Research/@22.7603558,75.8832935,17z/data=!3m1!4b1!4m5!3m4!1s0x396302a52ba04921:0x7fad922991d66926!8m2!3d22.7603558!4d75.8854822')
                #import os
                #os.system('curl -X fetch "https://www.google.com/maps/place/Prestige+Institute+of+Engineering+Management+%26+Research/@22.7603558,75.8832935,17z/data=!3m1!4b1!4m5!3m4!1s0x396302a52ba04921:0x7fad922991d66926!8m2!3d22.7603558!4d75.8854822" ')
                #print(var)
                #url = requests.get("https://www.google.com/maps/place/Prestige+Institute+of+Engineering+Management+%26+Research/@22.7603558,75.8832935,17z/data=!3m1!4b1!4m5!3m4!1s0x396302a52ba04921:0x7fad922991d66926!8m2!3d22.7603558!4d75.8854822")
                #htmltext = url
                #print(url)
                #os.system( 'xdg-open "https://www.google.com/maps/place/Prestige+Institute+of+Engineering+Management+%26+Research/@22.7603558,75.8832935,17z/data=!3m1!4b1!4m5!3m4!1s0x396302a52ba04921:0x7fad922991d66926!8m2!3d22.7603558!4d75.8854822" ')
                
                sender_address = 'criminalidentification123@gmail.com'
                sender_pass = 'prestige@123'
                mail_content = 'The Criminal is detected.'
                receiver_address = 'meetschouhan18@gmail.com'
                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address
                message['Subject'] = 'Criminal detected'   #The subject line
                message.attach(MIMEText(mail_content, 'plain'))
                session1 = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session1.starttls() #enable security
                session1.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session1.sendmail(sender_address, receiver_address, text)
                session1.quit()
                k = messagebox.showinfo('Alert','Criminal Detected')
                address = 'Prestige+Institute+of+Engineering+Management+%26+Research/@22.7603558,75.8832935,17z/data=!3m1!4b1!4m5!3m4!1s0x396302a52ba04921:0x7fad922991d66926!8m2!3d22.7603558!4d75.8854822'
                webbrowser.open('https://www.google.com/maps/place/' + address)
                k.destroy()
              
                
                if cv2.waitKey(1)==13:
                    break
                        
            if cv2.waitKey(1)==13:
                break
        
       

        #video_cap.release()
        #cv2.destroyAllWindows()
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    obj.face_recog()
    root.mainloop()