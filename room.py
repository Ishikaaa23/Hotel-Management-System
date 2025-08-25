from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

#-------variables--------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()        

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
        lblframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room booking Details',padx=2,
                                font=('arial',12,'bold'))
        lblframeleft.place(x=5,y=50,width=425,height=490)

#-------label & entry----------
        #customer contact
        lbl_cust_contact=Label(lblframeleft,text='Customer Contact:',padx=2,pady=6,font=('arial',12,'bold'))
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(lblframeleft,textvariable=self.var_contact,width=20,font=('arial',13,'bold'))
        entry_contact.grid(row=0,column=1,sticky=W)

           #fetch data button
        buttonFetchData=Button(lblframeleft,text='Fetch Data',command=self.FetchContact,font=('arial',8,'bold'),bg='black',fg='gold',width=9)
        buttonFetchData.place(x=347,y=4)

        #check_in_date
        check_in_date=Label(lblframeleft,text='Check_in date:',font=('arial',13,'bold'),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(lblframeleft,textvariable=self.var_checkin,width=29,font=('arial',13,'bold'))
        txtcheck_in_date.grid(row=1,column=1)

        #check_out_date
        check_out_date=Label(lblframeleft,text='Check_outdate:',font=('arial',13,'bold'),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date=ttk.Entry(lblframeleft,width=29,textvariable=self.var_checkout,font=('arial',13,'bold'))
        txtcheck_out_date.grid(row=2,column=1)

        #RoomType combobox
        lbl_RoomType=Label(lblframeleft,text='Room Type:',font=('arial',13,'bold'),padx=2,pady=6)
        lbl_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select RoomType from details')
        rows1=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(lblframeleft,width=27,textvariable=self.var_roomtype,font=('arial',13,'bold'),state='readonly')
        combo_RoomType["value"]=rows1
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Room Available
        lblRoomAvail=Label(lblframeleft,text='Available Room:',font=('arial',13,'bold'),padx=2,pady=6)
        lblRoomAvail.grid(row=4,column=0,sticky=W)
        #txtRoomAvail=ttk.Entry(lblframeleft,width=29,textvariable=self.var_roomavailable,font=('arial',13,'bold'))
        #txtRoomAvail.grid(row=4,column=1)

        conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select RoomNo from details')
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(lblframeleft,width=27,textvariable=self.var_roomavailable,font=('arial',13,'bold'),state='readonly')
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #meal
        lblMeal=Label(lblframeleft,text='Meal:',font=('arial',13,'bold'),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(lblframeleft,width=29,textvariable=self.var_meal,font=('arial',13,'bold'))
        txtMeal.grid(row=5,column=1)

        #No. Of Days
        lblNoOfDays=Label(lblframeleft,text='No. Of Days:',font=('arial',13,'bold'),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(lblframeleft,width=29,textvariable=self.var_noofdays,font=('arial',13,'bold'))
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblPaidTax=Label(lblframeleft,text='Paid Tax:',font=('arial',13,'bold'),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)
        txtPaidTax=ttk.Entry(lblframeleft,width=29,textvariable=self.var_paidtax,font=('arial',13,'bold'))
        txtPaidTax.grid(row=7,column=1)

        #Sub Total
        lblSubTotal=Label(lblframeleft,text='Sub Total:',font=('arial',13,'bold'),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(lblframeleft,width=29,textvariable=self.var_actualtotal,font=('arial',13,'bold'))
        txtSubTotal.grid(row=8,column=1)

        #Total Cost
        lblTotalCost=Label(lblframeleft,text='Total Cost:',font=('arial',13,'bold'),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(lblframeleft,width=29,textvariable=self.var_total,font=('arial',13,'bold'))
        txtTotalCost.grid(row=9,column=1)

#--------bill button---------
        buttonBill=Button(lblframeleft,text='Bill',command=self.total,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonBill.grid(row=10,column=0,padx=1,sticky=W)

#------------button----------
        button_frame=Frame(lblframeleft,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=400,width=412,height=40)

        buttonAdd=Button(button_frame,text='Add',command=self.add_data,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonAdd.grid(row=0,column=0,padx=1)

        buttonUpdate=Button(button_frame,text='Update',command=self.update,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonUpdate.grid(row=0,column=1,padx=1)

        buttonDelete=Button(button_frame,text='Delete',command=self.mDelete,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonDelete.grid(row=0,column=2,padx=1)

        buttonReset=Button(button_frame,text='Reset',command=self.reset,font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        buttonReset.grid(row=0,column=3,padx=1)

#------right side image--------------
        img3=Image.open(r"C:\Users\Ishika\Pictures\hotel\room1.jpg")
        img3=img3.resize((540,250),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        labeling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        labeling.place(x=760,y=55,width=540,height=250)

#------Table frame (search system) --------
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',padx=2, 
                               font=('arial',12,'bold'))
        table_frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(table_frame,text='Search By:',font=('arial',12,'bold'),padx=2,pady=6)
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,width=24,textvariable=self.search_var,font=('arial',12,'bold'),state='readonly')
        combo_search["value"]=('Contact','Room')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame,width=29,textvariable=self.txt_search,font=('arial',13,'bold'))
        txtSearch.grid(row=0,column=2,padx=2)

        buttonSearch=Button(table_frame,text='Search',command=self.search,font=('arial',13,'bold'),bg='black',fg='gold',width=10)
        buttonSearch.grid(row=0,column=3,padx=1)

        buttonShowAll=Button(table_frame,text='Show All',command=self.fetch_data,font=('arial',13,'bold'),bg='black',fg='gold',width=10)
        buttonShowAll.grid(row=0,column=4,padx=1)

#--------show data table------------
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,columns=('contact','checkin','checkout','roomtype',
                'roomavailable','meal','noofdays'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('contact',text='Contact')
        self.room_table.heading('checkin',text='Check-in')
        self.room_table.heading('checkout',text='Check-out')
        self.room_table.heading('roomtype',text='Room Type')
        self.room_table.heading('roomavailable',text='Room No.')
        self.room_table.heading('meal',text='Meal')
        self.room_table.heading('noofdays',text='NoOdDays')

        self.room_table['show']='headings'

        self.room_table.column('contact',width=100)
        self.room_table.column('checkin',width=100)
        self.room_table.column('checkout',width=100)
        self.room_table.column('roomtype',width=100)
        self.room_table.column('roomavailable',width=100)
        self.room_table.column('meal',width=100)
        self.room_table.column('noofdays',width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=='' or self.var_checkin.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into room values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get()                
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Room booked',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning','Something went wrong:',parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from room')
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get()=='':
            messagebox.showerror('Error','Please enter contact number',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute('update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where contact=%s',(
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get(),
                                                                                        self.var_contact.get()
                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('update','room details has been updated successfully',parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno('Hotel Management System','Do you want to delete this customer',parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            query='delete from room where contact=%s'
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(''),
        self.var_checkin.set(''),
        self.var_checkout.set(''),
        self.var_roomtype.set(''),
        self.var_roomavailable.set(''),
        self.var_meal.set(''),
        self.var_noofdays.set(''),
        self.var_paidtax=StringVar(''),
        self.var_actualtotal=StringVar(''),
        self.var_total=StringVar('')

#-----------all data fetch------------
    def FetchContact(self):
        if self.var_contact.get()=='':
            messagebox.showerror('Error','Please enter contact number')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            query=('select Name from customer where Mobile=%s')
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()  

            if row==None:
                messagebox.showerror('Error','This number is not found',parent=self.root)
            else:
                conn.commit()
                conn.close()     

                showDataFreame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFreame.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataFreame,text='Name:',font=('arial',12,'bold'))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFreame,text=row,font=('arial',12,'bold'))
                lbl.place(x=90,y=0)
#gender
                conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
                my_cursor=conn.cursor()
                query=('select Gender from customer where Mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone() 

                lblGender=Label(showDataFreame,text='Gender:',font=('arial',12,'bold'))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataFreame,text=row,font=('arial',12,'bold'))
                lbl2.place(x=90,y=30)
#email
                conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
                my_cursor=conn.cursor()
                query=('select Email from customer where Mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone() 

                lblEmail=Label(showDataFreame,text='Email:',font=('arial',12,'bold'))
                lblEmail.place(x=0,y=60)

                lbl3=Label(showDataFreame,text=row,font=('arial',12,'bold'))
                lbl3.place(x=90,y=60)
#nationality
                conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
                my_cursor=conn.cursor()
                query=('select Nationality from customer where Mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone() 

                lblNationality=Label(showDataFreame,text='Nationality:',font=('arial',12,'bold'))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataFreame,text=row,font=('arial',12,'bold'))
                lbl4.place(x=90,y=90)
#address
                conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
                my_cursor=conn.cursor()
                query=('select Address from customer where Mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone() 

                lblAddress=Label(showDataFreame,text='Address:',font=('arial',12,'bold'))
                lblAddress.place(x=0,y=120)

                lbl5=Label(showDataFreame,text=row,font=('arial',12,'bold'))
                lbl5.place(x=90,y=120)

#-------search system------------
    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
        my_cursor=conn.cursor()

        my_cursor.execute('select * from room where '+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,'%d/%m/%Y')
        outDate=datetime.strptime(outDate,'%d/%m/%Y')
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=='breakfast' and self.var_roomtype.get()=='luxury'):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax='Rs.'+str('%.2f'%((q5)*0.09))
            ST='Rs.'+str('%.2f'%(q5))
            TT='Rs.'+str('%.2f'%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=='lunch' and self.var_roomtype.get()=='single'):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax='Rs.'+str('%.2f'%((q5)*0.09))
            ST='Rs.'+str('%.2f'%(q5))
            TT='Rs.'+str('%.2f'%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)





if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()