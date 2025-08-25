from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

        # -------- title----------
        lbl_title = Label(self.root, text="REPORT AN ISSUE", font=('times new roman', 18, 'bold'), bg='black',
                          fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ------ logo -----------
        img2 = Image.open(r"C:\Users\Ishika\Pictures\hotel\logo1.jpeg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labeling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        labeling.place(x=5, y=4, width=80, height=40)

        # --------label frame-------
        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, padx=2)
        lblframeleft.place(x=5, y=50, width=425, height=490)

        # report
        lbl_report = Label(lblframeleft, text='Enter the issue:', padx=2, pady=6, font=('arial', 12, 'bold'))
        lbl_report.grid(row=0, column=0, sticky=W)

        self.txt_report = Text(lblframeleft, width=30, height=4, font=('arial', 12))
        self.txt_report.grid(row=0, column=1,padx=5,pady=5, sticky=W)

        # button
        buttonAdd = Button(lblframeleft, text='Save', command=self.add_data, font=('arial', 11, 'bold'),
                           bg='black', fg='gold', width=10)
        buttonAdd.grid(row=2, column=1, padx=1, pady=10)

        # ------Table frame --------
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show All Reports', padx=2,
                                 font=('arial', 12, 'bold'))
        table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(table_frame, columns=('report'), xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('report', text='Report')
        self.room_table['show'] = 'headings'
        self.room_table.column('report', width=500)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()

    def add_data(self):
        issue_text = self.txt_report.get("1.0", END).strip()

        if issue_text == '':
            messagebox.showerror('Error', 'Please enter something', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='ishikadas23', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO report VALUES (%s)', (issue_text,))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Issue added successfully', parent=self.root)
                self.txt_report.delete("1.0", END)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong:\n{str(es)}', parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username='root', password='ishikadas23', database='management')
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM report')
        rows = my_cursor.fetchall()
        if rows:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('', END, values=i)
        conn.close()

    def get_cursor(self, event=''):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']
        if row:
            self.txt_report.delete("1.0", END)
            self.txt_report.insert(END, row[0])


if __name__ == '__main__':
    root = Tk()
    app = Report(root)
    root.mainloop()
