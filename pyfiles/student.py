from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ************variables**************

        self.var_name = StringVar()
        self.var_description = StringVar()
        self.var_gender = StringVar()
        self.var_Id = StringVar()

        #first image
        img = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\side.png")
        img = img.resize((500,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height =130)

        #second image
        img1 = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\main.png")
        img1 = img1.resize((500,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height =130)

        #third image
        img2 = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\side.png")
        img2 = img2.resize((550,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height =130)

        #bg image
        img3 = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\6.png")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height =710)

        title_lbl = Label(bg_img,text="Details", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

    
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame

        Left_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text="Details", font=('times new roman',15,"bold"))
        Left_frame.place(x=10,y=10, width=750,height=580)


        #left image
        img_left = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\left1.png")
        img_left = img_left.resize((550,200),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left )
        f_lbl.place(x=5, y=0, width=720, height =250)

        #current course

        current_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text="Detail", font=('times new roman',15,"bold"))
        current_frame.place(x=15,y=260, width=720,height=300)

        #current_personname
        person_name = Label(current_frame,text="Name", font=("times new roman",13,"bold"))
        person_name.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        person_name_block = ttk.Entry(current_frame,textvariable=self.var_name, font=("times new roman",13,"bold"))
        person_name_block.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #current_personid
        person_phone = Label(current_frame,text="Description", font=("times new roman",13,"bold"), bg="white")
        person_phone.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        person_phone_block = ttk.Entry(current_frame,textvariable=self.var_description,font=("times new roman",13,"bold"))
        person_phone_block.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #current_gender
        person_Gender = Label(current_frame,text="Gender", font=("times new roman",13,"bold"), bg="white")
        person_Gender.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        gender_combo = ttk.Combobox(current_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"), state='readonly', width=18)
        gender_combo["values"] = ("Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,padx=6,pady=10,sticky=W)

     
        btn_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=15,y=430,width=720,height=40)  

        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=17, font=("times new roman",13,"bold"),bg="gray",fg="white")     
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman",13,"bold"),bg="gray",fg="white")     
        update_btn.grid(row=0, column=1)

        del_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman",13,"bold"),bg="gray",fg="white")     
        del_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman",13,"bold"),bg="gray",fg="white")     
        reset_btn.grid(row=0, column=3)

        #buttons frame
        btn_frame1=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=190,y=479,width=360,height=40)  

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample", width=36, font=("times new roman",13,"bold"),bg="gray",fg="white")
        take_photo_btn.grid(row=0,column=0)

        #update_photo_btn=Button(btn_frame1,text="Update Photo Sample", width=36, font=("times new roman",13,"bold"),bg="gray",fg="white")
        #update_photo_btn.grid(row=0,column=1)
        #right label frame

        Right_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text="Details", font=('times new roman',15,"bold"))
        Right_frame.place(x=750,y=10, width=720,height=580)

        img_right = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\boo1.png")
        img_right = img_right.resize((550,200),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right )
        f_lbl.place(x=5, y=0, width=720, height =180)
        #+++++++++++++++++table frame++++++++++++++++++
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=200,width=690,height=400) 

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column=("Name","Description","Gender","Id"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Description", text="Description")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Id", text="Id")
        #self.student_table.heading("Radio", text="Radio")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
    
        #*************function declaration****************

    def add_data(self):
        if self.var_gender.get()=='' or self.var_name.get()=='' or self.var_description.get()=='':
            messagebox.showerror('Error', 'All fields are required.', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student(name,description,gender) values (%s,%s,%s)', (
                    self.var_name.get(),
                    self.var_description.get(),
                    self.var_gender.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Data Saved Successfully', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f' Due To:  {str(es)}', parent=self.root)
    
    # ****************fetch data******************

    def fetch_data(self):
        conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='face_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from face_recognizer.student')
        data = my_cursor.fetchall()
        if len(data)!=0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
               self.student_table.insert("", END, values=i)
           conn.commit()
        conn.close()
    
    # *****************get cursor******************s

    def get_cursor(self, event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_name.set(data[0]),
        self.var_description.set(data[1]),
        self.var_gender.set(data[2]),
        self.var_Id.set(data[3]),
        #self.var_radio1.set(data[4])
    

    # ***************update function******************

    def update_data(self):
        if self.var_Id.get()=='' or self.var_gender.get()=='' or self.var_name.get()=='' or self.var_description.get()=='':
            messagebox.showerror('Error', 'All fields are required.', parent=self.root)
        else:
            try:
                update = messagebox.askyesno('Update', 'Do you want to update this data?', parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='face_recognizer')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update student set Name=%s, Gender=%s, description=%s where Id=%s', (
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_description.get(),
                        self.var_Id.get(),
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo('Success', 'Data Updated Successfully.', parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error', f' Due To:  {str(es)}', parent=self.root)
    

    # ******************delete function******************

    def delete_data(self):
        if self.var_Id.get()=='':
            messagebox.showerror('Error', 'Id required', parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('Delete Data', 'Do you want to delete data?', parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='face_recognizer')
                    my_cursor = conn.cursor()
                    sql = 'delete from student where Id=%s'
                    val = (self.var_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Data Deleted Successfully.', parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f' Due To:  {str(es)}', parent=self.root)


    # *******************reset function******************

    def reset_data(self):
        self.var_name.set('')
        self.var_Id.set('')
        self.var_gender.set('Male')
        self.var_description.set('')
    
    # ***************generate data set**************************
    def generate_dataset(self):
        #if self.var_Id.get()=='' or self.var_gender.get()=='' or self.var_name.get()=='' or self.var_description.get()=='':
        if self.var_gender.get()=='' or self.var_name.get()=='' or self.var_description.get()=='':
            messagebox.showerror('Error', 'All fields are required.', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute('update student set Name=%s, Gender=%s, Description=%s where Id=%s', (
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_description.get(),
                    #self.var_radio1.get(),
                    self.var_Id.get(),
                    
                    
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor is 1.3, minimum neighbor is 5

                    for (x,y,w,h) in faces:
                        face = img[y:y+h, x:x+w]
                        return face
                
                video = cv2.VideoCapture(0)
                #url = 'http://192.168.43.251:4747'
                # video = cv2.VideoCapture(url)
                #video.open(video)
                #video_cap = cv2.VideoCapture('protocol://192.168.43.251:4747/')
                import urllib.request
                import numpy as np
                
                #cap = cv2.VideoCapture(0)
                img_id = 0
                '''while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(url).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
    
                    if cv2.waitKey(1)==13:
                        break'''
                while True:
                    ret, my_frame = video.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = 'Data/user.'+str(id)+'.'+str(img_id)+'.jpg'
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv2.imshow('Cropped Face', face)

                    if cv2.waitKey(1)==13 or int(img_id)==250:
                        break
                video.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result', 'Data Added Successfully!!', parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f' Due To:  {str(es)}', parent=self.root)







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

    