from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ************variables**************
        self.var_status = StringVar()
        self.var_name = StringVar()
        self.var_description = StringVar()
        self.var_gender = StringVar()
        self.var_Id = StringVar()


        # first image
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
        img3 = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\attendence.png")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height =710)

        title_lbl = Label(bg_img,text="Criminal's Record", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

    
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

         #left label frame

        Left_frame = LabelFrame( main_frame,bd=2,relief=RIDGE,text="Record", font=('times new roman',15,"bold"))
        Left_frame.place(x=10,y=10, width=730,height=580)

        #left image
        img_left = Image.open(r"C:\Users\smita\OneDrive\Desktop\Project\Project\Images\lib.png")
        img_left = img_left.resize((550,200),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left )
        f_lbl.place(x=5, y=0, width=720, height =200)

        left_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_frame.place(x=50,y=210,width=635,height=300)


        
        #Labels_and_entry
        #current_id
        person_id = Label(left_frame,text="Id",font=("times new roman",13,"bold"), bg="white")
        person_id.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        person_id_block = ttk.Entry(left_frame,textvariable=self.var_Id ,font=("times new roman",13,"bold"))
        person_id_block.grid(row=4,column=1,padx=5,pady=7,sticky=W)

        #current_personname
        person_name = Label(left_frame,text="Name",font=("times new roman",13,"bold"),bg="white")
        person_name.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        person_name_block = ttk.Entry(left_frame, textvariable=self.var_name, font=("times new roman",13,"bold"))
        person_name_block.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #current_persondesc
        person_phone = Label(left_frame,text="Description",  font=("times new roman",13,"bold"), bg="white")
        person_phone.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        person_phone_block = ttk.Entry(left_frame,textvariable=self.var_description,font=("times new roman",13,"bold"))
        person_phone_block.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        
        #current_gender
        person_Gender = Label(left_frame,text="Gender", font=("times new roman",13,"bold"), bg="white")
        person_Gender.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        gender_combo = ttk.Combobox(left_frame, textvariable=self.var_gender,font=("times new roman",13,"bold"), state='readonly', width=18)
        gender_combo["values"] = ("Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,padx=6,pady=10,sticky=W)

         #status
        status = Label(left_frame,text="Availability", font=("times new roman",13,"bold"), bg="white")
        status.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        #status_block = ttk.Entry(left_frame,font=("times new roman",13,"bold"))
        #status_block.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        gen = ttk.Combobox(left_frame, textvariable=self.var_status,font=("times new roman",13,"bold"), state='readonly', width=18)
        gen["values"] = ("Available", "Not Available",)
        gen.current(0)
        gen.grid(row=3, column=1,padx=6,pady=10,sticky=W)

        #buttons frame
        btn_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=90,y=450,width=550,height=40)  

        save_btn = Button(btn_frame, text="Import csv", width=13, command=self.importCSV, font=("times new roman",13,"bold"),bg="gray",fg="white")     
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", width=13, command=self.exportCSV,font=("times new roman",13,"bold"),bg="gray",fg="white")     
        update_btn.grid(row=0, column=1)

        del_btn = Button(btn_frame, text="Update", width=13, font=("times new roman",13,"bold"),bg="gray",fg="white")     
        del_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=13, command=self.reset_data,font=("times new roman",13,"bold"),bg="gray",fg="white")     
        reset_btn.grid(row=0, column=3)

        #right label frame

        Right_frame = LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE,text="Record", font=('times new roman',15,"bold"))
        Right_frame.place(x=750,y=10, width=730,height=580)

        tbl_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        tbl_frame.place(x=3,y=0,width=710,height=550) 

        #======================scroll bar==========================
        scroll_x = ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tbl_frame,orient=VERTICAL)

        self.AttendenceReportTable = ttk.Treeview(tbl_frame,column=("Name","Description","Gender","Availability","Id",),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set) 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("Name", text="Name")
        self.AttendenceReportTable.heading("Description", text="Description")
        self.AttendenceReportTable.heading("Gender", text="Gender")
        self.AttendenceReportTable.heading("Availability", text="Availability")
        self.AttendenceReportTable.heading("Id", text="Id")
        self.AttendenceReportTable["show"]="headings"
        
        self.AttendenceReportTable.column("Name",width=100)
        self.AttendenceReportTable.column("Description",width=100)
        self.AttendenceReportTable.column("Gender",width=100)
        self.AttendenceReportTable.column("Availability",width=100)
        self.AttendenceReportTable.column("Id",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

       
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    #import csv
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    
    def get_cursor(self,event=""):
        cursor_row = self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_name.set(rows[0])
        self.var_description.set(rows[1])
        self.var_gender.set(rows[2])
        self.var_status.set(rows[3])
        self.var_Id.set(rows[4])

    def reset_data(self):
        self.var_name.set("")
        self.var_description.set("")
        self.var_gender.set("Male")
        self.var_status.set("Available")
        self.var_Id.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()