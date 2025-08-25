from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from hotel import HotelManagementSystem
from register import Register

def main():
    win=Tk()
    app=LoginWindow(win)
    win.mainloop()

class LoginWindow:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Ishika\Pictures\hotel\login.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Ishika\Pictures\hotel\login2.webp")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg='black',borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=('times new roman',20,'bold'),bg='black',fg='white')
        get_str.place(x=95,y=100)

#--------label--------
        username=lbl=Label(frame,text='Username',font=('times new roman',15,'bold'),bg='black',fg='white')
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text='Password',font=('times new roman',15,'bold'),bg='black',fg='white')
        password.place(x=40,y=225)

        self.txtpass=ttk.Entry(frame,font=('times new roman',15,'bold'),show='*')
        self.txtpass.place(x=40,y=250,width=270)

#----------button---------
        login_btn=Button(frame,text="Login",command=self.login,font=('times new roman',15,'bold'),relief=RIDGE,bg='gold',fg='black',bd=3)
        login_btn.place(x=110,y=300,width=120,height=35)

        register_btn=Button(frame,text="New user register",command=self.register_window,font=('times new roman',10,'bold'),bg='black',fg='gold',borderwidth=0,activebackground='black',activeforeground='gold')
        register_btn.place(x=15,y=350,width=160)

        forgot_btn=Button(frame,text="Forgot password",command=self.forgot_password_window,font=('times new roman',10,'bold'),bg='black',fg='gold',borderwidth=0,activebackground='black',activeforeground='gold')
        forgot_btn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=='' or self.txtpass.get()=='':
            messagebox.showerror('Error','All fields required')
        elif self.txtuser.get()=='Ishika' and self.txtpass.get()=='Ishika23':
            messagebox.showinfo('Success',"Welcome to our hotel management system")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute('select * from register where email=%s and password=%s',(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid username and password')
            else:
                open_main=messagebox.askyesno('YesNo','Access only admin')
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#-------reset password----------
    def reset_password(self):
        if self.combo_security_Q.get()=='select':
            messagebox.showerror('Error','Select the security question',parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror('Error','Please enter the answer',parent=self.root2)
        elif self.txt_newpass.get()=='':
            messagebox.showerror('Error','Please enter the new password',parent=self.root2)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            query=('select * from register where email=%s and securityQ=%s and securityA=%s')
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Please enter correct answer',parent=self.root2)
            else:
                query=('update register set password=%s where email=%s')
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Info','Your password has been changed, please login with new password',parent=self.root2)
                self.root2.destroy()

#--------forgot passwordwindow-------------
    def forgot_password_window(self):
        if self.txtuser.get()=='':
            messagebox.showerror('Error','Please enter the Email to reset password')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='ishikadas23',database='management')
            my_cursor=conn.cursor()
            query=('select * from register where email=%s')
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror('Error','Please enter the valis username')
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title('Forgot Password')
                self.root2.geometry('340x450+610+170')

                l=Label(self.root2,text="Forgot Password",font=('times new roman',20,'bold'),fg='red',bg='white')
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text='Select Security Question',font=('times new roman',15,'bold'),bg='white',fg='black')
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=('times new roman',15,'bold'),state='readonly')
                self.combo_security_Q['values']=('Select','Your birth place','Your pet name')
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text='Security Answer',font=('times new roman',15,'bold'),fg='black',bg='white')
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=('times new roman',15))
                self.txt_security.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text='New Password',font=('times new roman',15,'bold'),fg='black',bg='white')
                new_pass.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=('times new roman',15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text='Reset',command=self.reset_password,font=('times new roman',15,'bold'),bg='gold',fg='black')
                btn.place(x=110,y=300,width=120,height=35)




if __name__=='__main__':
    main()