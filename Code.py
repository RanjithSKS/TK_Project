from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import smtplib
import random
from tkcalendar import Calendar
from datetime import datetime
import pasword as p
tk = Tk()
tk.state('zoomed')
tk.title("Ranjith.S Project")

def project(tk):
    def rearrange_digits(number):
        digits = [digit for digit in str(number)]
        random.shuffle(digits)
        rearranged_number = int(''.join(map(str, digits)))
        return rearranged_number
    number = 123456
    rearranged_number = rearrange_digits(number)

    def send_email():
        sender_email = "ranjithdatascience05@gmail.com"
        receiver_email = entry_recipient.get()
        password = p.smpt_password
        email_body = str(rearranged_number)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, email_body)
            server.quit()
            messagebox.showinfo("Success", "OTP sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email.")
    
    def password_entry():
        menubar.destroy()
        label1.destroy()
        label_recipient.destroy()
        label_recipient1.destroy()
        entry_recipient.destroy()
        btn_verify.destroy()
        label_password.destroy()
        btn_login .destroy()
        lab3.destroy()
        entered_password = la.get()
        if int(entered_password) == rearranged_number:
            la.destroy()
            image = Image.open("Intex_Image.jpg")
            resize1 = image.resize((1400, 650))
            img = ImageTk.PhotoImage(resize1)
            lab1 = Label(image=img)
            lab1.image = img
            lab1.pack()
            messagebox.showinfo("Success", "Login Success")

            def open_new_window():
                def open_new_window1():                              
                    def submit():

                        bill_frame = Frame(new_window1, bg='#ffda79', width=800, height=400)
                        bill_frame.place(relx=0.4, rely=0.6, anchor=CENTER)

                        name_value = entry_customer_name.get()
                        address = entry_address.get()
                        phone=entry_phone_number.get()
                        room=lable_Next1.get()
                        Charges=lable_Next2.get()
                        Calendar=cal_widget.get_date()
                        Calendar1=cal_widget1.get_date()
                        print(name_value,address,phone,room,Calendar,Calendar1)

                        labels = [
                            ("Name:", name_value),
                            ("Phone Number:", phone),
                            ("Address:", address),
                            ("Check in date:", Calendar),
                            ("Check Out date:", Calendar1),
                            ("Type of Room:", room),
                            ("Room Charges:", Charges)
                        ]
                        for i, (label_text, value) in enumerate(labels):
                            label_name = Label(bill_frame, text=label_text, bg="white", font=("Arial", 14, "bold"))
                            label_name.grid(row=i, column=0, sticky='w', padx=20, pady=10)
                            label_value = Label(bill_frame, text=value, bg="white", font=("Arial", 14))
                            label_value.grid(row=i, column=1, sticky='w', padx=20, pady=10)

                        import mysql.connector
                        mysql=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="",
                        database="tk_project"
                    )
                        mycursor=mysql.cursor()
                        sql = "INSERT INTO nam (name, address, phone, room, charges, check_in_date, check_out_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        val = (name_value, address, phone, room, Charges, Calendar,Calendar1)
                        mycursor.execute(sql,val)
                        mysql.commit()

                        print("data saved")

                    
                    from PIL import Image, ImageTk 
                    
                    new_window1 = Toplevel(tk)                
                    image1 = Image.open("Intex_Image.jpg")
                    resize2 = image1.resize((1400, 650))
                    img1 = ImageTk.PhotoImage(resize2)
                    ne1 = Label(new_window1,image=img1)
                    ne1.image = img1
                    ne1.pack()                
                    new_window1.state('zoomed')

                    new_label_days_stayed = Label(new_window1, font=("time", 11, "normal"), text="Type of room : ",bg="#ffdd59")
                    new_label_days_stayed.place(x=40, y=65)

                    lable_Next1 = ttk.Combobox(new_window1,width=30,state="readonly")
                    lable_Next1['values']=("1- Single DX", "2- Double DX", "3- Single AC","4- Double AC", "5- Single NAC", "6- Double NAC")
                    lable_Next1.bind("<<ComboboxSelected>>")
                    lable_Next1.current()
                    lable_Next1.place(x=170, y=65)

                    label_address = Label(new_window1, font=("time", 11, "normal"), text="Room Charges : ",bg="#ffdd59")
                    label_address.place(x=40, y=120)
                    lable_Next2 = ttk.Combobox(new_window1,width=30,state="readonly")
                    lable_Next2['values']=("1- Rs.1200", "2- Rs.1700", "3- Rs.1000", "4-Rs.1300", "5- Rs.600", "6- Rs.850")
                    lable_Next2.bind("<<ComboboxSelected>>")
                    lable_Next2.current()
                    lable_Next2.place(x=170, y=120)

                    lable_Next = Checkbutton(new_window1, font=("time", 11, "normal"), text= "Accept Term and Conditions",bg="#ffdd59")
                    lable_Next.place(x=450, y=130)

                    lable_Next = Button(new_window1, font=("time", 11, "normal"), text= "Supmit",background="#ffdd59",command=submit)
                    lable_Next.place(x=450, y=160)

                    lable_Next = Button(new_window1, font=("time", 11, "normal"), text= "Cancel",background="#ffdd59",command=new_window1.destroy)
                    lable_Next.place(x=550, y=160)

                new_window = tk
                def cal():
                    selected_date = cal_widget.get_date()
                    messagebox.showinfo("Selected Date", f"Selected Check-in Date: {selected_date}")

                def cal1():
                    selected_date = cal_widget1.get_date()
                    messagebox.showinfo("Selected Date", f"Selected Check-out Date: {selected_date}")
                    
                    check_in_date = datetime.strptime(cal_widget.get_date(), "%d/%m/%Y")
                    check_out_date = datetime.strptime(cal_widget1.get_date(), "%d/%m/%Y")
                    days_stayed = (check_out_date - check_in_date).days
                    new_label_days_stayed.config(text=f"No of days stayed : {days_stayed}")

                label_customer_name = Label(tk, font=("time", 11, "normal"),bg="#add8e6" ,text="Customer name : ")
                label_customer_name.place(x=40, y=65)
                entry_customer_name = Entry(tk, font=("time", 15, "normal"))
                entry_customer_name.place(x=170, y=65)

                label_address1 = Label(tk, font=("time", 11, "normal"), text="Address : ",background="#add8e6")
                label_address1.place(x=40, y=120)
                entry_address = Entry(new_window, font=("time", 15, "normal"))
                entry_address.place(x=170, y=115)

                label_phone_number = Label(tk, font=("time", 11, "normal"),bg="#add8e6" , text="Phone Number : ")
                label_phone_number.place(x=40, y=175)
                entry_phone_number = Entry(tk, font=("time", 15, "normal"))
                entry_phone_number.place(x=170, y=175)

                label_check_in_date = Label(tk, font=("time", 11, "normal"), text="Check in date : ",bg="#add8e6")
                label_check_in_date.place(x=40, y=230)
                cal_widget = Calendar(tk, selectmode="day", date_pattern="dd/MM/yyyy")
                cal_widget.place(x=170, y=230)
                cal_widget.bind("<<CalendarSelected>>", lambda event: cal())

                label_check_out_date = Label(tk, font=("time", 11, "normal"), text="Check out date : ",bg="#add8e6")
                label_check_out_date.place(x=40, y=430)
                cal_widget1 = Calendar(tk, selectmode="day", date_pattern="dd/MM/yyyy")
                cal_widget1.place(x=170, y=430)
                cal_widget1.bind("<<CalendarSelected>>", lambda event: cal1())

                new_label_days_stayed = Label(tk, font=("time", 11, "normal"), text="No of days stayed : ",bg="#add8e6")
                new_label_days_stayed.place(x=450, y=570)

                lable_Next11 = Button(tk, font=("time", 11, "normal"), text= "Next",command=lambda: [tk.withdraw(),open_new_window1()])
                lable_Next11.place(x=450, y=620)

            open_new_window()
        else:
            messagebox.showerror("Error", "Login Failed")

    lab3 = Label(tk, text="Welcome to.., \n Hotel Reservation", font=("times", 13, "bold"),background="#f6e58d" ,fg="Black")
    lab3.pack(fill=X)

    def New():
        new = Toplevel(tk)
        new.geometry("800x800")
        new.config(bg="#2c3e80")
        new.title("")
        labnew = Label(new, text="Details", font=("times", 15, "bold"), fg="Black", width=10, padx=30, pady=10)
        labnew1 = Label(new, text="* Login with your E-Mail Id  \n * In E-Mail Id Check the Inbox six digit OTP Will Send \n *Six digit OTP Should Entered into OTP Column ", font=("times", 15, "normal"), fg="Black", width=10, padx=30, pady=10)
        labnew.pack(fill=X)
        labnew1.pack(fill=X)
        btnnew = Button(new, text="Close", font=("times", 15, "bold"), width=10, padx=0, pady=0, fg="Black", command=new.destroy)
        btnnew.pack(padx=10, pady=10)

    menubar = Menu(tk)
    filemenu = Menu(menubar,background="#f6e58d",tearoff=0)
    filemenu.add_command(label="Tips for Register", background="green",command=New)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", background="red",command=tk.quit)
    menubar.add_cascade(label="Options_//",menu=filemenu)
    tk.config(menu=menubar)

    image = Image.open("Intex_Image.jpg")
    resize1 = image.resize((1400, 650))
    img = ImageTk.PhotoImage(resize1)
    label1 = Label(image=img)
    label1.image = img
    label1.pack()

    label_recipient1 = Label(tk, text="Registration", font=("time", 16, "bold"), relief="groove")
    label_recipient1.place(x=620, y=320)

    label_recipient = Label(tk, text="Email:", font=("time", 15, "bold"), bg='#eccc68', relief="flat")
    label_recipient.place(x=520, y=400)
    entry_recipient = Entry(tk, font=("time", 15, "normal"))
    entry_recipient.place(x=590, y=400)
    btn_verify = Button(tk, text="Verify", font=("time", 10, "bold"), command=send_email)
    btn_verify.place(x=830, y=400)

    label_password = Label(tk, text="OTP :", font=("time", 15, "bold"), bg="#eccc68", relief="flat")
    label_password.place(x=520, y=450)
    la = Entry(tk, font=("time", 15, "normal"), show="**")
    la.place(x=590, y=450)
    btn_login = Button(tk, text="LOGIN", font=("times", 15, "bold"), bg="#eccc68", fg="black", command=password_entry)
    btn_login.place(x=640, y=500)

project(tk)
tk.mainloop()
