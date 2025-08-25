from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

#-------- title----------
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=('times new roman',18,'bold'),bg='black',
                        fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

# ------ logo -----------
        img2=Image.open(r"C:\Users\Ishika\Pictures\hotel\logo1.jpeg")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labeling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        labeling.place(x=5,y=4,width=80,height=40)

#--------label frame-------
        lblframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='New Room Add',padx=2,
                                font=('arial',12,'bold'))
        lblframeleft.place(x=5,y=50,width=425,height=490)

        #floor
        lbl_floor=Label(lblframeleft,text='Floor:',padx=2,pady=6,font=('arial',12,'bold'))
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(lblframeleft,width=20,textvariable=self.var_floor,font=('arial',13,'bold'))
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room No.
        lbl_RoomNo=Label(lblframeleft,text='Room No.:',padx=2,pady=6,font=('arial',12,'bold'))
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        entry_RoomNo=ttk.Entry(lblframeleft,width=20,textvariable=self.var_roomNo,font=('arial',13,'bold'))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType=Label(lblframeleft,text='Room Type:',padx=2,pady=6,font=('arial',12,'bold'))
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(lblframeleft,width=20,textvariable=self.var_RoomType,font=('arial',13,'bold'))
        entry_RoomType.grid(row=2,column=1,sticky=W)

#------------button----------
        button_frame=Frame(lblframeleft,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=200,width=412,height=40)

        buttonAdd=Button(button_frame,text='Add',command=self.add_data,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonAdd.grid(row=0,column=0,padx=1)

        buttonUpdate=Button(button_frame,text='Update',command=self.update,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonUpdate.grid(row=0,column=1,padx=1)

        buttonDelete=Button(button_frame,text='Delete',command=self.mDelete,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonDelete.grid(row=0,column=2,padx=1)

        buttonReset=Button(button_frame,text='Reset',command=self.reset_data,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonReset.grid(row=0,column=3,padx=1)

#------Table frame (search system) --------
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Show Room Details',padx=2, 
                               font=('arial',12,'bold'))
        table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(table_frame,columns=('floor','roomno','roomType'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('floor',text='Floor')
        self.room_table.heading('roomno',text='Room No.')
        self.room_table.heading('roomType',text='Room Type')

        self.room_table['show']='headings'

        self.room_table.column('floor',width=100)
        self.room_table.column('roomno',width=100)
        self.room_table.column('roomType',width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=='' or self.var_RoomType.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into details values(%s,%s,%s)',(
                                                                                        self.var_floor.get(),
                                                                                        self.var_roomNo.get(),
                                                                                        self.var_RoomType.get()                
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','New room added successfully',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning','Something went wrong:',parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from details')
        rows=my_cursor.fetchall()
        if(len(rows))!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content['values']

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])

    def update(self):
        if self.var_floor.get()=='':
            messagebox.showerror('Error','Please enter floor number',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute('update details set Floor=%s,RoomType=%s where RoomNo=%s',(
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_roomNo.get()
                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('update','room details has been updated successfully',parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno('Hotel Management System','Do you want to delete this room details',parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            query='delete from details where RoomNo=%s'
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_floor.set(''),
        self.var_roomNo.set(''),
        self.var_RoomType.set('')





if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()