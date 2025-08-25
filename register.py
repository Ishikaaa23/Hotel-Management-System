from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register')
        self.root.geometry('1600x900+0+0')

#-----variables----------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

#-------------bg image---------------
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Ishika\Pictures\hotel\login.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

#----------left image----------------
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Ishika\Pictures\hotel\hotel4.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

#---------main frame---------
        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=('times new roman',20,'bold'),bg='white',fg='gold')
        register_lbl.place(x=20,y=20)

#--------label & entry---------
        #1st row
        fname=lbl=Label(frame,text='First Name',font=('times new roman',15,'bold'),bg='white')
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=('times new roman',15,'bold'))
        fname_entry.place(x=50,y=130,width=250)

        l_name=lbl=Label(frame,text='Last Name',font=('times new roman',15,'bold'),fg='black',bg='white')
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=('times new roman',15))
        self.txt_lname.place(x=370,y=130,width=250)

        #2nd row
        contact=Label(frame,text='Contact No.',font=('times new roman',15,'bold'),bg='white',fg='black')
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=('times new roman',15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text='Email',font=('times new roman',15,'bold'),fg='black',bg='white')
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=('times new roman',15))
        self.txt_email.place(x=370,y=200,width=250)

        #3rd row
        security_Q=Label(frame,text='Select Security Question',font=('times new roman',15,'bold'),bg='white',fg='black')
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=('times new roman',15,'bold'),state='readonly')
        self.combo_security_Q['values']=('Select','Your birth place','Your pet name')
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text='Security Answer',font=('times new roman',15,'bold'),fg='black',bg='white')
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=('times new roman',15))
        self.txt_security.place(x=370,y=270,width=250)

        #4th row
        pswd=Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white',fg='black')
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=('times new roman',15))
        self.txt_pswd.place(x=50,y=340,width=250)

        pswd=Label(frame,text='Confirm Password',font=('times new roman',15,'bold'),fg='black',bg='white')
        pswd.place(x=370,y=310)

        self.txt_conf_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=('times new roman',15))
        self.txt_conf_pswd.place(x=370,y=340,width=250)

#-----------check button-------------
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text='I agree to the terms & conditions',font=('times new roman',12),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

#----------buttons-------------
        reg_btn=Button(frame,text="Register Now",command=self.RegisterData,font=('times new roman',15,'bold'),relief=RIDGE,bg='gold',fg='black',bd=3)
        reg_btn.place(x=50,y=420,width=250,height=35)

        login_btn=Button(frame,text="Login Now",font=('times new roman',15,'bold'),command=self.return_login,relief=RIDGE,bg='gold',fg='black',bd=3)
        login_btn.place(x=370,y=420,width=250,height=35)

#-------function declaration---------
    def RegisterData(self):
        if self.var_fname.get()=='' or self.var_email.get()=='' or self.var_securityQ.get()=='Select':
            messagebox.showerror('Error','All fields are required')
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwword didn't match,try again!")
        elif self.var_check.get()==0:
            messagebox.showerror('Error','Please agree our terms & conditions')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            query=('select * from register where email=%s')
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','User already exist,please try another email')
            else:
                my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                        self.var_fname.get(),
                                                                        self.var_lname.get(),
                                                                        self.var_contact.get(),
                                                                        self.var_email.get(),
                                                                        self.var_securityQ.get(),
                                                                        self.var_securityA.get(),
                                                                        self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success','Registration successful')

    def return_login(self):
        self.root.destroy()






if __name__=='__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()