from tkinter import *
from tkinter import messagebox
from tkinter import font
import pymysql
from urllib.request import FancyURLopener

top=Tk()
top.geometry("1000x700")
top.title("complaint_management\python")
C = Canvas(top,bg="red", height=700, width=1000)
filename = PhotoImage(file = "Capture1.png")
image = C.create_image(500,353,image=filename)
C.place(x=0,y=0)

def ok1():
    def ok2():
        def ok3(b):
            def ok4():
                root4=Tk()
                root4.geometry("1000x700")
                root4.title("complaint_management\python")
                root3.destroy()
                
                def back1():
                    root4.destroy()
                    ok3(b)
                def func1():
                    sql="INSERT INTO complaints(comp_heading, comp_detail, cid)VALUES ('"+e5.get()+"', '"+t1.get("1.0",END)+"', '"+b+"' )"
                    msg=messagebox.askyesno("cms","Are you sure to register your complain? If you want to check your details once again then press NO.")
                    if msg:
                        db = pymysql.connect("localhost","root","","cms")
                        c=db.cursor()
                        c.execute(sql)
                        db.commit()
                        db.close()
                        msg=messagebox.askokcancel("cms","You have successfully registered your complain. Your complain will be solved as soon as possible and you will be notified on registered mobile no.")
                        if msg:
                            root4.destroy()
                            ok3(b)
                    else:
                        pass
                C = Canvas(root4,bg="deeppink1", height=700, width=1000)
                C.place(x=0,y=0)
                back=Button(root4,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
                back.place(x=10,y=10)
                l4=Label(root4,text="COMPLAINT SUBMISSION FORM ",font=helv35)
                l4.place(x=330,y=30)
                l5=Label(root4,text="Subject : ",font=helv36,bg="deeppink1")
                l5.place(x=120,y=150)
                e5=Entry(root4,bd=4,width=50,selectborderwidth=60,font=helv33)
                e5.place(x=250,y=150)
                l6=Label(root4,text="Complaint : ",font=helv36,bg="deeppink1")
                l6.place(x=120,y=255)
                t1=Text(root4,width=50,height=9,font=helv34,bd=4)
                t1.place(x=250,y=255)
                b1=Button(root4,text="Register ",width=12,height=1,bg="#00ff00",font=helv36,relief=RAISED,bd=10,command=func1)
                b1.place(x=650,y=550)
                
            root3=Tk()
            root3.geometry("1000x700")
            
            root3.title("complaint_management\python")
            try:
                root2.destroy()
            except:
                pass
            def back1():
                root3.destroy()
                ok1()
            def hm():
                sql="SELECT cid FROM complaints "
                sql1="SELECT comp_detail FROM complaints WHERE cid='"+b+"' "
                sql2="SELECT solution FROM complaints WHERE cid='"+b+"' "
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql)
                result = c.fetchall()
                DL=[]
                for i in result:
                    DL.append(i[0])
                        
                if b in DL:
                    root8=Tk()
                    root8.geometry("1000x700")
                    root8.title("complaint_management\python")
                    root3.destroy()
                    def back1():
                        root8.destroy()
                        ok3(b)
                    C = Canvas(root8,bg="deeppink1", height=700, width=1000)
                    C.place(x=0,y=0)
                    back=Button(root8,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
                    back.place(x=10,y=10)
                    l1=Label(root8,text="YOUR COMPLAINT REGISTERED INFORMATION ",font=helv35,bg="dodgerblue")
                    l1.place(x=250,y=10)
                    l2=Label(root8,text="Your Complaint : ",font=helv36,bg="deeppink1")
                    l2.place(x=200,y=90)
                    t1=Text(root8,width=30,height=20,font=helv34,bd=5,bg="burlywood2")
                    t1.place(x=100,y=140)
                    l3=Label(root8,text="Your Solution : ",font=helv36,bg="deeppink1")
                    l3.place(x=650,y=90)
                    t2=Text(root8,width=30,height=20,font=helv34,bd=5,bg="burlywood2")
                    t2.place(x=560,y=140)

                    c.execute(sql1)
                    result1 = c.fetchall()
                    DL1=[]
                    for i in result1:
                        DL1.append(i[0]+"\n")
                    c.execute(sql2)
                    result2 = c.fetchall()
                    DL2=[]
                    for i in result2:
                        DL2.append(i[0]+"\n")
                    for i in range(0,len(DL1)):
                        m=str(str(i+1)+".  ")
                        t1.insert(INSERT,m)
                        t1.insert(END,DL1[i])
                        t2.insert(INSERT,m)      
                        t2.insert(END,DL2[i])

                else:
                    msg=messagebox.askokcancel("cms","You have not registered any complain till now. Kindly register first then check for registered complains.")
                    if msg:
                        ok4()
                    else:
                        pass
            C = Canvas(root3,bg="deeppink1", height=700, width=1000)
            C.place(x=0,y=0)
            back=Button(root3,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
            back.place(x=10,y=10)
            b1=Button(root3,text="NEW\n COMPLAINT ",width=20,height=4,bg="dodgerblue",font=helv36,command=ok4,relief=RAISED,bd=10)
            b1.place(x=380,y=180)
            b2=Button(root3,text="REGISTERED\n COMPLAINT ",width=20,height=4,bg="dodgerblue",font=helv36,relief=RAISED,bd=10,command=hm)
            b2.place(x=380,y=380)
            
        root2=Tk()
        root2.geometry("1000x700")
        root2.title("complaint_management\python")
        try:
            root1.destroy()
        except:
            pass
        C=Canvas(root2,bg="deeppink1", height=700, width=1000)
        C.place(x=0,y=0)
        def back1():
            root2.destroy()
        def func4():
            a=e6.get()
            sql1= "SELECT email FROM customer_register"
            sql= "SELECT cpassword FROM customer_register"
            msg=messagebox.askyesno("cms","Are you sure to login? If you want to check your details once again then press NO.")
            if msg:
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result = c.fetchall()
                DL=[]
                for i in result:
                    DL.append(i[0])
                    
                if e6.get() in DL:
                    c.execute(sql)
                    result = c.fetchall()
                    DL1=[]
                    for i in result:
                        DL1.append(i[0])
                    if e7.get() in DL1:
                        db.commit()
                        db.close()
                        msg3=messagebox.askokcancel("cms","You have successfully login.")
                        ok3(a)
                    else:
                        msg1=messagebox.askokcancel("cms","Please enter valid email id or password.")
                        if msg1:
                            pass
                else:    
                    msg2=messagebox.askokcancel("cms","Please enter valid email id or password.")
                    if msg2:
                        pass       
            else:
                pass
        back=Button(root2,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
        back.place(x=10,y=10)
        l2=Label(root2,text="Login Id : ",font=helv36,bg="deeppink1")
        l2.place(x=180,y=200)
        e6=Entry(root2,bd=4,width=40,selectborderwidth=60,font=helv33)
        e6.place(x=330,y=200)
        l3=Label(root2,text="Password : ",font=helv36,bg="deeppink1")
        l3.place(x=180,y=260)
        e7=Entry(root2,bd=4,width=40,selectborderwidth=60,font=helv33,show="*")
        e7.place(x=330,y=260)
        b1=Button(root2,text="LOGIN",width=10,height=2,bg="#00ff00",font=helv35,command=func4,relief=RAISED,bd=10)
        b1.place(x=500,y=400)

    def ok5():
        root5=Tk()
        root5.geometry("1000x700")
        root5.title("complaint_management\python")
        root1.destroy()
        def back1():
            root5.destroy()
            ok1()
        def func():
            #call vars
            sql="INSERT INTO customer_register(cname, cpassword, email, mobile)VALUES ('"+e1.get()+"', '"+e4.get()+"', '"+e2.get()+"', '"+str(e3.get())+"' )"
            sql1= "SELECT email FROM customer_register" 
            msg=messagebox.askyesno("cms","Are you sure to register? If you want to check your details once again then press NO.")
            if msg:
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result = c.fetchall()
                DL=[]
                for i in result:
                    DL.append(i[0])
                    
                if e2.get() in DL:
                    msg1=messagebox.askokcancel("cms","This email is already exists. Please login or try with another email")
                else:    
                    c.execute(sql)
                    db.commit()
                    root5.destroy()
                    ok2()
                db.close()
                    
            else:
                pass
        C = Canvas(root5,bg="deeppink1", height=700, width=1000)
        C.place(x=0,y=0)
        
        l5=Label(root5,text="REGISTRATION FORM ",font=helv35,width=95,bg="dodgerblue",height=5)
        l5.place(x=0,y=0)
        back=Button(root5,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
        back.place(x=10,y=10)
        l1=Label(root5,text="Name : ",font=helv36,bg="deeppink1")
        l1.place(x=150,y=200)
        e1=Entry(root5,bd=4,width=40,selectborderwidth=60,font=helv33)
        e1.place(x=290,y=200)
        l2=Label(root5,text="Email : ",font=helv36,bg="deeppink1")
        l2.place(x=150,y=250)
        e2=Entry(root5,bd=4,width=40,selectborderwidth=60,font=helv33)
        e2.place(x=290,y=250)
        l3=Label(root5,text="Mobile no. : ",font=helv36,bg="deeppink1")
        l3.place(x=150,y=300)
        e3=Entry(root5,bd=4,width=40,selectborderwidth=60,font=helv33)
        e3.place(x=290,y=300)
        l4=Label(root5,text="Password : ",font=helv36,bg="deeppink1")
        l4.place(x=150,y=350)
        e4=Entry(root5,bd=4,width=40,selectborderwidth=60,font=helv33,show="*")
        e4.place(x=290,y=350)
        b1=Button(root5,text="REGISTER",width=10,height=2,bg="#00ff00",font=helv35,relief=RAISED,bd=10,command=func)
        b1.place(x=450,y=450)

    
    root1=Tk()
    root1.geometry("1000x700")
    root1.title("complaint_management\python")
    def back1():
        root1.destroy()
    C = Canvas(root1,bg="deeppink1", height=700, width=1000)
    C.place(x=0,y=0)
    back=Button(root1,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
    back.place(x=10,y=10)
    b1=Button(root1,text="REGISTERED\n CUSTOMER ",width=20,height=4,bg="dodgerblue",font=helv36,command=ok2,relief=RAISED,bd=10)
    b1.place(x=380,y=180)
    b2=Button(root1,text="NEW\n CUSTOMER ",width=20,height=4,bg="dodgerblue",font=helv36,command=ok5,relief=RAISED,bd=10)
    b2.place(x=380,y=380)
    
def ach():
    def ach1():
        def ach3():
            root3=Tk()
            root3.geometry("1000x700")
            root3.title("complaint_management\python")
            try:
                root2.destroy()
            except:
                pass
            def back1():
                root3.destroy()
                ach()
            def man1():
                root9=Tk()
                root9.geometry("1000x700")
                root9.title("complaint_management\python")
                root3.destroy()
                def back1():
                    root9.destroy()
                    ach3()
                def ach4():
                    f=(var.get())
                    k=str(DL2[f])
                    print(f)
                    print(k)
                    sql="INSERT INTO manager_comp(cid, tp_id, comp_heading)VALUES ('"+e11.get()+"', '"+e13.get()+"', '"+k+"' )"
                    sql1="UPDATE complaints SET tpid ='"+e13.get()+"' WHERE cid = '"+e11.get()+"' AND comp_heading = '"+k+"' "
                    db = pymysql.connect("localhost","root","","cms")
                    c=db.cursor()
                    c.execute(sql)
                    c.execute(sql1)
                    db.commit()
                    man1()
                C = Canvas(root9,bg="deeppink1", height=700, width=1000)
                C.place(x=0,y=0)
                back=Button(root9,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
                back.place(x=10,y=10)
                l1=Label(root9,text="LIST OF UNSOLVED COMPLAINS ",font=helv35,bg="dodgerblue")
                l1.place(x=310,y=10)
                l2=Label(root9,text="Customer Id : ",font=helv36,bg="deeppink1")
                l2.place(x=200,y=70)
                t5=Text(root9,width=30,height=15,font=helv34,bd=4,bg="burlywood2")
                t5.place(x=110,y=120)
                l3=Label(root9,text="Complaints : ",font=helv36,bg="deeppink1")
                l3.place(x=600,y=70)
                t6=Text(root9,width=30,height=15,font=helv34,bd=4,bg="burlywood2")
                t6.place(x=510,y=120)
                l4=Label(root9,text="Customer id :",font=helv36,bg="deeppink1")
                l4.place(x=200,y=500)
                e11=Entry(root9,bd=4,width=28,selectborderwidth=60,font=helv33)
                e11.place(x=132,y=560)
                l5=Label(root9,text="Cno.  ",font=helv36,bg="deeppink1")
                l5.place(x=50,y=500)
                var=IntVar()
                s=Spinbox(root9,bd=4,width=2,font=helv33,from_=0,to=20,textvariable=var)
                s.place(x=50,y=560)
                l6=Label(root9,text="Assign to :  ",font=helv36,bg="deeppink1")
                l6.place(x=600,y=500)
                e13=Entry(root9,bd=4,width=28,selectborderwidth=60,font=helv33)
                e13.place(x=500,y=560)
                b1=Button(root9,text="SUBMIT",width=8,height=0,bg="#00ff00",font=helv35,relief=RAISED,bd=8,command=ach4)
                b1.place(x=850,y=550)
                g="NP"
                sql1="SELECT cid FROM complaints WHERE tpid = '"+g+"'"
                sql2="SELECT comp_heading FROM complaints WHERE tpid = '"+g+"'"
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result1 = c.fetchall()
                DL1=[]
                for i in result1:
                    DL1.append(i[0]+"\n")
 
                c.execute(sql2)
                result2 = c.fetchall()
                DL2=[]
                for i in result2:
                    DL2.append(i[0])
                j=1.0
                for i in range(0,len(DL1)):
                    m=str(str(i+1)+".  ")
                    t5.insert(INSERT,m)
                    t5.insert(END,DL1[i])
                    t6.insert(j,m)
                    j=j+1
                    t6.insert(j,DL2[i])
                    j=j+2
                    t6.insert(j,"\n")
    

            def man2():
                root9=Tk()
                root9.geometry("1000x700")
                root9.title("complaint_management\python")
                root3.destroy()
                def back1():
                    root9.destroy()
                    ach3()
                C = Canvas(root9,bg="deeppink1", height=700, width=1000)
                C.place(x=0,y=0)
                back=Button(root9,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
                back.place(x=10,y=10)
                l1=Label(root9,text="LIST OF SOLVED COMPLAINS ",font=helv35,bg="dodgerblue")
                l1.place(x=300,y=10)
                l2=Label(root9,text="Customer Id : ",font=helv36,bg="deeppink1")
                l2.place(x=120,y=90)
                t7=Text(root9,width=25,height=20,font=helv34,bd=4,bg="burlywood2")
                t7.place(x=50,y=140)
                l3=Label(root9,text="TechPerson Id : ",font=helv36,bg="deeppink1")
                l3.place(x=410,y=90)
                t8=Text(root9,width=25,height=20,font=helv34,bd=4,bg="burlywood2")
                t8.place(x=350,y=140)
                l4=Label(root9,text="Complaints : ",font=helv36,bg="deeppink1")
                l4.place(x=740,y=90)
                t9=Text(root9,width=25,height=20,font=helv34,bd=4,bg="burlywood2")
                t9.place(x=650,y=140)
                
                sql1="SELECT cid FROM manager_comp"
                sql2="SELECT comp_heading FROM manager_comp"
                sql3="SELECT tp_id FROM manager_comp"
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result1 = c.fetchall()
                DL1=[]
                for i in result1:
                    DL1.append(i[0]+"\n")
                c.execute(sql2)
                result2 = c.fetchall()
                DL2=[]
                for i in result2:
                    DL2.append(i[0])
                c.execute(sql3)
                result3 = c.fetchall()
                DL3=[]
                for i in result3:
                    DL3.append(i[0]+"\n")
                j=1.0
                for i in range(0,len(DL1)):
                    m=str(str(i+1)+".  ")
                    t7.insert(INSERT,m)
                    t7.insert(END,DL1[i])
                    t8.insert(INSERT,m)
                    t8.insert(END,DL3[i])
                    t9.insert(j,m)
                    j=j+1
                    t9.insert(j,DL2[i])
                    j=j+1
                    t9.insert(j,"\n")
                    
                   
                
                db.close()
                
            C = Canvas(root3,bg="deeppink1", height=700, width=1000)
            C.place(x=0,y=0)
            back=Button(root3,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
            back.place(x=10,y=10)
            b1=Button(root3,text="UNSOLVED\n COMPLAINS ",width=20,height=4,bg="dodgerblue",font=helv36,relief=RAISED,bd=10,command=man1)
            b1.place(x=380,y=180)
            b2=Button(root3,text="SOLVED\n COMPLAINS ",width=20,height=4,bg="dodgerblue",font=helv36,relief=RAISED,command=man2,bd=10)
            b2.place(x=380,y=380)
        root2=Tk()
        root2.geometry("1000x700")
        root2.title("complaint_management\python")
        root1.destroy()
        def back1():
            root2.destroy()
            ach()
        def func2():
            sql1= "SELECT email FROM manager"
            sql= "SELECT mpassword FROM manager"
            msg=messagebox.askyesno("cms","Are you sure to login? If you want to check your details once again then press NO.")
            if msg:
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result = c.fetchall()
                DL=[]
                for i in result:
                    DL.append(i[0])    
                if e7.get() in DL:
                    c.execute(sql)
                    result1 = c.fetchall()
                    DL1=[]
                    for i in result1:
                        DL1.append(i[0])
                    if e8.get() in DL1:
                        db.commit()
                        db.close()
                        msg3=messagebox.askokcancel("cms","You have successfully login.")
                        ach3()
                    else:
                        msg1=messagebox.askokcancel("cms","Please enter valid email id or password.")
                        if msg1:
                            pass
                else:    
                    msg2=messagebox.askokcancel("cms","Please enter valid email id or password.")
                    if msg2:
                        pass       
            else:
                pass
            
        C = Canvas(root2,bg="deeppink1", height=700, width=1000)
        C.place(x=0,y=0)
        back=Button(root2,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
        back.place(x=10,y=10)
        l2=Label(root2,text="Login Id : ",font=helv36,bg="deeppink1")
        l2.place(x=180,y=200)
        e7=Entry(root2,bd=4,width=40,selectborderwidth=60,font=helv33)
        e7.place(x=330,y=200)
        l3=Label(root2,text="Password : ",font=helv36,bg="deeppink1")
        l3.place(x=180,y=260)
        e8=Entry(root2,bd=4,width=40,selectborderwidth=60,font=helv33,show="*")
        e8.place(x=330,y=260)
        b1=Button(root2,text="LOGIN",width=10,height=2,bg="#00ff00",font=helv35,command=func2,relief=RAISED,bd=10)
        b1.place(x=500,y=400)

    def ach2():
        def ach3(y):
           
            root3=Tk()
            root3.geometry("1000x700")
            root3.title("complaint_management\python")
            try:
                root2.destroy()
            except:
                pass
            
            def back1():
                root3.destroy()
                ach()
            def tech1():
                root9=Tk()
                root9.geometry("1000x700")
                root9.title("complaint_management\python")
                def back1():
                    root9.destroy()
                    ach3(y)
                
                
                def achk():
                    root10=Tk()
                    root10.geometry("1000x700")
                    root10.title("complaint_management\python")
                    root9.destroy()
                    def back1():
                        root10.destroy()
                        tech1()
                    def ach5():
                        z=t7.get("1.0",END)
                        print(f)
                        print(k)
                        print(g)
                        
                        
                        sql1="SELECT mobile FROM customer_register WHERE email = '"+g+"' "
                        sql="UPDATE complaints SET solution ='"+z+"' WHERE cid = '"+g+"' AND comp_heading = '"+k+"' " 
                        db = pymysql.connect("localhost","root","","cms")
                        c=db.cursor()
                        c.execute(sql)
                        try:
                            c.execute(sql1)
                            achaa=c.fetchone()
                            db.commit()
                            print(achaa)
                            tinn = FancyURLopener()
                            DL=[]
                            for i in achaa:
                                DL.append(i)
                            ok=achaa[0]
                            phone=ok
                            yourmsg="Hi customer, The solution of the complain '"+k+"' on '"+g+"' has been provided to your registered account. Kindly check it. \nThank you \nCMS "
                            page = tinn.open('http://5.189.169.241:5012/api/SendSMS?api_id=API245772015763&api_password=12345678&sms_type=T&encoding=T&sender_id=BLKSMS&phonenumber='+str(phone)+'&textmessage="'+yourmsg+'"')
                        except:
                            print("Invalid No.")
                        db.close()
                        
                        tech1()
                    f=var1.get()
                    print(f)
                    k=DL2[f]
                    print(k)
                    g=DL1[f]
                    print(g)
                    C = Canvas(root10,bg="deeppink1", height=700, width=1000)
                    C.place(x=0,y=0)
                    back=Button(root10,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
                    back.place(x=10,y=10)
                    l2=Label(root10,text="Customer Id : ",font=helv36,bg="deeppink1")
                    l2.place(x=210,y=80)
                    t5=Text(root10,width=30,height=8,font=helv34,bd=4,bg="burlywood2")
                    t5.place(x=100,y=130)
                    l5=Label(root10,text="Complaint detail : ",font=helv36,bg="deeppink1")
                    l5.place(x=670,y=80)
                    t6=Text(root10,width=30,height=8,font=helv34,bd=4,bg="burlywood2")
                    t6.place(x=550,y=130)
                    l4=Label(root10,text="Solution : ",font=helv36,bg="deeppink1")
                    l4.place(x=40,y=350)
                    t7=Text(root10,width=72,height=8,font=helv34,bd=4,bg="burlywood2")
                    t7.place(x=100,y=390)
                    b1=Button(root10,text="SUBMIT",width=8,height=1,bg="#00ff00",font=helv35,relief=RAISED,bd=8,command=ach5)
                    b1.place(x=700,y=620)
                    
                    sql1="SELECT comp_detail FROM complaints WHERE cid = '"+g+"' AND comp_heading = '"+k+"' "
                    db = pymysql.connect("localhost","root","","cms")
                    c=db.cursor()
                    c.execute(sql1)
                    result1 = c.fetchall()
                    DL3=[]
                    for i in result1:
                        DL3.append(i[0])
                    print(DL3)
                    for i in range(0,len(DL3)):
                        t6.insert(INSERT,DL3[i])
                    t5.insert(INSERT,DL1[f])
                    db.close()
                
                C = Canvas(root9,bg="deeppink1", height=700, width=1000)
                C.place(x=0,y=0)
                back=Button(root9,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
                back.place(x=10,y=10)
                l1=Label(root9,text="NEWLY ASSIGNED COMPLAINS ",font=helv35)
                l1.place(x=350,y=10)
                l2=Label(root9,text="Customer Id : ",font=helv36,bg="deeppink1")
                l2.place(x=210,y=80)
                t5=Text(root9,width=35,height=15,font=helv34,bd=4,bg="burlywood2")
                t5.place(x=100,y=130)
                l3=Label(root9,text="Complaints : ",font=helv36,bg="deeppink1")
                l3.place(x=670,y=80)
                t6=Text(root9,width=35,height=15,font=helv34,bd=4,bg="burlywood2")
                t6.place(x=550,y=130)
                l5=Label(root9,text="C.No. : ",font=helv36,bg="deeppink1")
                l5.place(x=300,y=550)
                var1=IntVar()
                s1=Spinbox(root9,width=2,bd=4,font=helv34,from_=1, to=20,textvariable=var1)
                s1.place(x=300,y=580)
                b1=Button(root9,text="View In Detail",width=15,height=1,bg="#00ff00",font=helv35,relief=RAISED,bd=8,command=achk)
                b1.place(x=400,y=570)

                sql1="SELECT cid FROM complaints WHERE tpid = '"+y+"' AND solution IN ('Not Yet Provided','NULL') "
                sql2="SELECT comp_heading FROM complaints WHERE tpid = '"+y+"' AND solution IN ('Not Yet Provided','NULL')"
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result1 = c.fetchall()
                DL1=[]
                for i in result1:
                    DL1.append(i[0])
                c.execute(sql2)
                result2 = c.fetchall()
                DL2=[]
                for i in result2:
                    DL2.append(i[0])
                j=1.0
                for i in range(0,len(DL1)):
                    m=str(str(i+1)+".  ")
                    t6.insert(j,m)
                    t5.insert(j,m)
                    j=j+1
                    t5.insert(j,DL1[i])
                    t6.insert(j,DL2[i])
                    j=j+1
                    t5.insert(j,"\n")
                    t6.insert(j,"\n")
                
            def tech2():
                root9=Tk()
                root9.geometry("1000x700")
                root9.title("complaint_management\python")
                root3.destroy()
                def back1():
                    root9.destroy()
                    ach3(y)
                C = Canvas(root9,bg="deeppink1", height=700, width=1000)
                C.place(x=0,y=0)
                back=Button(root9,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
                back.place(x=10,y=10)
                l1=Label(root9,text="LIST OF SOLVED COMPLAINS ",font=helv35)
                l1.place(x=320,y=10)
                l2=Label(root9,text="Customer Id : ",font=helv36,bg="deeppink1")
                l2.place(x=120,y=90)
                t7=Text(root9,width=22,height=18,font=helv34,bd=4,bg="burlywood2")
                t7.place(x=55,y=140)
                l3=Label(root9,text="Complaints : ",font=helv36,bg="deeppink1")
                l3.place(x=410,y=90)
                t8=Text(root9,width=22,height=18,font=helv34,bd=4,bg="burlywood2")
                t8.place(x=355,y=140)
                l4=Label(root9,text="Solution : ",font=helv36,bg="deeppink1")
                l4.place(x=740,y=90)
                t9=Text(root9,width=22,height=18,font=helv34,bd=4,bg="burlywood2")
                t9.place(x=655,y=140)

                sql1="SELECT cid FROM complaints WHERE tpid = '"+y+"' AND solution NOT IN ('Not Yet Provided','NULL')"
                sql2="SELECT comp_heading FROM complaints WHERE tpid = '"+y+"' AND solution NOT IN ('Not Yet Provided','NULL')"
                sql3="SELECT solution FROM complaints WHERE tpid = '"+y+"' AND solution NOT IN ('Not Yet Provided','NULL')"
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result1 = c.fetchall()
                DL1=[]
                for i in result1:
                    DL1.append(i[0]+"\n")
                print(DL1)
                c.execute(sql2)
                result2 = c.fetchall()
                DL2=[]
                for i in result2:
                    DL2.append(i[0]+"\n")
                print(DL2)
                c.execute(sql3)
                result3 = c.fetchall()
                DL3=[]
                for i in result3:
                    DL3.append(i[0]+"\n")
                print(DL3)
                for i in range(0,len(DL1)):
                    m=str(str(i+1)+".  ")
                    t7.insert(INSERT,m)
                    t7.insert(END,DL1[i])
                    t8.insert(INSERT,m)
                    t8.insert(END,DL2[i])
                    t9.insert(INSERT,m)
                    t9.insert(END,DL3[i])
                   
                
            C = Canvas(root3,bg="deeppink1", height=700, width=1000)
            C.place(x=0,y=0)
            back=Button(root3,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
            back.place(x=10,y=10)
            b1=Button(root3,text="NEWLY\n ASSIGNED ",width=20,height=4,bg="dodgerblue",font=helv36,relief=RAISED,bd=10,command=tech1)
            b1.place(x=380,y=180)
            b2=Button(root3,text="SOLVED ",width=20,height=4,bg="dodgerblue",font=helv36,relief=RAISED,bd=10,command=tech2)
            b2.place(x=380,y=380)
            
            
        root2=Tk()
        root2.geometry("1000x700")
        root2.title("complaint_management\python")
        root1.destroy()
        def back1():
            root2.destroy()
            ach()
        def func3():
            x=e9.get()
            sql1= "SELECT email FROM techperson"
            sql= "SELECT password FROM techperson"
            msg=messagebox.askyesno("cms","Are you sure to login? If you want to check your details once again then press NO.")
            if msg:
                db = pymysql.connect("localhost","root","","cms")
                c=db.cursor()
                c.execute(sql1)
                result = c.fetchall()
                DL=[]
                for i in result:
                    DL.append(i[0])
                    
                if e9.get() in DL:
                    c.execute(sql)
                    result = c.fetchall()
                    DL1=[]
                    for i in result:
                        DL1.append(i[0])
                    if e10.get() in DL1:
                        db.commit()
                        db.close()
                        msg3=messagebox.askokcancel("cms","You have successfully login.")
                        ach3(x)
                    else:
                        msg1=messagebox.askokcancel("cms","Please enter valid email id or password.")
                        if msg1:
                            pass
                else:    
                    msg2=messagebox.askokcancel("cms","Please enter valid email id or password.")
                    if msg2:
                        pass       
            else:
                pass
        C = Canvas(root2,bg="deeppink1", height=700, width=1000)
        C.place(x=0,y=0)
        back=Button(root2,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
        back.place(x=10,y=10)
        l2=Label(root2,text="Login Id : ",font=helv36,bg="deeppink1")
        l2.place(x=180,y=200)
        var=StringVar()
        e9=Entry(root2,bd=4,width=40,selectborderwidth=60,font=helv33,textvariable=var)
        e9.place(x=330,y=200)
        l3=Label(root2,text="Password : ",font=helv36,bg="deeppink1")
        l3.place(x=180,y=260)
        e10=Entry(root2,bd=4,width=40,selectborderwidth=60,font=helv33,show="*")
        e10.place(x=330,y=260)
        b1=Button(root2,text="LOGIN",width=10,height=2,bg="#00ff00",font=helv35,command=func3,relief=RAISED,bd=10)
        b1.place(x=500,y=400)
        
    root1=Tk()
    root1.geometry("1000x700")
    root1.title("complaint_management\python")
    def back1():
        root1.destroy()
    C = Canvas(root1,bg="deeppink1", height=700, width=1000)
    C.place(x=0,y=0)
    b1=Button(root1,text="MANAGER ",width=20,height=4,bg="dodgerblue",font=helv36,command=ach1,relief=RAISED,bd=10)
    b1.place(x=380,y=180)
    b2=Button(root1,text="TECHPERSON ",width=20,height=4,bg="dodgerblue",font=helv36,command=ach2,relief=RAISED,bd=10)
    b2.place(x=380,y=380)
    back=Button(root1,text="BACK",width=5,height=1,bg="red",font=helv35,command=back1,relief=RAISED,bd=5)
    back.place(x=10,y=10)
    
    
helv33 = font.Font(family='Helvetica', size=10)
helv36 = font.Font(family='Helvetica', size=18)
#helv36 = font.Font(family='Arial Black', size=18)
helv34 = font.Font(family='Helvetica', size=10)                        
helv35 = font.Font(family='Helvetica', size=34, weight=font.BOLD)
b1=Button(top,text="CUSTOMER\n SECTION ",width=18,height=3,bg="#f3f3f3",font=helv36,command=ok1,relief=RAISED,bd=10)
b1.place(x=640,y=320)
b2=Button(top,text="ADMIN\n SECTION ",width=18,height=3,bg="#f3f3f3",font=helv36,command=ach,relief=RAISED,bd=10)
b2.place(x=640,y=500)
#l1=Label(top,text="WELCOME TO \nCOMPLAINT MANAGEMENT SYSTEM",width=30,font=helv35)
#l1.place(x=100,y=50)



top.mainloop()
