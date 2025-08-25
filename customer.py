from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class CustomerWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

#-------variables----------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_idp_roof=StringVar()
        self.var_id_number=StringVar()

#-------- title----------
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=('times new roman',18,'bold'),bg='black',
                        fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

# ------ logo -----------
        img2=Image.open(r"C:\Users\Ishika\Pictures\hotel\logo1.jpeg")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labeling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        labeling.place(x=5,y=4,width=80,height=40)

#--------label frame-------
        lblframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',padx=2,
                                font=('arial',12,'bold'))
        lblframeleft.place(x=5,y=50,width=425,height=490)

#-------label & entry----------
        #customer ref
        lbl_cust_ref=Label(lblframeleft,text='Customer Ref:',padx=2,pady=6,font=('arial',12,'bold'))
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(lblframeleft,width=29,textvariable=self.var_ref,font=('arial',13,'bold'),state='readonly')
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(lblframeleft,text='Customer Name:',font=('arial',13,'bold'),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(lblframeleft,width=29,textvariable=self.var_cust_name,font=('arial',13,'bold'))
        txtcname.grid(row=1,column=1)

        #mother name
        mname=Label(lblframeleft,text='Mother Name:',font=('arial',13,'bold'),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(lblframeleft,width=29,textvariable=self.var_mother,font=('arial',13,'bold'))
        txtmname.grid(row=2,column=1)

        #gender combobox
        lbl_gender=Label(lblframeleft,text='Gender:',font=('arial',13,'bold'),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(lblframeleft,width=27,textvariable=self.var_gender,font=('arial',13,'bold'),state='readonly')
        combo_gender["value"]=('Male','Female','Other')
        combo_gender.grid(row=3,column=1)
        
        #postcode
        lblpostcode=Label(lblframeleft,text='PostCode:',font=('arial',13,'bold'),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtpostcode=ttk.Entry(lblframeleft,width=29,textvariable=self.var_post,font=('arial',13,'bold'))
        txtpostcode.grid(row=4,column=1)

        #mobile number
        lblMobile=Label(lblframeleft,text='Mobile:',font=('arial',13,'bold'),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(lblframeleft,width=29,textvariable=self.var_mobile,font=('arial',13,'bold'))
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail=Label(lblframeleft,text='Email:',font=('arial',13,'bold'),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(lblframeleft,width=29,textvariable=self.var_email,font=('arial',13,'bold'))
        txtEmail.grid(row=6,column=1)

        #nationality
        lblnationality=Label(lblframeleft,text='Nationality:',font=('arial',13,'bold'),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(lblframeleft,width=27,textvariable=self.var_nationality,font=('arial',13,'bold'),state='readonly')
        combo_nationality["value"]=('Indian','American','British','Chinese','Others')
        combo_nationality.grid(row=7,column=1)
        
        #idproof type combo box
        lblIdproof=Label(lblframeleft,text='Id Proof Type:',font=('arial',13,'bold'),padx=2,pady=6)
        lblIdproof.grid(row=8,column=0,sticky=W)
        combo_id=ttk.Combobox(lblframeleft,width=27,textvariable=self.var_idp_roof,font=('arial',13,'bold'),state='readonly')
        combo_id["value"]=('Adhaar Card','Driving Licence','Passport')
        combo_id.grid(row=8,column=1)
        
        #id
        lblIdNum=Label(lblframeleft,text='Id Number:',font=('arial',13,'bold'),padx=2,pady=6)
        lblIdNum.grid(row=9,column=0,sticky=W)
        txtIdNum=ttk.Entry(lblframeleft,width=29,textvariable=self.var_id_number,font=('arial',13,'bold'))
        txtIdNum.grid(row=9,column=1)

        #address
        lblAddress=Label(lblframeleft,text='Address:',font=('arial',13,'bold'),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(lblframeleft,width=29,textvariable=self.var_address,font=('arial',13,'bold'))
        txtAddress.grid(row=10,column=1)
#------------button----------
        button_frame=Frame(lblframeleft,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=400,width=412,height=40)

        buttonAdd=Button(button_frame,text='Add',command=self.add_data,font=('arial',13,'bold'),bg='black',fg='gold',width=9,height=2)
        buttonAdd.grid(row=0,column=0,padx=1)

        buttonUpdate=Button(button_frame,text='Update',command=self.update,font=('arial',13,'bold'),bg='black',fg='gold',width=9,height=2)
        buttonUpdate.grid(row=0,column=1,padx=1)

        buttonDelete=Button(button_frame,text='Delete',command=self.mDelete,font=('arial',13,'bold'),bg='black',fg='gold',width=9,height=2)
        buttonDelete.grid(row=0,column=2,padx=1)

        buttonReset=Button(button_frame,text='Reset',command=self.reset,font=('arial',13,'bold'),bg='black',fg='gold',width=9,height=2)
        buttonReset.grid(row=0,column=3,padx=1)

#------Table frame (search system) --------
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',padx=2, 
                               font=('arial',12,'bold'))
        table_frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(table_frame,text='Search By:',font=('arial',12,'bold'),padx=2,pady=6)
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,width=24,textvariable=self.search_var,font=('arial',12,'bold'),state='readonly')
        combo_search["value"]=('Mobile','Ref')
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
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.cust_details_table=ttk.Treeview(details_table,columns=('ref','name','mother','gender','post','mobile',
                'email','nationality','idproof','idnumber','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.xview)

        self.cust_details_table.heading('ref',text='Refer No')
        self.cust_details_table.heading('name',text='Name')
        self.cust_details_table.heading('mother',text='Mother Name')
        self.cust_details_table.heading('gender',text='Gender')
        self.cust_details_table.heading('post',text='PostCode')
        self.cust_details_table.heading('mobile',text='Mobile')
        self.cust_details_table.heading('email',text='Email')
        self.cust_details_table.heading('nationality',text='Nationality')
        self.cust_details_table.heading('idproof',text='Id Proof')
        self.cust_details_table.heading('idnumber',text='Id Number')
        self.cust_details_table.heading('address',text='Address')

        self.cust_details_table['show']='headings'

        self.cust_details_table.column('ref',width=100)
        self.cust_details_table.column('name',width=100)
        self.cust_details_table.column('mother',width=100)
        self.cust_details_table.column('gender',width=100)
        self.cust_details_table.column('post',width=100)
        self.cust_details_table.column('mobile',width=100)
        self.cust_details_table.column('email',width=100)
        self.cust_details_table.column('nationality',width=100)
        self.cust_details_table.column('idproof',width=100)
        self.cust_details_table.column('idnumber',width=100)
        self.cust_details_table.column('address',width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=='' or self.var_mother.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_mother.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_idp_roof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_address.get()                
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Customer has been added',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning','Something went wrong:',parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from customer')
        rows=my_cursor.fetchall()
        if(len(rows))!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idp_roof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=='':
            messagebox.showerror('Error','Please enter mobile number',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute('update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where ref=%s',(
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_mother.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_idp_roof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_ref.get()
                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('update','customer details has been updated successfully',parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno('Hotel Management System','Do you want to delete this customer',parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            query='delete from customer where Ref=%s'
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(''),
        self.var_cust_name.set(''),
        self.var_mother.set(''),
        self.var_gender.set(''),
        self.var_post.set(''),
        self.var_mobile.set(''),
        self.var_email.set(''),
        self.var_nationality.set(''),
        self.var_idp_roof.set(''),
        self.var_id_number.set(''),
        self.var_address.set('')
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
        my_cursor=conn.cursor()

        my_cursor.execute('select * from customer where '+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert('',END,values=i)
            conn.commit()
        conn.close()





if __name__=="__main__":
    root=Tk()
    obj=CustomerWindow(root)
    root.mainloop()