from tkinter import *
from tkinter.messagebox import *
import sqlite3
import datetime
root=Tk()
root.configure(bg='white')
root.state('zoomed')
root.title("intro")
amount_p=0
con=sqlite3.Connection('Envy_db')
cur=con.cursor()
cur.execute("create table if not exists airlines(user_name varchar(20) primary key,first_name varchar(20),last_name varchar(20),phone_number number(10),email varchar(30),passw varchar(20))")
cur.execute("create table if not exists booking(id integer primary key autoincrement, name varchar(20), date varchar(15),no_of_pas integer, amount integer, source varchar(10), destination varchar(10))")
fr2=Frame(bg='white')
fr2.pack(side=BOTTOM,expand=1)
Label(fr2,text="Project By:-\n",font=("courier",16),compound="center",fg="Black",bg='white').pack()
Label(fr2,text="Nihal Anand",font=("times new roman",16),fg="Black",compound="center",bg='white').pack()
Label(fr2,text="Rishabh Khemka",font=("times new roman",16),fg="Black",compound="center",bg='white').pack()
Label(fr2,text="Sudip Nandi\n",font=("times new roman",16),compound="center",fg="Black",bg='white').pack()
fr1=Frame()
fr1.pack(side=BOTTOM,expand=1)
a=PhotoImage(file="air.gif")
Label(fr1,image=a).pack()
def airline():
    root.destroy()
    root1=Tk()
    root1.state('zoomed')
    root1.title("Booking Portal")
    b=PhotoImage(file="aeroplane2.gif")
    Label(root1,image=b).grid(row=0,column=0,columnspan=4,ipadx=450)
    Label(root1,text="Welcome to Envy Airlines",font=("times new roman",17),fg="Black",width=40,bg="White").grid(row=0,column=0,columnspan=4)
    Label(root1,text="Flights Availability",font=("times new roman",17),fg="White",width=46,bg="Black").grid(row=1,column=0,columnspan=4,pady=20)
    Label(root1,text="Select Pick Up Point:",font=("times new roman",14),fg="black").grid(row=2,column=1)
    variable = StringVar(root1)
    variable.set("Select Source") 
    w = OptionMenu(root1, variable, "Delhi", "Kolkata", "Mumbai","U.S.A","Canada")
    w.grid(row=2,column=2)
    Label(root1,text="Select Boarding Point:",font=("times new roman",14),fg="black").grid(row=3,column=1)
    variable1 = StringVar(root1)
    variable1.set("Select Destination") 
    w = OptionMenu(root1, variable1, "Delhi", "Kolkata", "Mumbai","U.S.A","Canada")
    w.grid(row=3,column=2)
    #Sign In
    def signup():
                 def success():
                    user = user_name.get()
                    cur.execute("select user_name from airlines where user_name=(?)", (user,))
                    a = cur.fetchall()
                    if user=="":
                        showerror('Error',"User name required")
                    elif passw.get()=="":
                        showerror('Error',"Password required")
                    elif a != []:
                          showerror('Error',"Username Already Exists")
                    else:
                          l = (user_name.get(), first_name.get(), last_name.get(),phone_number.get(),email.get(), passw.get())
                          cur.execute("insert into airlines values(?,?,?,?,?,?)",l)
                          showinfo('Signed Up',"Congratulation You are Successfully Signed Up")
                          con.commit()
                          user_name.delete(0,20)
                          first_name.delete(0,20)
                          last_name.delete(0,20)
                          phone_number.delete(0,10)
                          email.delete(0,30)
                          passw.delete(0,20)
                 root1.destroy()
                 root=Tk()
                 root.title("Sign Up")
                 root.state('zoomed')
                 d=PhotoImage(file="aeroplane2.gif")
                 Label(root,image=d).grid(row=0,column=0,columnspan=4,ipadx=450)
                 Label(root,text="Welcome to Envy Airlines",font=("times new roman",17),fg="Black",width=46,bg="White").grid(row=0,column=0,columnspan=4)
                 Label(root,text="SIGN UP",font=("times new roman",17,"bold"),fg="White",width=46,bg="blue").grid(row=1,column=0,columnspan=4,pady=10)
                 Label(root,text="Username*:",font=("times new roman",14),fg="Black").grid(row=2,column=1)
                 user_name=Entry(width=30)
                 user_name.grid(row=2,column=2)
                 Label(root,text="First Name:",font=("times new roman",14),fg="Black").grid(row=3,column=1)
                 first_name=Entry(width=30)
                 first_name.grid(row=3,column=2)
                 Label(root,text="Last Name:",font=("times new roman",14),fg="Black").grid(row=4,column=1)
                 last_name=Entry(width=30)
                 last_name.grid(row=4,column=2)
                 Label(root,text="Phone Number:",font=("times new roman",14),fg="Black").grid(row=5,column=1)
                 phone_number=Entry(width=30)
                 phone_number.grid(row=5,column=2)
                 Label(root,text="Email:",font=("times new roman",14),fg="Black").grid(row=6,column=1)
                 email=Entry(width=30)
                 email.grid(row=6,column=2)
                 Label(root,text="Password*:",font=("times new roman",14),fg="Black").grid(row=7,column=1)
                 passw=Entry(root,show="*",width=30)
                 passw.grid(row=7,column=2)   
                 Button(root,text="Sign Up",fg="white",bg="blue",font=("times",14),command=lambda: success()).grid(row=8,columnspan=4,ipadx=150,pady=20)
                 def signin():
                     root.destroy()
                     root2=Tk()
                     root2.title("Sign In")
                     root2.state('zoomed')
                     b=PhotoImage(file="aeroplane2.gif")
                     Label(root2,image=b).grid(row=0,column=0,columnspan=4,ipadx=450)
                     Label(root2,text="Welcome to Envy Airlines",font=("times new roman",17),fg="Black",width=46,bg="White").grid(row=0,column=0,columnspan=4)
                     Label(root2,text="Sign In",font=("times new roman",17),fg="White",width=46,bg="green").grid(row=1,column=0,columnspan=4,pady=10)
                     Label(root2,text="Username*:",font=("times new roman",14),fg="Black").grid(row=2,column=1)
                     user_name=Entry(width=30)
                     user_name.grid(row=2,column=2)
                     Label(root2,text="Password*:",font=("times new roman",14),fg="Black").grid(row=3,column=1)
                     passw=Entry(root2,show="*",width=30)
                     passw.grid(row=3,column=2)
                     def bookingportal():
                          usr = user_name.get()
                          passs = passw.get()
                          cur.execute("select * from airlines where user_name=(?) and passw=(?)", (usr, passs,))
                          a = cur.fetchall()
                          if usr=="":
                                showerror('Error',"Please enter the user name")
                          elif passs=="":
                                showerror('Error',"Please enter the password")
                          elif a==[]:
                                   showerror('Log In Failed', "Invalid Username or Password")
                          else:
                                root2.destroy()
                                root4=Tk()
                                root4.title("Booking Portal")
                                root4.state('zoomed')
                                Label(root4,text="Welcome to Envy Airlines:",font=("times new roman",17),fg="Black",width=46,bg="White").grid(row=0,column=0,columnspan=4,ipadx=450)
                                Label(root4,text="Booking Portal:",font=("times new roman",17),fg="White",width=46,bg="red").grid(row=1,column=0,columnspan=4,pady=20)
                                Label(root4,text="Enter Your Details:",font=("times new roman",14),fg="Black",width=46).grid(row=2,column=0,columnspan=4)
                                Label(root4,text="Full Name:",font=("times new roman",14),fg="Black").grid(row=3,column=1)
                                name=Entry(width=30)
                                name.grid(row=3,column=2)
                                Label(root4,text="Enter Your age:",font=("times new roman",14),fg="Black").grid(row=4,column=1)
                                age=Entry(width=6)
                                age.grid(row=4,column=2)
                                Label(root4,text="Select Gender:",font=("times new roman",14),fg="Black").grid(row=5,column=1)
                                a=IntVar()
                                Radiobutton(root4,text="Male",variable=a,value=0,fg="black").grid(row=5,column=2)
                                Radiobutton(root4,text="Female",variable=a,value=1,fg="black").grid(row=5,column=2,columnspan=2)
                                Label(root4,text="Seat Class:",font=("times new roman",14),fg="Black").grid(row=6,column=1)
                                v= StringVar(root4)
                                v.set("Select class") # default value
                                w = OptionMenu(root4, v, "First Class", "Business Class", "Economy Class")
                                w.grid(row=6,column=2)
                                Label(root4,text="Additional Passengers Details:",font=("times new roman",14),fg="Black",width=46).grid(row=7,column=0,columnspan=4)
                                Label(root4,text="Passenger1",font=("times new roman",14),fg="Black").grid(row=8,column=1)
                                name1=Entry(width=30)
                                name1.grid(row=8,column=2)
                                Label(root4,text="Enter Your age:",font=("times new roman",14),fg="Black").grid(row=9,column=1)
                                age1=Entry(width=6)
                                age1.grid(row=9,column=2)
                                Label(root4,text="Seat Class:",font=("times new roman",14),fg="Black").grid(row=10,column=1)
                                v1= StringVar(root4)
                                v1.set("Select class") # default value
                                w1 = OptionMenu(root4, v1, "First Class", "Business Class", "Economy Class")
                                w1.grid(row=10,column=2)
                                Label(root4,text="Passenger2",font=("times new roman",14),fg="Black").grid(row=11,column=1)
                                name2=Entry(width=30)
                                name2.grid(row=11,column=2)
                                Label(root4,text="Enter Your age:",font=("times new roman",14),fg="Black").grid(row=12,column=1)
                                age2=Entry(width=6)
                                age2.grid(row=12,column=2)
                                Label(root4,text="Seat Class:",font=("times new roman",14),fg="Black").grid(row=13,column=1)
                                v2= StringVar(root4)
                                v2.set("Select class") # default value
                                w2 = OptionMenu(root4, v2, "First Class", "Business Class", "Economy Class")
                                w2.grid(row=13,column=2)
                                Label(root4,text="Passenger3",font=("times new roman",14),fg="Black").grid(row=14,column=1)
                                name3=Entry(width=30)
                                name3.grid(row=14,column=2)
                                Label(root4,text="Enter Your age:",font=("times new roman",14),fg="Black").grid(row=15,column=1)
                                age3=Entry(width=6)
                                age3.grid(row=15,column=2)
                                Label(root4,text="Seat Class:",font=("times new roman",14),fg="Black").grid(row=16,column=1)
                                v3= StringVar(root4)
                                v3.set("Select class") # default value
                                w3 = OptionMenu(root4, v3, "First Class", "Business Class", "Economy Class")
                                w3.grid(row=16,column=2)
                                Label(root4, text="Journey Date:",font=("times new roman",14),fg="Black").grid(row=17,column=1)
                                date1 = Entry(root4, width=15, font=("times new roman", 14),fg="Black")
                                date1.grid(row=17, column=2)
                                date1.insert(0,"YYYY-MM-DD")
                                Label(root4,text="Number of Passengers",font=("times new roman",14),fg="Black").grid(row=18,column=1)
                                v4= StringVar(root4)
                                v4.set("0") # default value
                                w4 = OptionMenu(root4, v4, "1", "2", "3","4")
                                w4.grid(row=18,column=2)
                                def data():
                                        root5=Tk()
                                        root5.title("Ticket Details")
                                        root5.state('zoomed')
                                        root5.configure(bg='white')
                                        Label(root5,text="Thanks For Choosing Envy Airlines",font=("times new roman",17),fg="White",bg="black",width=46).grid(row=0,column=0,columnspan=4,ipadx=450,pady=20)
                                        Label(root5,text="Ticket Details",font=("times new roman",17),fg="Black",width=46,bg="white").grid(row=1,column=0,columnspan=4)
                                        Label(root5,text="Passenger Name",font=("Arial",14),fg="Black",bg="white").grid(row=2,column=1)
                                        Label(root5,text=name.get(),font=("Arial",14),fg="Black",bg="white").grid(row=2,column=2)
                                        Label(root5,text="Age",font=("Arial",14),fg="Black",bg="white").grid(row=3,column=1)
                                        Label(root5,text=age.get(),font=("Arial",14),fg="Black",bg="white").grid(row=3,column=2)
                                        Label(root5,text="Gender",font=("Arial",14),fg="Black",bg="white").grid(row=4,column=1)
                                        if(a.get()==0):
                                                Label(root5,text="Male",font=("Arial",14),fg="Black",bg="white").grid(row=4,column=2)
                                        else:
                                                Label(root5,text="Female",font=("Arial",14),fg="Black",bg="white").grid(row=4,column=2)
                                        Label(root5,text="Class",font=("Arial",14),fg="Black",bg="white").grid(row=5,column=1)
                                        Label(root5,text=v.get(),font=("Arial",14),fg="Black",bg="white").grid(row=5,column=2)
                                        Label(root5,text="Date",font=("Arial",14),fg="Black",bg="white").grid(row=6,column=1)
                                        Label(root5,text=date1.get(),font=("Arial",14),fg="Black",bg="white").grid(row=6,column=2)
                                        Label(root5,text="Additional Passenger Details",font=("times new roman",17),fg="Black",width=46,bg="white").grid(row=7,column=0,columnspan=4)
                                        if int(v4.get()) > 1:
                                            Label(root5,text="Passenger Name",font=("Arial",14),fg="Black",bg="white").grid(row=8,column=1)
                                            Label(root5,text=name1.get(),font=("Arial",14),fg="Black",bg="white").grid(row=8,column=2)
                                            Label(root5,text="Class",font=("Arial",14),fg="Black",bg="white").grid(row=9,column=1)
                                            Label(root5,text=v1.get(),font=("Arial",14),fg="Black",bg="white").grid(row=9,column=2)
                                        if int(v4.get()) > 2:
                                            Label(root5,text="Passenger Name",font=("Arial",14),fg="Black",bg="white").grid(row=10,column=1)
                                            Label(root5,text=name2.get(),font=("Arial",14),fg="Black",bg="white").grid(row=10,column=2)
                                            Label(root5,text="Class",font=("Arial",14),fg="Black",bg="white").grid(row=11,column=1)
                                            Label(root5,text=v2.get(),font=("Arial",14),fg="Black",bg="white").grid(row=11,column=2)
                                        if int(v4.get()) > 3:
                                            Label(root5,text="Passenger Name",font=("Arial",14),fg="Black",bg="white").grid(row=12,column=1)
                                            Label(root5,text=name3.get(),font=("Arial",14),fg="Black",bg="white").grid(row=12,column=2)
                                            Label(root5,text="Class",font=("Arial",14),fg="Black",bg="white").grid(row=13,column=1)
                                            Label(root5,text=v3.get(),font=("Arial",14),fg="Black",bg="white").grid(row=13,column=2)
                                        Label(root5,text="Amount Per Passsenger",font=("times new roman",17),fg="Black",width=46,bg="white").grid(row=14,column=0,columnspan=4)
                                        Label(root5,text="Ticket From " + variable.get() + "<-> to <->" + variable1.get(),fg="White",bg="green",font=("LCD",10),width=46).grid(row=15,column=0,columnspan=4,pady=5)
                                        def amount(price):
                                                global amount_p
                                                if (int(v4.get())==1):
                                                     if(v.get()=="First Class"):
                                                        price=10000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black",bg="white").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                        
                                                     elif (v.get()=="Business Class"):
                                                        price=6000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                     elif(v.get()=="Econoy Class"):
                                                        price=3800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                elif int(v4.get())==2:
                                                    if(v.get()=="First Class" and v1.get()=="First Class"):
                                                        price=20000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class"):
                                                        price=16000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class"):
                                                        price=13800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class"):
                                                        price=16000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class"):
                                                        price=12000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class"):
                                                        price=9800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class"):
                                                        price=13800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class"):
                                                        price=9800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class"):
                                                        price=7600
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                elif (int(v4.get())==3):
                                                    if(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                        price=30000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                        price=26000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                        price=23800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                        price=30000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                        price=26000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                         price=23800
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                        price=30000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                        price=26000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                         price=23800
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                        price=26000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                        price=22000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                         price=19800
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                        price=22000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                         price=18000
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                         price=15800
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                         price=19800
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                        price=15800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                         price=13600
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                        price=23800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                        price=19800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                         price=17600
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                        price=19800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                        price=15800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                         price=13600
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                        price=17600
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                        price=13600
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                         price=11400
                                                         Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)

                                                         amount_p=price*int(v4.get())
                                                elif (int(v4.get())==4):
                                                    if(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                        Label(root5,text="Price",font=("Arial",14),fg="Black").grid(row=16,column=1)
                                                        Label(root5,text=price,font=("Arial",14),fg="Black",bg="white").grid(row=16,column=2)
                                                        Label(root5,text="Total Amount",font=("Arial",14),fg="Black",bg="white").grid(row=18,column=1)
                                                        Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Black",bg="white").grid(row=18,column=2)
                                                        amount_p=price*int(v4.get())
                                                
                                        amount(0)
                                        Label(root5,text="Number of Passengers",font=("Arial",14),fg="Black").grid(row=17,column=1)
                                        Label(root5,text=v4.get(),font=("Arial",14),fg="Black").grid(row=17,column=2)
                                        l1 = (name.get(), date1.get(), v4.get(), amount_p, variable.get(), variable1.get() )
                                        cur.execute("insert into booking(name,date,no_of_pas,amount,source,destination) values(?,?,?,?,?,?)",l1)
                                        con.commit()
                                        def exitw():
                                            root4.destroy()
                                            root5.destroy()
                                        Button(root5,text="Done",font=("times"),fg="white",bg="black",command=exitw).grid(row=19,columnspan=5,ipadx=100,pady=10)
                                        #Button(root5,text="Price",font=("times"),fg="white",bg="white",command=amount(0)).grid(row=20,columnspan=5,ipadx=100)
                          Button(root4,text="Confirm Booking",fg="white",font=("times"),bg="red",command=data).grid(row=19,columnspan=5,ipadx=100,pady=20)
                     Button(root2,text="Sign In",fg="white",bg="green",font=("times",14),command=lambda: bookingportal()).grid(row=4,columnspan=5,ipadx=100,pady=20)
                     asd#Error for displaying the image
                 Button(root,text="Sign in",fg="white",bg="green",font=("times",14),command=signin).grid(row=9,columnspan=5,ipadx=100,pady=20)
                 asd#Error For Displaying the Images
     #Flights Availability
    def books():
        root9=Tk()
        root9.title("Ticket Details")
        root9.state('zoomed')
        root9.configure(bg='white')
        Label(root9,text="Booking details:",font=("times new roman",17),fg="black",bg="white").grid(row=0,column=0)
        Label(root9, text="Start Date:",font=("times new roman",14),fg="Black",bg="white").grid(row=1,column=1)
        date11 = Entry(root9, width=17, font=("times new roman", 14),fg="Black")
        date11.grid(row=1, column=2)
        date11.insert(0,"YYYY-MM-DD")
        Label(root9, text="End Date:",font=("times new roman",14),fg="Black",bg="white").grid(row=1,column=3)
        date12 = Entry(root9, width=17, font=("times new roman", 14),fg="black",bg="white")
        date12.grid(row=1, column=4)
        date12.insert(0,"YYYY-MM-DD")
        def Filter():
            root8=Tk()
            root8.title("Ticket Details")
            root8.state('zoomed')
            root8.configure(bg='white')
            Label(root8,text="Booking details:",font=("times new roman",17),fg="black",bg="white").grid(row=0,column=0)
            Label(root8, text="Start Date:",font=("times new roman",14),fg="Black",bg="white").grid(row=1,column=1)
            date5 = Entry(root8, width=17, font=("times new roman", 14),fg="Black")
            date5.grid(row=1, column=2)
            startd=date11.get()
            date5.insert(0,date11.get())
            Label(root8, text="End Date:",font=("times new roman",14),fg="Black",bg="white").grid(row=1,column=3)
            date6 = Entry(root8, width=17, font=("times new roman", 14),fg="black",bg="white")
            date6.grid(row=1, column=4)
            endd=date12.get()
            date6.insert(0,date12.get())
            Label(root8,text="ID",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=1)
            Label(root8,text="Name",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=2,pady=10)
            Label(root8,text="Date",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=3,pady=10)
            Label(root8,text="Total Passengers",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=4,pady=10)
            Label(root8,text="Amount",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=5,pady=10)
            Label(root8,text="Source",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=6,pady=10)
            Label(root8,text="Destination",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=7,pady=10)
            cur.execute("select * from booking")
            a12 = cur.fetchall()
            i=3
            d1 = datetime.datetime(int(startd[:4]), int(startd[5:7]), int(startd[8:10])) 
            d2 = datetime.datetime(int(endd[:4]), int(endd[5:7]), int(endd[8:10])) 
            for j in a12:
                giv=datetime.datetime(int(j[2][:4]), int(j[2][5:7]), int(j[2][8:10]))
                if (d1<=giv and d2>=giv):
                    Label(root8,text=j[0],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=1)
                    Label(root8,text=j[1],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=2)
                    Label(root8,text=j[2],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=3)
                    Label(root8,text=j[3],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=4)
                    Label(root8,text=j[4],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=5)
                    Label(root8,text=j[5],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=6)
                    Label(root8,text=j[6],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=7)
                    i=i+1
        Button(root9,text="Filter",fg="white",font=("times"),bg="dark blue",command=Filter).grid(row=1,column=5,ipadx=50)
        Label(root9,text="ID",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=1)
        Label(root9,text="Name",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=2,pady=10)
        Label(root9,text="Date",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=3,pady=10)
        Label(root9,text="Total Passengers",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=4,pady=10)
        Label(root9,text="Amount",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=5,pady=10)
        Label(root9,text="Source",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=6,pady=10)
        Label(root9,text="Destination",font=("times new roman",14),fg="white",bg="black",width=17).grid(row=2,column=7,pady=10)
        cur.execute("select * from booking")
        a11 = cur.fetchall()
        i=3
        for j in a11:
            Label(root9,text=j[0],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=1)
            Label(root9,text=j[1],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=2)
            Label(root9,text=j[2],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=3)
            Label(root9,text=j[3],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=4)
            Label(root9,text=j[4],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=5)
            Label(root9,text=j[5],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=6)
            Label(root9,text=j[6],font=("times new roman",12),fg="black",bg="white",width=17).grid(row=i,column=7)
            i=i+1
    def flights():
        if variable.get()=="Delhi" and variable1.get()=="Kolkata":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="100",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Delhi" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="250",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Delhi" and variable1.get()=="U.S.A":
            showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="Delhi" and variable1.get()=="Canada":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="201",font=("times new roman",14),fg="white",bg="green").grid(row=4,columnspan=5,column=2)
        if variable.get()=="Kolkata" and variable1.get()=="Delhi":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="100",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Kolkata" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="150",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Kolkata" and variable1.get()=="U.S.A":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="115",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Kolkata" and variable1.get()=="Canada":
            showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="Mumbai" and variable1.get()=="Delhi":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="250",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Mumbai" and variable1.get()=="Kolkata":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="150",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Mumbai" and variable1.get()=="U.S.A":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="167",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Mumbai" and variable1.get()=="Canada":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="160",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="U.S.A" and variable1.get()=="Delhi":
            showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="U.S.A" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="167",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="U.S.A" and variable1.get()=="Kolkata":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="115",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="U.S.A" and variable1.get()=="Canada":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="168",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Canada" and variable1.get()=="Delhi":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="201",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Canada" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="160",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        if variable.get()=="Canada" and variable1.get()=="Kolkata":
           showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="Canada" and variable1.get()=="U.S.A":
            Label(root1,text="Number of Seats Available are:",font=("times new roman",14),fg="black").grid(row=5,columnspan=4,pady=20)
            Label(root1,text="168",font=("times new roman",14),fg="white",bg="green").grid(row=5,columnspan=3,column=1)
        Button(root1,text="Signup to Book",fg="white",bg="black",font=("time",10),command=signup).grid(row=8,columnspan=5,pady=10,ipadx=100,ipady=10)  
    Button(root1,text="Show Seat Availability",font=("times",12),fg="white",bg="black",compound="center",command=flights).grid(row=6,columnspan=5,ipadx=100,pady=20)
    Button(root1,text="Check Bookings",font=("times",12),fg="white",bg="black",compound="center",command=books).grid(row=7,columnspan=5,ipadx=100,pady=20)
    root1.mainloop()
Button(fr2,text="Proceed to Project",compound="center",bg="black",font=("times"),fg="white",command=airline).pack()
root.mainloop()
