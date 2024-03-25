import tkinter as tk
from tkinter import ttk
from datetime import *
from tkcalendar import *
import tkinter.messagebox
from tkinter import messagebox
from tkinter import*
import tempfile
import datetime
from PIL import ImageTk,Image
import Functions as fun
import sqlite3
import os.path

global emailVar
global passVar
global nameVar
global Namevar
global mnoVar
global prntchk,dbchk
global prnchk,crnchk
global dv1,dv2

window=tk.Tk()

emailVar=StringVar()
passVar=StringVar()
cpassVar=StringVar()
dpassVar=StringVar()
nameVar=StringVar()
Namevar=StringVar()
quesVar=StringVar()
ansVar=StringVar()
mnoVar=StringVar()
rtyvar=StringVar()
nadvar=StringVar()
nacvar=StringVar()
narvar=StringVar()
bfvar=StringVar()
btvar=StringVar()
bf1var=StringVar()
bt1var=StringVar()
ntravar=StringVar()
nmVar=StringVar()
agVar=StringVar()
genVar=StringVar()
cntv=IntVar()
bidVar=StringVar()
frmVar=StringVar()
toVar=StringVar()
dtvar=StringVar()
npas=IntVar()
dname=StringVar()
dlic=StringVar()
nodvar=StringVar()
mno=StringVar()

prnchk=0

#############################FieldListeners###############################

def MnoFieldListener(a,b,c):
    a=mnoVar.get()
    for i in a:
        if i.isalpha() or i.isspace():
            mnoVar.set('')
            messagebox.showinfo("Warning","Mobile No. doesn't contain alphabets or spaces")

def NameFieldListener(a,b,c):
    a=nameVar.get()
    for i in a:
        try :
            int(i)
            nameVar.set('')
            messagebox.showinfo("Warning","Name doesn't contain digits")
        except ValueError:
            continue

def DateFieldListener(a,b,c):
    try:
        date2=btvar.get()
        date1=bfvar.get()
        t11=date1.index('/')
        t12=date1.index('/',3)
        t21=date2.index('/')
        t22=date2.index('/',3)
        dd1=int(date1[0:t11])
        mm1=int(date1[t11+1:t12])
        yy1=int(date1[t12+1:len(date1)])
        dd2=int(date2[0:t21])
        mm2=int(date2[t21+1:t22])
        yy2=int(date2[t22+1:len(date1)])    
        if dd2<dd1:
            if mm2<=mm1 and yy2<=yy1:
                btvar.set('Select Date')
                messagebox.showinfo("Warning","Check-Out Date cannot be before Check-In Date")
    except ValueError:
        return

def DateFListener(a,b,c):
    try:
        myDate=bfvar.get()
        t1=myDate.index('/')
        t2=myDate.index('/',3)
        dd=int(myDate[0:t1])
        mm=int(myDate[t1+1:t2])
        yy='20'+myDate[t2+1:len(myDate)]
        yy=int(yy)
        d=date(yy,mm,dd)
        to=datetime.date.today()
        if to>d:
            bfvar.set('Select Date')
            messagebox.showinfo("Warning","Select Date correctly")
    except ValueError:
        return
        
    
mnoVar.trace('w', MnoFieldListener)
nameVar.trace('w',NameFieldListener)
btvar.trace('w',DateFieldListener)
bfvar.trace('w',DateFListener)
    
######################################Tour Package#########################    

def tour(a):
    
    def trBkng(event):
        value=Tree.item(Tree.selection())
        fc = value['values']
        can.destroy()
        trBkn(fc)
        
    def trBkn(fc):
        cnt=0
        window.geometry('550x600+250+5')  
        trv=[]    
        def adtrv(d):        
            a=nmVar.get()
            b=agVar.get()
            c=genVar.get()
            tr=[]
            if a!='' and b!='' and c!='':
                if b.isdigit():
                    tr.extend((a,b,c))
                    z=cntv.get()
                    cntv.set(z+1)
                else:
                    messagebox.showinfo("Warning","Age should be in digits")
                    agVar.set('')
                    return
            else:
                messagebox.showinfo("Warning","Enter Name,age and gender correctly")
                return
            trv.append(tr)
            nmVar.set('')
            agVar.set('')
            genVar.set('')
            cnt=cntv.get()
            t1.insert('', END, text='',value=(trv[cnt][0],trv[cnt][1],trv[cnt][2]))                
            t1.place(x=10,y=d+40)

        def cbkng(a,b,c,d,e):
            f=Namevar.get()
            g=bfvar.get()
            i=bidVar.get()
            global prnchk,crnchk
            if prnchk == 0:
                fq = a.get('1.0', END)
                ibd=i+'.txt'
                file = 'Bills\\'+ibd
                open(file, 'w').write(fq)
                os.startfile(file, "print")
                prnchk = 1
                crnchk=0
                genVar.set("")
            else:
                messagebox.showinfo("Information", "Bill already Printed...!")
            if crnchk==0:
                mdb=sqlite3.connect('Tour.db')
                mcr=mdb.cursor()
                mcr.execute("Insert into Record Values('{}','{}','{}','{}','{}','{}')".format(c,f,b,g,d,e))
                mdb.commit()
                mdb.close()
                crnchk=1
            tour(can)
            


        def tbkg(a):
            dt=bfvar.get()
            db=sqlite3.connect('Tour.db')
            cr=db.cursor()
            cr.execute(f"Select * from Tours where Name='{a[0]}'")
            data=cr.fetchall()
            hotl=data[0][6]-data[0][3]-data[0][4]
            ml=data[0][4]
            act=data[0][3]
            hotlp=hotl*len(trv)
            print(str(hotlp))
            mlp=ml*len(trv)
            actp=act*len(trv)
            db.close()
            
            db1=sqlite3.connect('Tour.db')
            cr1=db1.cursor()
            cr1.execute(f"Select bnID from Record where Tname='{a[0]}'")
            vl=cr1.fetchall()
            db1.close()
             
            chkr=a[0]
            chkr=chkr[0:3]
            
            mx=0
            for i in range(len(vl)):
                bnd=vl[i][0]
                bnd=bnd[8:len(vl[i][0])]
                bn=int(bnd)
                if mx<bn:
                    mx=bn
            bnid=chkr+"TD000"+str(mx+1)
            bidVar.set(bnid)
            if len(trv)<=4:
                dtrf=data[0][5]*1
                dtf=dtrf
                dtrf='Rs.'+str(dtrf)
            else:
                dtrf=data[0][5]*2
                dtf=dtrf
                dtrf='Rs.'+str(dtrf)
            ttlpr=hotlp+mlp+actp+dtf
            tpttl='Rs.'+str(ttlpr)    
                
            if len(trv)==0: 
                messagebox.showinfo("Warning","Add Travellers to book package")
            elif dt=='Select Date':
                messagebox.showinfo("Warning","Select Date to star tour")
            else:
                bkg.place_forget()
                window.geometry('1160x600+250+5')
                can3=Canvas(can,width=610,height=600,bg='white')
                can3.pack(side=RIGHT)
                textreciept = Text(can3,state='normal',width=450,height=600)
                textreciept.pack(fill='both')
                textreciept.bind('<Enter>', fun.E_reciept)
                textreciept.bind('<Leave>', fun.L_reciept)
                cbkg=Button(can2,text="Confirm Booking",relief=FLAT,font=('Times New Roman','12','bold'),bg='olive drab',fg='lemon chiffon',
                         command=lambda: cbkng(textreciept,bnid,a[0],len(trv),ttlpr))
                cbkg.place(x=400,y=560)
                cbkg.bind('<Enter>', fun.adtime)
                cbkg.bind('<Leave>', fun.adtimeends)
                ht='Rs.'+str(hotl)
                meal='Rs.'+str(ml)
                actv='Rs.'+str(act)
                dta='Rs.'+str(data[0][5])
                tphtl='Rs.'+str(hotlp)
                tpml='Rs.'+str(mlp)
                tpac='Rs.'+str(actp)               
                textreciept.insert(END, "\t\t\t   GOA TOUR PACKAGES   \t" + "\n")
                textreciept.insert(END, "\t\t    _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ \t" + "\n"+"\n")
                textreciept.insert(END, " Tour Name: "+a[0]+"\n")
                textreciept.insert(END, " Booking ID: "+bnid+"\n")
                textreciept.insert(END, " Tour Starts on: "+ bfvar.get()+"\n")
                textreciept.insert(END, " Duration: "+a[1]+"\n")
                textreciept.insert(END, " +" + "-" * (20) + "+" + "-" * (12) + "+" + "-" * (20) + "+" + "-" * (15)+"+"+"\n")
                textreciept.insert(END, " |" + " Inclusions" +" "*(9)+"|"+ " Price"+" "*(6)+"|"+" No. of travellers  "+"|"+" Total Price"+" "*(3)+"|"+"\n")
                textreciept.insert(END, " +" + "-" * (20) + "+" + "-" * (12) + "+" + "-" * (20) + "+" + "-" * (15)+"+"+"\n")
                textreciept.insert(END, " |" + " Hotel" +" "*(14)+"| "+ht +" "*(8-len(str(hotl)))+"| "+str(len(trv))+" "*(18)+"| "+tphtl+" "*(11-len(str(hotlp)))+"|"+"\n")
                textreciept.insert(END, " +" + "-" * (20) + "+" + "-" * (12) + "+" + "-" * (20) + "+" + "-" * (15)+"+"+"\n")
                textreciept.insert(END, " |" + " Meals" +" "*(14)+"| "+meal  +" "*(8-len(str(ml)))+"| "+str(len(trv))+" "*(18)+"| "+tpml+" "*(11-len(str(mlp)))+"|"+"\n")
                textreciept.insert(END, " +" + "-" * (20) + "+" + "-" * (12) + "+" + "-" * (20) + "+" + "-" * (15)+"+"+"\n")
                if a[2]!=0:
                    textreciept.insert(END, " |" + " Activities" +" "*(9)+"| "+actv  +" "*(8-len(str(act)))+"| "+str(len(trv))+" "*(18)+"| "+tpac+" "*(11-len(str(actp)))+"|"+"\n")
                    textreciept.insert(END, " +" + "-" * (20) + "+" + "-" * (12) + "+" + "-" * (20) + "+" + "-" * (15)+"+"+"\n")
                
                textreciept.insert(END, " |" + " Transfers" +" "*(10)+"| "+dta +" "*(8-len(str(data[0][5])))+"| "+str(len(trv))+" "*(18)+"| "+dtrf+" "*(13-len(str(dtrf)))+"|"+"\n")                
                textreciept.insert(END, " +" + "-" * (20) + "+" + "-" * (12) + "+" + "-" * (20) + "+" + "-" * (15)+"+"+"\n")
                textreciept.insert(END, " "*(35)+"|"+" Total Price:"+" "*(7)+ "| "+tpttl+" "*(11-len(str(ttlpr)))+"|"+"\n")
                textreciept.insert(END, " "*(35)+"+" + "-" * (20) + "+" + "-" * (15)+"+"+"\n"+"\n")
                textreciept.insert(END, "\t\t\t *******THANK YOU*******")


        
        def calendar(event):
            screen=Toplevel()
            screen.overrideredirect(1)
            screen.maxsize=(210,230)
            screen.geometry('210x230+530+400')
            screen.title("Calendar")
            screen.configure(bg='White',border='1px solid')
            def selectDate():
                myDate=myCal.get_date()
                bfvar.set(myDate)
                t1=myDate.index('/')
                t2=myDate.index('/',3)
                dd=int(myDate[0:t1])
                mm=int(myDate[t1+1:t2])
                yy='20'+myDate[t2+1:len(myDate)]
                yy=int(yy)
                d1=date(yy,mm,dd)
                bf1var.set(d1)
                screen.destroy()
            myCal=Calendar(screen,setmode='day',date_pattern='d/m/yy')
            myCal.pack(fill=BOTH)            
            opencal=Button(screen,text="Select Date",command=selectDate)
            opencal.place(x=30,y=195)
            bkcal=Button(screen,text="Cancel",command=lambda: screen.destroy())
            bkcal.place(x=140,y=195)
        global pic,imjpg
        def agrtr(event):
            agetr.focus_set()
        can=Canvas(window,width=1000,height=700,bg='white')
        can.pack()
        can2=Canvas(can,width=550,height=700,bg='lemon chiffon')
        can2.pack(side=LEFT)
        bk=Button(can2,text="Back",relief=FLAT,font=('Times New Roman','12','bold'),bg='olive drab',fg='lemon chiffon',
                         command=lambda: tour(can))
        bk.place(x=10,y=560)
        bk.bind('<Enter>', fun.adtime)
        bk.bind('<Leave>', fun.adtimeends)
        bkg=Button(can2,text="Book",relief=FLAT,font=('Times New Roman','12','bold'),bg='olive drab',fg='lemon chiffon',
                         command=lambda: tbkg(fc))
        bkg.place(x=490,y=560)
        bkg.bind('<Enter>', fun.adtime)
        bkg.bind('<Leave>', fun.adtimeends)
        m2=sqlite3.connect('Tour.db')
        c2=m2.cursor()
        c2.execute(f"select pics from Tours where Name='{fc[0]}'")        
        drt=c2.fetchall()
        pic=drt[0][0]
        im=Image.open(pic)
        kim=im.resize((240,140),Image.LANCZOS)
        imjpg=ImageTk.PhotoImage(kim)
        can2.create_image(280,60,anchor='nw',image=imjpg)
        can2.create_text(280,250,text="Price:  "+str(fc[3]),anchor='w',font=('Impact','16'),fill='olive drab')
        can2.create_text(420,250,text=" per person",anchor='w',font=('Impact','12'),fill='olive drab')
        can2.create_text(280,320,text="Start Date:",anchor='w',font=('Impact','16'),fill='olive drab')
        bfvar.set('Select Date')
        dtbtn=Entry(can2,textvariable=bfvar,font=('Book Antiqua', 12, 'bold'),state=DISABLED)
        dtbtn.place(x=280,y=340)
        dtbtn.bind('<Enter>', fun.showtime)
        dtbtn.bind('<Leave>', fun.showtimeends)
        dtbtn.bind('<Button-1>', calendar)  
        t1=ttk.Treeview(can2,height=5)
        sty=ttk.Style()
        sty.theme_use("alt")
        sty.configure("Treeview",background="LemonChiffon2",foreground="LemonChiffon4",font=('Times New Roman','11','bold'),
                                rowheight=25,fieldbackground="olive drab")
        t1["columns"] = ("one", "two","three")
        t1.column("#0", width=0,  stretch=NO)
        t1.column("one", width=120, minwidth=120, stretch=NO)
        t1.column("two", width=30, minwidth=30, stretch=NO)
        t1.column("three", width=70, minwidth=70, stretch=NO)
        t1.heading("#0", text="", anchor=W)
        t1.heading("one", text="Name", anchor=W)
        t1.heading("two", text="Age", anchor=W)
        t1.heading("three", text="Gender", anchor=W)
        ttlbl=Label(can2,text=fc[0],font=('Impact','25'),bg='lemon chiffon',fg='OliveDrab4')
        ttlbl.place(x=2,y=2)
        cntv.set(-1)
        if str(fc[2])=='0':
            can2.create_text(10,60,text= "• Transfers Included",anchor='w',font=('Times New Roman','12','bold'),fill='LemonChiffon4')
            can2.create_text(10,80,text= "• Meals Included",anchor='w',font=('Times New Roman','12','bold'),fill='LemonChiffon4')
            can2.create_text(10,140,text= "Activities",anchor='w',font=('Impact','16'),fill='olive drab')
            can2.create_text(10,165,text= "Not Included",anchor='w',font=('Times New Roman','12','bold'),fill='LemonChiffon4')
            can2.create_text(10,205,text= "Travellers",anchor='w',font=('Impact','16'),fill='olive drab')
            can2.create_text(100,205,text= "(2 travellers=1 room,max 8)",anchor='w',font=('Impact','10'),fill='olive drab')
            can2.create_text(10,230,text= "Name: ",anchor='w',font=('Impact','12'),fill='LemonChiffon4')
            can2.create_text(10,258,text= "Age: ",anchor='w',font=('Impact','12'),fill='LemonChiffon4')
            can2.create_text(10,286,text= "Gender: ",anchor='w',font=('Impact','12'),fill='LemonChiffon4')
            nmetr=Entry(can2,textvariable=nmVar,font=('Times New Roman','11'))
            nmetr.place(x=100,y=225)
            nmetr.bind('<Return>',agrtr)
            agetr=Entry(can2,textvariable=agVar,font=('Times New Roman','11'))
            agetr.place(x=100,y=250)
            genetr=OptionMenu(can2,genVar,"Male","Female","Transgender")
            genetr.config(width=12,height=1,bg='white')
            genetr.place(x=100,y=275)
            c=320
            adbtn=Button(can2,text="Add Traveller",relief=FLAT,font=('Times New Roman','12','bold'),bg='olive drab',fg='lemon chiffon',
                         command=lambda: adtrv(c))
            adbtn.place(x=10,y=c)
            adbtn.bind('<Enter>', fun.adtime)
            adbtn.bind('<Leave>', fun.adtimeends)
        else:
            can2.create_text(10,60,text= "• Activities lncluded",anchor='w',font=('Times New Roman','12','bold'),fill='LemonChiffon4')
            can2.create_text(10,80,text= "• Transfers Included",anchor='w',font=('Times New Roman','12','bold'),fill='LemonChiffon4')
            can2.create_text(10,100,text= "• Meals Included",anchor='w',font=('Times New Roman','12','bold'),fill='LemonChiffon4')
            can2.create_text(10,137,text= "Activities",anchor='w',font=('Impact','16'),fill='olive drab')
            m1=sqlite3.connect('Tour.db')
            c1=m1.cursor()
            c1.execute(f"select * from Activity where no='{fc[2]}'")
            ft=c1.fetchall()
            c=162
            for i in range(1,int(ft[0][0])+1):
                can2.create_text(10,c,text="• "+ft[0][i],anchor='w',font=('Times New Roman','12','bold'),fill='LemonChiffon4')
                c+=20
            c+=17
            can2.create_text(10,c,text= "Travellers",anchor='w',font=('Impact','16'),fill='olive drab')
            can2.create_text(100,c,text= "(2 travellers=1 room,max 8)",anchor='w',font=('Impact','10'),fill='olive drab')
            can2.create_text(10,c+25,text= "Name: ",anchor='w',font=('Impact','12'),fill='LemonChiffon4')
            can2.create_text(10,c+53,text= "Age: ",anchor='w',font=('Impact','12'),fill='LemonChiffon4')
            can2.create_text(10,c+81,text= "Gender: ",anchor='w',font=('Impact','12'),fill='LemonChiffon4')
            nmetr=Entry(can2,textvariable=nmVar,font=('Times New Roman','11'))
            nmetr.place(x=100,y=c+20)
            nmetr.bind('<Return>',agrtr)
            agetr=Entry(can2,textvariable=agVar,font=('Times New Roman','11'))
            agetr.place(x=100,y=c+45)
            genetr=OptionMenu(can2,genVar,"Male","Female","Transgender")
            genetr.config(width=12,height=1,bg='white')
            genetr.place(x=100,y=c+70)
            c+=110
            adbtn=Button(can2,text="Add Traveller",font=('Times New Roman','12','bold'),bg='olive drab',fg='lemon chiffon',
                         command=lambda: adtrv(c),relief=FLAT)
            adbtn.place(x=10,y=c)
            adbtn.bind('<Enter>', fun.adtime)
            adbtn.bind('<Leave>', fun.adtimeends)
    
    a.destroy()
    global Img
    window.geometry('800x760+300+5')
    window.title('Tour Packages')
    can=Canvas(window,width=800,height=800,bg='white')
    can.pack()
    into=r'pct3.png'
    Img=ImageTk.PhotoImage(Image.open(into))
    lbl=Label(can,image=Img,text='  Tour Packages',height=100,width=800,relief=FLAT,compound=LEFT,
              font=('Monotype Corsiva','50','bold','underline'),bg='white')
    lbl.pack(side=TOP,anchor='w')
    Tree = ttk.Treeview(can,height=11)
    Tree.pack()
    style=ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview",background="gray92",foreground="black",font=('Centaur','15'),
                            rowheight=50,fieldbackground="gray95")
    Tree["columns"] = ("one", "two","three","four")
    Tree.column("#0", width=0,  stretch=NO)
    Tree.column("one", width=400, minwidth=400, stretch=NO)
    Tree.column("two", width=100, minwidth=100, stretch=NO)
    Tree.column("three", width=100, minwidth=100, stretch=NO)
    Tree.column("four", width=100, minwidth=100, stretch=NO)
    Tree.heading("#0", text="", anchor=W)
    Tree.heading("one", text="Name", anchor=W)
    Tree.heading("two", text="Duration", anchor=W)
    Tree.heading("three", text="Activities", anchor=W)
    Tree.heading("four", text="Price per person", anchor=W)
    Tree['show']='headings'
    mydbs=sqlite3.connect('Tour.db')
    mycrsr=mydbs.cursor()
    mycrsr.execute("select Name,Specs,Activity,TotalPrice from Tours")
    data = mycrsr.fetchall()
    mydbs.close()
    dat=[]
    for i in range(len(data)):
        s=''
        t=str(data[i][0])
        for j in t:
            if j == '{' or j=='}':
                continue
            else:
                s=s+j
        dat.append(s)

    for i in range(len(data)):
        p=u'\u20B9'+str(data[i][3])
        Tree.insert('', END, text='',value=(dat[i],data[i][1],data[i][2],p))
    Tree.bind('<Double-Button-1>',trBkng)
    back=Button(can,text="Back",relief=FLAT,height=10,width=40,font=('Times New Roman','16','bold'),bg='olive drab',fg='lemon chiffon',
                         command=lambda: optionPg(can))
    back.pack(side=BOTTOM,pady=12)
    back.bind('<Enter>', fun.adtime)
    back.bind('<Leave>', fun.adtimeends)


###################################Hotel################################    

def hotel(a):
    a.destroy()
    global Img,img,imgfl
    window.geometry('800x760+300+5')
    window.title('Hotels')
    
    def Book():
        def Save(a,b,c,d,e):
            global prntchk,dbchk
            f=rtyvar.get()
            g=bf1var.get()
            h=bt1var.get()
            i=bidVar.get()
            if prntchk == 0:
                q = c.get('1.0', END)
                idb=i+'.txt'
                file = 'Bills\\'+idb
                open(file, 'w').write(q)
                os.startfile(file, "print")
                prntchk = 1
                dbchk=0
            else:
                messagebox.showinfo("Information", "Bill already Printed...!")
            if dbchk==0:
                for i in e:
                    mdbs=sqlite3.connect("Hotel Data/"+d+".db")
                    crsr=mdbs.cursor()
                    crsr.execute("Insert into Booking Values('{}','{}','{}','{}','{}')".format(i,g,h,b,f))
                    mdbs.commit()
                    mdbs.close()
                root.destroy()
                dbchk=1

            
        def genrecp(p):
            global prntchk,dbchk
            a=rtyvar.get()
            b=nadvar.get()
            c=nacvar.get()
            d=narvar.get()
            e=bf1var.get()
            f=bt1var.get()
            j=bfvar.get()
            k=btvar.get()
            g=emailVar.get()
            if j=='Select Date' or k=="Select Date":
                pass
            else:
                t1=j.index('/')
                t2=j.index('/',3)
                dd=int(j[0:t1])
                mm=int(j[t1+1:t2])
                yy='20'+j[t2+1:len(j)]
                yy=int(yy)
                d1=date(yy,mm,dd)
                t1=k.index('/')
                t2=k.index('/',3)
                dd=int(k[0:t1])
                mm=int(k[t1+1:t2])
                yy='20'+k[t2+1:len(k)]
                yy=int(yy)
                d2=date(yy,mm,dd)
                dft=d2-d1
                dt=dft.days
            mds=sqlite3.connect('Tourism.db')
            cn=mds.cursor()
            cn.execute(f"Select Name,Mno from login where Email='{g}'")
            Nmn=cn.fetchall()
            mds.close()
            if a!='' and b!='' and c!='' and d!='' and e!='' and f!='':
                root.geometry('1180x500+250+5')
                can2=Canvas(root,width=680,height=500,bg='white')
                can2.pack(side=RIGHT)
                textreciept = Text(can2,state='normal',width=680,height=500)
                textreciept.pack(fill='both')
                textreciept.bind('<Enter>', fun.E_reciept)
                textreciept.bind('<Leave>', fun.L_reciept)
                mds1=sqlite3.connect('Hotels.db')
                cn1=mds1.cursor()
                cn1.execute(f"Select * from '{p}' where RoomType='{a}'")
                da=cn1.fetchall()
                l1=len(da)
                ttl=da[0][1]*int(d)
                mds2=sqlite3.connect('Hotel Data/'+p+'.db')
                cn2=mds2.cursor()
                cn2.execute(f"Select * from Booking where RoomType='{a}'")
                data=cn2.fetchall()
                cn2.execute(f"Select DISTINCT bookingID from Booking")
                data1=cn2.fetchall()
                bi=0
               
                for i in data1:
                    gd=i[0]
                    lbid=gd[8:len(gd)]
                    lbid=int(lbid)
                    if lbid>bi:
                        bi=lbid
                bid="BK"+p[0:3].upper()+'000'+str(bi+1)
                bidVar.set(bid)
                l2=len(data)
                n=[]
                nr=da[0][0]
                nrc=''
                nrd=[]
                if l2>0:                    
                    for i in range(l2):
                        q1=data[i][1]
                        q2=data[i][2]
                        if e>=q1 and f<=q2 or e>=q1 and e<q2 and f>=q2 or e<=q1 and f>q1 and f<=q2 or e<=q1 and f>=q2:
                            n.append(data[i][0])
                    if (len(n)+int(d))>l1:
                        messagebox.showinfo('Warning',d," rooms unavailable on dates mentioned")
                        root.destroy()
                    else:
                        nvc=nr+len(n)
                        for i in range(nvc,nvc+int(d)):
                            if i!=(nvc+int(d)-1):
                                nrc=nrc+str(i)+' , '
                            else:
                                nrc=nrc+str(i)
                            nrd.append(i)
                        
                        textreciept.insert(END, "\t\t\t\t    GOA TOURISM   \t\t\t" + "\n")
                        textreciept.insert(END, "\t\t\t  _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ \t\t\t" + "\n"+"\n")
                        textreciept.insert(END, "   Name: "+Nmn[0][0]+"\n")
                        textreciept.insert(END, "   Mobile No.: "+str(Nmn[0][1])+"\n")
                        textreciept.insert(END, "   Email: "+g+" "*(40-len(g))+"Check-In: "+j+"\n")
                        textreciept.insert(END, "   No. of Adults: "+b+" "*(32-len(b))+"Check-Out: "+k+"\n")
                        textreciept.insert(END, "   No. of Children: "+c+"\n")
                        textreciept.insert(END, "   Room No.: "+nrc+"\n")
                        textreciept.insert(END, "   Booking ID: "+bid+"\n")
                        textreciept.insert(END, "   +" + "-" * (30) + "+" + "-" * (12) + "+" + "-" * (14) + "+" + "-" * (14)+"+"+"\n")
                        textreciept.insert(END, "   |" + " Hotel Name" +" "*(19)+"|"+ " Room Type"+" "*(2)+"|"+" No. of Rooms "+"|"+" Total"+" "*(8)+"|"+"\n")
                        textreciept.insert(END, "   +" + "-" * (30) + "+" + "-" * (12) + "+" + "-" * (14) + "+" + "-" * (14)+"+"+"\n")
                        textreciept.insert(END, "   | " + p +" "*(29-len(p))+"| "+ a+" "*(11-len(a))+"| "+d+" "*(13-len(d))+"| Rs."+str(ttl*dt)+" "*(10-len(str(ttl*dt)))+"|"+"\n")
                        textreciept.insert(END, "   +" + "-" * (30) + "+" + "-" * (12) + "+" + "-" * (14) + "+" + "-" * (14)+"+"+"\n")
                        textreciept.insert(END, "\t\t\t   "+"*"*(8)+"Thank You"+"*"*(8)+"\t\t\t" + "\n"+"\n")
                        svbtn.place_forget()
                        prntchk=0
                        dbchk=0
                        bkbtn=Button(can1,text="Confirm Booking",font=('Impact', 12),width=30,bg='azure4',fg='azure2',
                                     command=lambda: Save(ttl,bid,textreciept,p,nrd),relief=FLAT)
                        bkbtn.place(x=130,y=445)
                else:                   
                    for i in range(nr,nr+int(d)):
                        if i!=(nr+int(d)-1):
                            nrc=nrc+str(i)+' , '
                        else:
                            nrc=nrc+str(i)
                        nrd.append(i)
                    bid="BK"+p[0:3].upper()+'0001'
                    textreciept.insert(END, "\t\t\t\t    GOA TOURISM   \t\t\t" + "\n")
                    textreciept.insert(END, "\t\t\t  _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ \t\t\t" + "\n"+"\n")
                    textreciept.insert(END, "   Name: "+Nmn[0][0]+"\n")
                    textreciept.insert(END, "   Mobile No.: "+str(Nmn[0][1])+"\n")
                    textreciept.insert(END, "   Email: "+g+" "*(40-len(g))+"Check-In:  "+j+"\n")
                    textreciept.insert(END, "   No. of Adults: "+b+" "*(32-len(b))+"Check-Out: "+k+"\n")
                    textreciept.insert(END, "   No. of Children: "+c+"\n")
                    textreciept.insert(END, "   Room No.: "+nrc+"\n")
                    textreciept.insert(END, "   Booking ID: "+bid+"\n")
                    textreciept.insert(END, "   +" + "-" * (30) + "+" + "-" * (12) + "+" + "-" * (14) + "+" + "-" * (14)+"+"+"\n")
                    textreciept.insert(END, "   |" + " Hotel Name" +" "*(19)+"|"+ " Room Type"+" "*(2)+"|"+" No. of Rooms "+"|"+" Total"+" "*(8)+"|"+"\n")
                    textreciept.insert(END, "   +" + "-" * (30) + "+" + "-" * (12) + "+" + "-" * (14) + "+" + "-" * (14)+"+"+"\n")
                    textreciept.insert(END, "   | " + p +" "*(29-len(p))+"| "+ a+" "*(11-len(a))+"| "+d+" "*(13-len(d))+"| Rs."+str(ttl*dt)+" "*(10-len(str(ttl*dt)))+"|"+"\n")
                    textreciept.insert(END, "   +" + "-" * (30) + "+" + "-" * (12) + "+" + "-" * (14) + "+" + "-" * (14)+"+"+"\n")
                    textreciept.insert(END, "\t\t\t   "+"*"*(8)+"Thank You"+"*"*(8)+"\t\t\t" + "\n"+"\n")
                    svbtn.place_forget()
                    prntchk=0
                    bkbtn=Button(can1,text="Confirm Booking",font=('Impact', 12),width=30,bg='azure4',fg='azure2',
                                 command=lambda: Save(ttl,bid,textreciept,p,nrd),relief=FLAT)
                    bkbtn.place(x=130,y=445)
            else:
                messagebox.showinfo('Warning',"Please enter all the details")
                                    
        def calendar1(event):
            screen=Toplevel()
            screen.overrideredirect(1)
            screen.maxsize=(210,230)
            screen.geometry('210x230+505+292')
            screen.title("Calendar")
            screen.configure(bg='White',border='1px solid')
            def selectDate():
                myDate=myCal.get_date()
                bfvar.set(myDate)
                t1=myDate.index('/')
                t2=myDate.index('/',3)
                dd=int(myDate[0:t1])
                mm=int(myDate[t1+1:t2])
                yy='20'+myDate[t2+1:len(myDate)]
                yy=int(yy)
                d1=date(yy,mm,dd)
                bf1var.set(d1)
                screen.destroy()
            myCal=Calendar(screen,setmode='day',date_pattern='d/m/yy')
            myCal.pack(fill=BOTH)            
            opencal=Button(screen,text="Select Date",command=selectDate)
            opencal.place(x=30,y=195)
            bkcal=Button(screen,text="Cancel",command=lambda: screen.destroy())
            bkcal.place(x=140,y=195)
            
        def calendar2(event):
            screen=Toplevel()
            screen.overrideredirect(1)
            screen.maxsize=(210,230)
            screen.geometry('210x230+505+412')
            screen.title("Calendar")
            screen.configure(bg='White',border='1px solid')
            def selectDate():
                myDate=myCal.get_date()
                btvar.set(myDate)
                t1=myDate.index('/')
                t2=myDate.index('/',3)
                dd=int(myDate[0:t1])
                mm=int(myDate[t1+1:t2])
                yy='20'+myDate[t2+1:len(myDate)]
                yy=int(yy)
                d1=date(yy,mm,dd)
                bt1var.set(d1)
                screen.destroy()
            myCal=Calendar(screen,setmode='day',date_pattern='d/m/yy')
            myCal.pack(fill=BOTH)            
            opencal=Button(screen,text="Select Date",command=selectDate)
            opencal.place(x=30,y=195)
            bkcal=Button(screen,text="Cancel",command=lambda: screen.destroy())
            bkcal.place(x=140,y=195)
        rtyvar.set('')
        global pic,imjpg
        root=tk.Toplevel()
        root.geometry('500x500+250+5')
        root.maxsize(1180,500)
        value=Tree.item(Tree.selection())
        fc = value['values']
        pic="Hotel/"+fc[0]+".jpg"
        im=Image.open(pic)
        kim=im.resize((230,130),Image.LANCZOS)
        can1=Canvas(root,width=500,height=500,bg='azure2')
        can1.pack(side=LEFT)
        imjpg=ImageTk.PhotoImage(kim)
        can1.create_image(5,50,anchor=NW,image=imjpg)
        can1.create_text(250,25,text=fc[0],font=('Impact','20'),fill='azure4')
        file="Hotel Data/"+fc[0]+".db"
        dbs=sqlite3.connect('Hotels.db')
        con=dbs.cursor()
        con.execute(f"Select Rooms from '{fc[0]}'")
        data1=con.fetchall()
        con.execute(f"Select DISTINCT Price,RoomType from '{fc[0]}'")
        data2=con.fetchall()
        dbs.close()
        h=75
        rt=[]
        def nxtet1(event):
            nad.focus_set()
        def nxtet2(event):
            nac.focus_set()
        def nxtet3(event):
            nar.focus_set()
        for i in data2:            
            can1.create_text(450,h,text=i[1]+" Price:    "+u'\u20B9'+str(i[0]),font=('Impact','10'),anchor='e',fill='azure4')
            h=h+15
            rt.append(i[1])
        can1.create_text(20,215,text="Room Type",anchor='w',font=('Impact','12'),fill='azure4')
        drop=ttk.Combobox(can1,value=rt,textvariable=rtyvar,width=15,font=('Book Antiqua', 12, 'bold'))
        drop.place(x=20,y=230)
        drop.focus_set()
        drop.bind('<Return>',nxtet1)
        can1.create_text(20,275,text="No. of adults",anchor='w',font=('Impact','12'),fill='azure4')
        can1.create_text(20,335,text="No. of children",anchor='w',font=('Impact','12'),fill='azure4')
        can1.create_text(20,395,text="No. of rooms",anchor='w',font=('Impact','12'),fill='azure4')
        can1.create_text(250,215,text="Booking from",anchor='w',font=('Impact','12'),fill='azure4')
        can1.create_text(250,335,text="Booking to",anchor='w',font=('Impact','12'),fill='azure4')
        nad=Entry(root,textvariable=nadvar,width=15,font=('Book Antiqua', 12, 'bold'))
        nad.place(x=20,y=290)
        nad.bind('<Enter>', fun.showtime)
        nad.bind('<Leave>', fun.showtimeends)
        nad.bind('<Return>',nxtet2)
        nac=Entry(root,textvariable=nacvar,width=15,font=('Book Antiqua', 12, 'bold'))
        nac.place(x=20,y=350)
        nac.bind('<Enter>', fun.showtime)
        nac.bind('<Leave>', fun.showtimeends)
        nac.bind('<Return>',nxtet3)
        nar=Entry(root,textvariable=narvar,width=15,font=('Book Antiqua', 12, 'bold'))
        nar.place(x=20,y=410)
        nar.bind('<Enter>', fun.showtime)
        nar.bind('<Leave>', fun.showtimeends)
        bfvar.set('Select Date')
        btvar.set('Select Date')
        bfdtbtn=Entry(can1,textvariable=bfvar,font=('Book Antiqua', 12, 'bold'),state=DISABLED,relief=FLAT)
        bfdtbtn.place(x=250,y=230)
        bfdtbtn.bind('<Enter>', fun.showtime)
        bfdtbtn.bind('<Leave>', fun.showtimeends)
        bfdtbtn.bind('<Button-1>', calendar1)  
        btdtbtn=Entry(can1,textvariable=btvar,font=('Book Antiqua', 12, 'bold'),state=DISABLED,relief=FLAT)
        btdtbtn.place(x=250,y=350)
        btdtbtn.bind('<Enter>', fun.showtime)
        btdtbtn.bind('<Leave>', fun.showtimeends)
        btdtbtn.bind('<Button-1>', calendar2)
        svbtn=Button(can1,text="Book",font=('Impact', 12),width=30,bg='azure4',fg='azure2',command=lambda: genrecp(fc[0]),relief=FLAT)
        svbtn.place(x=130,y=445)
                
    def Booking(event):
        Book()
        
    can=Canvas(window,width=800,height=760,bg='white')
    can.pack()
    into=r'pct.png'
    Img=ImageTk.PhotoImage(Image.open(into))
    lbl=Label(can,image=Img,text='  Hotels',height=100,width=800,relief=FLAT,compound=LEFT,
              font=('Monotype Corsiva','50','bold','underline'),bg='white')
    lbl.pack(side=TOP,anchor='w')
    mydbs=sqlite3.connect('Hotels.db')
    mycrsr=mydbs.cursor()
    mycrsr.execute("select name from sqlite_master where type='table'")
    data = mycrsr.fetchall()
    mydbs.close()
    dat=[]
    for i in data:
        s=''
        for j in i:
            if j == '{' or j=='}':
                continue
            else:
                s=s+j
        dat.append(s)
    Tree = ttk.Treeview(can,height=11)
    Tree.pack()
    style=ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview",background="gray92",foreground="black",font=('Centaur','15'),
                            rowheight=50,fieldbackground="gray95")
    Tree["columns"] = ("one", "two")
    Tree.column("#0", width=0,  stretch=NO)
    Tree.column("one", width=400, minwidth=400, stretch=NO)
    Tree.column("two", width=100, minwidth=100, stretch=NO)
    Tree.heading("#0", text="", anchor=W)
    Tree.heading("one", text="Hotel Name", anchor=W)
    Tree.heading("two", text="Price per day", anchor=W)
    Tree['show']='headings'
    for i in dat:
        sq=sqlite3.connect('Hotels.db')
        myc=sq.cursor()
        myc.execute(f"select Price from '{i}'")
        d = myc.fetchall()
        t=d[0]
        p=u'\u20B9'+str(t[0])
        Tree.insert('', END, text='',value=(i,p))
        sq.close()
    Tree.bind('<Double-Button-1>',Booking)
    back=Button(can,text="Back",relief=FLAT,height=10,width=40,font=('Times New Roman','16','bold'),bg='olive drab',fg='lemon chiffon',
                         command=lambda: optionPg(can))
    back.pack(side=BOTTOM,pady=12)
    back.bind('<Enter>', fun.adtime)
    back.bind('<Leave>', fun.adtimeends)
    

##############################Travel###################################

def bus(a):
    a.destroy()
    window.geometry('523x580+450+10')
    window.title('Bus')
    def calendar(event):
        screen=Toplevel()
        screen.overrideredirect(1)
        screen.maxsize(210,230)
        screen.geometry('210x230+780+140')
        screen.configure(bg='White',border='1px solid')
        def selectDate():
            myDate=myCal.get_date()
            dtvar.set(myDate)
            t1=myDate.index('/')
            t2=myDate.index('/',3)
            dd=int(myDate[0:t1])
            mm=int(myDate[t1+1:t2])
            yy='20'+myDate[t2+1:len(myDate)]
            yy=int(yy)
            screen.destroy()
        myCal=Calendar(screen,setmode='day',date_pattern='d/m/yy')
        myCal.pack(fill=BOTH)            
        opencal=Button(screen,text="Select Date",command=selectDate)
        opencal.place(x=30,y=195)
        bkcal=Button(screen,text="Cancel",command=lambda: screen.destroy())
        bkcal.place(x=140,y=195)
    def search():
        d=dtvar.get()
        if d=="Select Date":
            messagebox.showinfo('Warning'," Please select the date first")
        else:
            treeVw()
    def treeVw():
        def tktbk(event):
            def save(a,l):
                q = a.get('1.0', END)
                file = tempfile.mktemp('.txt', '', 'Bills\\')
                open(file, 'w').write(q)
                os.startfile(file, "print")
                c=npas.get()
                d=dtvar.get()
                db=sqlite3.connect("Travel.db")
                for i in range(l+1,l+c+1):                                        
                    crs=db.cursor()
                    crs.execute("Insert into booking Values('{}','{}','{}','{}','{}')".format(fc[0],fc[1],fc[2],i,d))
                    db.commit()
                db.close()
                messagebox.showinfo('Success'," Ticket generated successfully")
                travel(main)

                
                
            def book():
                screen.destroy()
                a=frmVar.get()
                b=toVar.get()
                c=npas.get()
                d=dtvar.get()
                window.geometry('923x580+450+10')
                rtfr=Canvas(mainf,height=580,width=400,bg='grey10')
                rtfr.pack(side=RIGHT)
                textreciept = Text(rtfr,state='normal',width=400,height=450)
                textreciept.place(x=0,y=0)
                textreciept.bind('<Enter>', fun.E_reciept)
                textreciept.bind('<Leave>', fun.L_reciept)                
                mydb=sqlite3.connect("Travel.db")
                crs=mydb.cursor()
                crs.execute(f"Select * from booking where busno='{fc[0]}' AND ftime='{fc[1]}' AND ttime='{fc[2]}' AND date='{d}'")
                data=crs.fetchall()
                l=len(data)
                sts=''
                for i in range(l+1,l+c+1):
                    if i==(l+c):
                        sts+=str(i)
                    else:
                        sts+=str(i)+', '
                tp=float(fc[3])*c
                textreciept.insert(END, "\t\t GOA BUS SERVICE   \t\t\t" + "\n")
                textreciept.insert(END, "\t _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ \t\t\t" + "\n"+"\n")
                textreciept.insert(END, "  Bus No.: "+fc[0]+"\n")
                textreciept.insert(END, "  Date: "+d+"\n")
                textreciept.insert(END, "  From: "+a+"\n")
                textreciept.insert(END, "  To: "+b+"\n")
                textreciept.insert(END, "  Departure: "+fc[1]+"\n")
                textreciept.insert(END, "  Arrival: "+fc[2]+"\n")
                textreciept.insert(END, "  No. of Passengers: "+str(c)+"\n")
                textreciept.insert(END, "  Seats: "+sts+"\n")
                textreciept.insert(END, "  Total Price: Rs."+str(tp)+"\n"+"\n")
                textreciept.insert(END, "\t    ******Thank You******")
                conf=Button(rtfr,text="Confirm Booking",width=24,relief=RIDGE,font=('Imprint MT Shadow', 10,'bold'),bg='DodgerBlue4',fg='snow2',
                  command=lambda: save(textreciept,l))
                conf.place(x=80,y=500)
                conf.bind('<Enter>', fun.btime)
                conf.bind('<Leave>', fun.btimeends)
                
                                
            def cancel():
                screen.destroy()
            value=tree.item(tree.selection())
            fc = value['values']
            screen=Toplevel()
            screen.overrideredirect(1)
            screen.maxsize(200,120)
            screen.geometry('200x120+620+260')            
            vas=Canvas(screen,height=120,width=200,bg='snow2')
            vas.pack()
            vas.create_text(10,10,text="No. of Passengers:",font=('Imprint MT Shadow', 12,'bold'),anchor=W,fill='DodgerBlue4')
            vasetry=Entry(vas,textvariable=npas,font=('Book Antiqua', 12, 'bold'))
            vasetry.place(x=10,y=30)
            bkn=Button(vas,text="Book",font=('Imprint MT Shadow', 12,'bold'),bg='DodgerBlue4',fg='snow2',relief=FLAT,
                  command=book)
            bkn.place(x=10,y=70)
            bkn.bind('<Enter>', fun.btime)
            bkn.bind('<Leave>', fun.btimeends)
            btn=Button(vas,text="Cancel",font=('Imprint MT Shadow', 12,'bold'),bg='DodgerBlue4',fg='snow2',relief=FLAT,
                  command=cancel)
            btn.place(x=105,y=70)
            btn.bind('<Enter>', fun.btime)
            btn.bind('<Leave>', fun.btimeends)

            
        a=frmVar.get().upper()
        b=toVar.get().upper()
        tree= ttk.Treeview(can,height=7)
        tree.place(x=35,y=90)
        style=ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview",background="DodgerBlue4",foreground="snow2",font=('Centaur','15'),
                                rowheight=50,fieldbackground="DodgerBlue3")
        tree["columns"] = ("one", "two","three","four")
        tree.column("#0", width=0,  stretch=NO)
        tree.column("one", width=150, minwidth=150, stretch=NO)
        tree.column("two", width=100, minwidth=100, stretch=NO)
        tree.column("three", width=100, minwidth=100, stretch=NO)
        tree.column("four", width=100, minwidth=100, stretch=NO)
        tree.heading("#0", text="", anchor=W)
        tree.heading("one", text="Bus No.", anchor=W)
        tree.heading("two", text="Departure Time", anchor=W)
        tree.heading("three", text="Arrival Time", anchor=W)
        tree.heading("four", text="Price", anchor=W)
        tree.bind('<Double-Button-1>',tktbk)
        my_db=sqlite3.connect("Travel.db")
        crsr=my_db.cursor()
        crsr.execute(f"Select bsno,ftime,ttime,price from Bus where frm='{a}' and dest='{b}'")
        vl1=crsr.fetchall()
        crsr.execute(f"Select bsno,rftime,rttime,price from Bus where frm='{b}' and dest='{a}'")
        vl2=crsr.fetchall()
        vl1.extend(vl2)
        for i in vl1:
            tree.insert('', END, text='',value=(i[0],i[1],i[2],i[3])) 
                


    main=Frame(window,bg='grey10',bd=2)
    main.pack(fill=BOTH,expand=True)
    mainf=Frame(main,bg='grey10',bd=2)
    mainf.place(relx=0.5,rely=0.5,anchor=CENTER)
    mainfr=Frame(mainf,bg='grey10',height=600,width=523,bd=2)
    mainfr.pack(side=LEFT)
    fr=Frame(mainfr,height=90,bg='DodgerBlue4',relief=RIDGE,bd=2)
    fr.pack(side=TOP,fill='x')
    lbl=Label(fr,text='Goa Bus Service',font=('Broadway','28'),bg='DodgerBlue4',fg='snow2')
    lbl.pack()
    can=Canvas(mainfr,height=530,width=523,bg='snow2')
    can.pack(side=BOTTOM)
    can.create_text(20,30,text='From:',font=('Imprint MT Shadow', 15,'bold'),anchor=W,fill='DodgerBlue4')
    place=["Panjim","Morjim","Candolim","Calangute","Baga","Goa Airport","Colva","Canacona","Arambol"]
    frety=ttk.Combobox(can,value=place,textvariable=frmVar,width=12,font=('Book Antiqua', 12, 'bold'))
    frety.place(x=90,y=15)
    can.create_text(20,70,text='To:',font=('Imprint MT Shadow', 15,'bold'),anchor=W,fill='DodgerBlue4')
    toety=ttk.Combobox(can,value=place,textvariable=toVar,width=12,font=('Book Antiqua', 12, 'bold'))
    toety.place(x=90,y=55)
    can.create_text(270,30,text='Date :',font=('Imprint MT Shadow', 15,'bold'),anchor=W,fill='DodgerBlue4')
    dtvar.set("Select Date")
    bfdtbtn=Entry(can,textvariable=dtvar,font=('Book Antiqua', 12, 'bold'),state=DISABLED,relief=FLAT)
    bfdtbtn.place(x=330,y=20)
    bfdtbtn.bind('<Enter>', fun.showtime)
    bfdtbtn.bind('<Leave>', fun.showtimeends)
    bfdtbtn.bind('<Button-1>', calendar)
    srcbtn=Button(can,text="Search",width=24,relief=RIDGE,font=('Imprint MT Shadow', 10,'bold'),bg='DodgerBlue4',fg='snow2',
                  command=search)
    srcbtn.place(x=270,y=55)
    srcbtn.bind('<Enter>', fun.btime)
    srcbtn.bind('<Leave>', fun.btimeends)
    bbtn=Button(can,text="Back",width=20,relief=RIDGE,font=('Imprint MT Shadow', 10,'bold'),bg='DodgerBlue4',fg='snow2',
                  command=lambda: travel(main))
    bbtn.place(x=170,y=470)
    bbtn.bind('<Enter>', fun.btime)
    bbtn.bind('<Leave>', fun.btimeends)
    treeVw()


def rental(a,b):
    nodvar.set('')

    def srch():
        m=mno.get()
        n=nodvar.get()
        if dtvar.get()=="Select Date" or dname.get()=='' or n=='' or m=='':
            messagebox.showinfo("Warning","Enter all the details to search")          
        else:
            trvw()

    def trvw():
        def tktbk(event):
            def sav(a):
                q = a.get('1.0', END)
                file = tempfile.mktemp('.txt', '', 'Bills\\')
                open(file, 'w').write(q)
                os.startfile(file, "print")
                b=dname.get()
                d=dtvar.get()
                db=sqlite3.connect("Travel.db")                       
                crs=db.cursor()
                crs.execute("Insert into renrec Values('{}','{}','{}')".format(fc[0],d,b))
                db.commit()
                db.close()
                messagebox.showinfo('Success'," Vehicle booking successful")
                dname.set('')
                mno.set('')
                travel(can)


                
            value=tree.item(tree.selection())
            fc = value['values']
            window.geometry('500x750+450+10')
            fl=Canvas(can,width=500,height=350,bg='white')
            fl.pack(side=BOTTOM)
            textreciept = Text(fl,state='normal',width=500,height=300)
            textreciept.place(x=0,y=0)
            textreciept.bind('<Enter>', fun.E_reciept)
            textreciept.bind('<Leave>', fun.L_reciept)            
            textreciept.insert(END, "\t\t\t  GOA TRAVELS\t\t" + "\n")
            textreciept.insert(END, "\t\t_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ \t\t\t" + "\n"+"\n")
            textreciept.insert(END, "   Name: "+dname.get()+"\n")
            textreciept.insert(END, "   Mobile No.: "+mno.get()+"\n")
            textreciept.insert(END, "   Date: "+dtvar.get()+"\n")
            textreciept.insert(END, "   No. of days: "+nodvar.get()+"\n")
            textreciept.insert(END, "   Vehicle No.: "+fc[0]+"\n")
            textreciept.insert(END, "   Company: "+fc[1]+"\n")
            if a==1 or a==2 or a==3:
                textreciept.insert(END, "   Driver: "+genVar.get()+"\n")
            if genVar.get()=='Yes':
                ttl=(float(fc[2])+500)*int(n)
            else:
                ttl=(float(fc[2]))*int(n)
            textreciept.insert(END, "   Total Price: "+"Rs."+str(ttl)+"\n"+"\n")
            textreciept.insert(END, "\t\t   ******Thank You******")
            conf=Button(fl,text="Confirm Booking",width=24,relief=RIDGE,font=('Imprint MT Shadow', 10,'bold'),bg='DarkOrchid4',fg='old lace',
                  command=lambda: sav(textreciept))
            conf.place(x=130,y=310)
            conf.bind('<Enter>', fun.btime1)
            conf.bind('<Leave>', fun.btimeends1)

            
        p=dtvar.get()
        tree= ttk.Treeview(can,height=5)
        tree.place(x=45,y=175)
        style=ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview",background="DarkOrchid4",foreground="old lace",font=('Centaur','10'),
                                rowheight=30,fieldbackground="DarkOrchid2")
        tree["columns"] = ("one", "two","three")
        tree.column("#0", width=0,  stretch=NO)
        tree.column("one", width=150, minwidth=150, stretch=NO)
        tree.column("two", width=150, minwidth=150, stretch=NO)
        tree.column("three", width=100, minwidth=100, stretch=NO)
        tree.heading("#0", text="", anchor=W)
        tree.heading("one", text="Vehicle No.", anchor=W)
        tree.heading("two", text="Company", anchor=W)
        tree.heading("three", text="Price", anchor=W)
        tree.bind('<Double-Button-1>',tktbk)
        m=mno.get()
        n=nodvar.get()
        if dtvar.get()=="Select Date" or dname.get()=='' or n=='' or m=='':
            pass
        else:
            if a==1:
                myd=sqlite3.connect('Travel.db')
                cr=myd.cursor()
                cr.execute(f"Select * from renrec where date='{p}'")
                data1=cr.fetchall()
                cr.execute("Select * from rental where type='SEDAN'")
                data2=cr.fetchall()
                data=[]
                for i in data2:
                    for j in data1:
                        if j[0]==i[0]:
                            continue
                        else:
                            data.append(i)
                if data1==[]:
                    for i in data2:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))
                else:
                    for i in data:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))
            elif a==2:
                myd=sqlite3.connect('Travel.db')
                cr=myd.cursor()
                cr.execute(f"Select * from renrec where date='{p}'")
                data1=cr.fetchall()
                cr.execute("Select * from rental where type='SUV'")
                data2=cr.fetchall()
                data=[]
                for i in data2:
                    for j in data1:
                        if j[0]==i[0]:
                            continue
                        else:
                            data.append(i)

                if data1==[]:
                    for i in data2:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))
                else:
                    for i in data:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))
            elif a==3:
                myd=sqlite3.connect('Travel.db')
                cr=myd.cursor()
                cr.execute(f"Select * from renrec where date='{p}'")
                data1=cr.fetchall()
                cr.execute("Select * from rental where type='MPV'")
                data2=cr.fetchall()
                data=[]
                for i in data2:
                    for j in data1:
                        if j[0]==i[0]:
                            continue
                        else:
                            data.append(i)
                if data1==[]:
                    for i in data2:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))
                else:
                    for i in data:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))

            elif a==4:
                myd=sqlite3.connect('Travel.db')
                cr=myd.cursor()
                cr.execute(f"Select * from renrec where date='{p}'")
                data1=cr.fetchall()
                cr.execute("Select * from rental where type='2-WHEELER'")
                data2=cr.fetchall()
                data=[]
                for i in data2:
                    for j in data1:
                        if j[0]==i[0]:
                            continue
                        else:
                            data.append(i)
                if data1==[]:
                    for i in data2:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))
                else:
                    for i in data:
                        tree.insert('', END, text='',value=(i[0],i[3],i[2]))
                        
        
    def calendar(event):
        screen=Toplevel()
        screen.overrideredirect(1)
        screen.maxsize(210,230)
        screen.geometry('210x230+680+105')
        screen.configure(bg='White',border='1px solid')
        def selectDate():
            myDate=myCal.get_date()
            dtvar.set(myDate)
            t1=myDate.index('/')
            t2=myDate.index('/',3)
            dd=int(myDate[0:t1])
            mm=int(myDate[t1+1:t2])
            yy='20'+myDate[t2+1:len(myDate)]
            yy=int(yy)
            screen.destroy()
        myCal=Calendar(screen,setmode='day',date_pattern='d/m/yy')
        myCal.pack(fill=BOTH)            
        opencal=Button(screen,text="Select Date",command=selectDate)
        opencal.place(x=30,y=195)
        bkcal=Button(screen,text="Cancel",command=lambda: screen.destroy())
        bkcal.place(x=140,y=195)
    b.destroy()
    window.geometry('500x400+450+10')
    can=Canvas(window,width=500,height=750,bg='white')
    can.pack()
    fr=Canvas(can,width=500,height=400,bg='old lace')
    fr.pack(side=TOP)
    fr.create_text(10,5,text="Name:",font=('Imprint MT Shadow', 15,'bold'),anchor=NW,fill='DarkOrchid4')
    fren=Entry(can,textvariable=dname,font=('Book Antiqua', 12, 'bold'),relief=RIDGE)
    fren.place(x=10,y=35)
    fren.bind('<Enter>', fun.showtime)
    fren.bind('<Leave>', fun.showtimeends)
    fr.create_text(230,5,text="Date:",font=('Imprint MT Shadow', 15,'bold'),anchor=NW,fill='DarkOrchid4')
    dtvar.set("Select Date")
    bfdtbtn=Entry(can,textvariable=dtvar,font=('Book Antiqua', 12, 'bold'),state=DISABLED,relief=RIDGE)
    bfdtbtn.place(x=230,y=35)
    bfdtbtn.bind('<Enter>', fun.showtime)
    bfdtbtn.bind('<Leave>', fun.showtimeends)
    bfdtbtn.bind('<Button-1>', calendar)
    fr.create_text(10,80,text="Mobile No.:",font=('Imprint MT Shadow', 15,'bold'),anchor=NW,fill='DarkOrchid4')
    btn1=Entry(can,textvariable=mno,font=('Book Antiqua', 12, 'bold'),relief=RIDGE)
    btn1.place(x=10,y=110)
    btn1.bind('<Enter>', fun.showtime)
    btn1.bind('<Leave>', fun.showtimeends)
    fr.create_text(230,110,text="No. of Days:",font=('Imprint MT Shadow', 15,'bold'),anchor=NW,fill='DarkOrchid4')
    btn=Entry(can,textvariable=nodvar,width=8,font=('Book Antiqua', 12, 'bold'),relief=RIDGE)
    btn.place(x=370,y=110)
    btn.bind('<Enter>', fun.showtime)
    btn.bind('<Leave>', fun.showtimeends)
    srcbtn=Button(can,text="Search",width=24,relief=RIDGE,font=('Imprint MT Shadow', 10,'bold'),bg='DarkOrchid4',fg='old lace',
                  command=srch)
    srcbtn.place(x=140,y=140)
    srcbtn.bind('<Enter>', fun.btime1)
    srcbtn.bind('<Leave>', fun.btimeends1)
    bbtn=Button(can,text="Back",width=20,relief=RIDGE,font=('Imprint MT Shadow', 10,'bold'),bg='DarkOrchid4',fg='old lace',
                  command=lambda: travel(can))
    bbtn.place(x=155,y=360)
    bbtn.bind('<Enter>', fun.btime1)
    bbtn.bind('<Leave>', fun.btimeends1)
    
    if a==1:
        window.title('Sedan')
        fr.create_text(230,80,text="Do you want a driver?",font=('Imprint MT Shadow', 10),anchor=NW,fill='DarkOrchid4')
        detr=OptionMenu(fr,genVar,"Yes","No")
        detr.config(width=8,height=1,bg='white')
        detr.place(x=360,y=70)
    elif a==2:
        window.title('SUV')
        fr.create_text(230,80,text="Do you want a driver?",font=('Imprint MT Shadow', 10),anchor=NW,fill='DarkOrchid4')
        detr=OptionMenu(fr,genVar,"Yes","No")
        detr.config(width=8,height=1,bg='white')
        detr.place(x=360,y=70)
    elif a==3:
        window.title('MPV')
        fr.create_text(230,80,text="Do you want a driver?",font=('Imprint MT Shadow', 10),anchor=NW,fill='DarkOrchid4')
        detr=OptionMenu(fr,genVar,"Yes","No")
        detr.config(width=8,height=1,bg='white')
        detr.place(x=360,y=70)
    elif a==4:
        window.title('2-Wheeler')
    trvw()

    
def travel(a):
    global bgIm
    a.destroy()
    window.geometry('523x600+450+10')
    window.title('Travels')
    cvn=Canvas(window,bg='gold')
    cvn.pack(fill=BOTH,expand=True)
    can=Canvas(cvn,width=516,height=595,bg='white')
    can.place(relx=0.5,rely=0.5,anchor=CENTER)
       
    bgIm=ImageTk.PhotoImage(Image.open(r"road.jpg"))
    can.create_image(0,0,anchor=NW,image=bgIm)
    can.create_text(260,45,text='Travels',font=('Broadway','30'),fill='khaki1')
    clkbt1=Button(can,text=' BUS',font=('Ravie', 15),
                   bg='sandy brown',fg='gold',height=1,width=10,relief=FLAT,command=lambda: bus(cvn))
    clkbt1.place(x=40,y=150)
    clkbt1.bind('<Enter>', fun.opt_btn1)
    clkbt1.bind('<Leave>', fun.opt_ebtn1)
    can.create_text(130,250,text=' RENTAL VEHICLES',font=('Ravie', 15),fill='khaki1',anchor='w')
    c1=1
    ck1=Button(can,text=' SEDAN',font=('Imprint MT Shadow', 10,'bold'),
                   bg='Sky Blue3',fg='gold',height=1,width=15,relief=FLAT,command=lambda: rental(c1,cvn))
    ck1.place(x=190,y=290)
    ck1.bind('<Enter>', fun.opt_btn2)
    ck1.bind('<Leave>', fun.opt_ebtn2)
    c2=2
    ck2=Button(can,text=' SUV',font=('Imprint MT Shadow', 10,'bold'),
                   bg='Sky Blue3',fg='gold',height=1,width=15,relief=FLAT,command=lambda: rental(c2,cvn))
    ck2.place(x=190,y=330)
    ck2.bind('<Enter>', fun.opt_btn2)
    ck2.bind('<Leave>', fun.opt_ebtn2)
    c3=3
    ck3=Button(can,text=' MPV',font=('Imprint MT Shadow', 10,'bold'),
                   bg='Sky Blue3',fg='gold',height=1,width=15,relief=FLAT,command=lambda: rental(c3,cvn))
    ck3.place(x=190,y=370)
    ck3.bind('<Enter>', fun.opt_btn2)
    ck3.bind('<Leave>', fun.opt_ebtn2)
    c4=4
    ck4=Button(can,text=' 2-WHEELER',font=('Imprint MT Shadow', 10,'bold'),
                   bg='Sky Blue3',fg='gold',height=1,width=15,relief=FLAT,command=lambda: rental(c4,cvn))
    ck4.place(x=190,y=410)
    ck4.bind('<Enter>', fun.opt_btn2)
    ck4.bind('<Leave>', fun.opt_ebtn2)
    clkbt3=Button(can,text=' BACK',font=('Ravie', 15),height=1,width=10,
                   bg='sandy brown',fg='gold',relief=FLAT,compound=RIGHT,command=lambda: optionPg(cvn))
    clkbt3.place(x=475,y=500,anchor=NE)
    clkbt3.bind('<Enter>', fun.opt_btn1)
    clkbt3.bind('<Leave>', fun.opt_ebtn1)


###############################Option Page###############################
        
def optionPg(a):
    global mainIm
    a.destroy()
    
    window.geometry('520x700+450+10')

    window.title('Goa Tourism')
    cn=Canvas(window,bg='misty rose')
    cn.pack(fill=BOTH,expand=True)
    can=Canvas(cn,width=520,height=700,bg='white')
    can.place(relx=0.5,rely=0.5,anchor=CENTER)
    mainIm=ImageTk.PhotoImage(Image.open(r"pct2.png"))
    can.create_image(0,0,anchor=NW,image=mainIm)
    can.create_text(260,45,text='Goa Tourism',font=('Broadway','30'),fill='khaki1')
    global clk1,clk2,clk3,clk4
    clk1=PhotoImage(file='review.png')
    clkbtn1=Button(can,text=' Hotels',image=clk1,height=35,width=210,font=('Gabriola', 22,'bold'),
                   bg='misty rose',fg='light pink',relief=FLAT,compound=LEFT,command=lambda: hotel(cn))
    clkbtn1.place(x=40,y=210)
    clkbtn1.bind('<Enter>', fun.opt_btn)
    clkbtn1.bind('<Leave>', fun.opt_ebtn)
    clk2=PhotoImage(file='multiple.png')
    clkbtn2=Button(can,text=' Tour Packages',image=clk2,height=35,width=300,font=('Gabriola', 22,'bold'),
                   bg='misty rose',fg='light pink',relief=FLAT,compound=LEFT,command=lambda: tour(cn))
    clkbtn2.place(x=40,y=280)
    clkbtn2.bind('<Enter>', fun.opt_btn)
    clkbtn2.bind('<Leave>', fun.opt_ebtn)
    clk3=PhotoImage(file='tour-bus.png')
    clkbtn3=Button(can,text=' Travels',image=clk3,height=35,width=210,font=('Gabriola', 22,'bold'),
                   bg='misty rose',fg='light pink',relief=FLAT,compound=LEFT,command=lambda: travel(cn))
    clkbtn3.place(x=40,y=350)
    clkbtn3.bind('<Enter>', fun.opt_btn)
    clkbtn3.bind('<Leave>', fun.opt_ebtn)



###############################LoginPage####################################

def login():
    global emailVar
    global passVar
    global cpassVar
    global nameVar
    global mnoVar
    window.geometry('640x750+400+10')
    
    window.title('Goa Tourism')
    can=Canvas(window,bg='Skyblue1')
    can.pack(fill=BOTH,expand=True)
    canv=Canvas(can,width=640,height=750,bg='white')
    canv.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def logging():
        a=emailVar.get()
        b=passVar.get()
        if a==b=='':
            messagebox.showinfo("Information","Fill the details to login")
        elif a=='':
            messagebox.showinfo("Information","Enter the email")
        elif b=='':
            messagebox.showinfo("Information","Enter the password")
        else:
            mydbs=sqlite3.connect('tourism.db')
            mycrsr=mydbs.cursor()
            qry="select * from login where Email='{}'".format(a)
            mycrsr.execute(qry)
            data = mycrsr.fetchall()
            mydbs.commit()
            mydbs.close()
            if len(data)>0:
                if b==data[0][3]:
                    messagebox.showinfo("Successful","Welcome "+data[0][0])
                    optionPg(can)
                else:
                    messagebox.showinfo("Incorrect Password","Please enter correct password")
            else:
                messagebox.showinfo("Warning","No such user")
                emailVar.set('')
                passVar.set('')
                
    def createAcc(a,b,c,d,aa,bb,cc,dd,ee):
        canv.delete(a,b,c,d)
        aa.place_forget()
        bb.place_forget()
        cc.place_forget()
        dd.place_forget()
        ee.place_forget()
        
        def create():
            a=nameVar.get()
            b=mnoVar.get()
            c=emailVar.get()
            d=passVar.get()
            e=cpassVar.get()
            f=quesVar.get()
            g=ansVar.get()
            if(a==b==c==d==e=='' or a==b==c==d==e==' '):
                messagebox.showinfo("Information","Necessary to fill all the details")
            elif(a=='' or a==' '):
                messagebox.showinfo("Information","Please enter your name")
                name.focus_set()
            elif(b=='' or b==' '):
                messagebox.showinfo("Information","Please enter your mobile no.")
                mno.focus_set()
            elif(c=='' or c==' '):
                messagebox.showinfo("Information","Please enter your email")
                gmail.focus_set()
            elif(d=='' or d==' '):
                messagebox.showinfo("Information","Please enter your password")
                pasS.focus_set()
            elif(e=='' or e==' '):
                messagebox.showinfo("Information","Please enter your password again to confirm")
                cpasS.focus_set()
            elif(f=='' or f==' '):
                messagebox.showinfo("Information","Please enter a security question")
                ques.focus_set()
            elif(g=='' or g==' '):
                messagebox.showinfo("Information","Please enter a security answer")
                ans.focus_set()
            else:
                if len(b)==10:
                    if len(d)>=4:
                        if d==e:
                            mydb=sqlite3.connect('tourism.db')
                            mycr=mydb.cursor()
                            mycr.execute(f"select * from login where Email='{c}'")
                            dtr=mycr.fetchall()
                            mydb.close()
                            if len(dtr)==0:
                                mydb=sqlite3.connect('tourism.db')
                                mycr=mydb.cursor()
                                query="insert into login values('{}','{}','{}','{}','{}','{}')".format(a,b,c,d,f,g)
                                mycr.execute(query)
                                mydb.commit()
                                mydb.close()
                                messagebox.showinfo("Successful","New User Created")
                                messagebox.showinfo("Successful","You are being directed to the Login Page.")
                                Back()
                            else:
                                messagebox.showinfo("Error","User already exists")
                                emailVar.set('')
                                gmail.focus_set()
                        else:
                            messagebox.showinfo("Error","Please enter the same password")
                            cpasS.focus_set()
                    else:
                        messagebox.showinfo("Error","Password should be at least 4 characters")
                        pasS.focus_set()
                else:
                    messagebox.showinfo("Warning","Mobile No. should contain 10 digits only")
                    mno.focus_set()
                
        def Back():
            emailVar.set('')
            passVar.set('')
            cpassVar.set('')
            ansVar.set('')
        
            canv.delete(v1,v2,v3,v4,v5,v6,v7,v8)
            name.place_forget()
            mno.place_forget()
            gmail.place_forget()
            pasS.place_forget()
            cpasS.place_forget()
            creat.place_forget()
            back.place_forget()
            ques.place_forget()
            ans.place_forget()
            logPg()
            
        v1=canv.create_text(120,140,text='Create New Account',font=('9'),fill='white')
        v2=canv.create_text(30,180,text='Name:',font=('Impact','18'),fill='white',anchor='w')
        v3=canv.create_text(30,280,text='Mobile No.:',font=('Impact','18'),fill='white',anchor='w')
        v4=canv.create_text(30,380,text='Email:',font=('Impact','18'),fill='white',anchor='w')
        v5=canv.create_text(30,480,text='Password:',font=('Impact','18'),fill='white',anchor='w')
        v6=canv.create_text(30,580,text='Confirm Password:',font=('Impact','18'),fill='white',anchor='w')
        v7=canv.create_text(320,180,text='Security Question:',font=('Impact','18'),fill='white',anchor='w')
        v8=canv.create_text(320,280,text='Security Answer:',font=('Impact','18'),fill='white',anchor='w')


        def nx1(event):
            mno.focus_set()

        def nx2(event):
            gmail.focus_set()

        def nx3(event):
            pasS.focus_set()

        def nx4(event):
            cpasS.focus_set()
        sqt=["What is your mother's maiden name?","What is your childhood nickname?","What is your birthday date?",
             "In what city where you born?","What is the name of your first school you attended?"]
        name=Entry(canv,textvariable=nameVar,font=('Book Antiqua', 15, 'bold'))
        name.place(x=35,y=195)
        name.bind('<Enter>', fun.showtime)
        name.bind('<Leave>', fun.showtimeends)
        name.bind('<Return>',nx1)
        mno=Entry(canv,textvariable=mnoVar,font=('Book Antiqua', 15, 'bold'))
        mno.place(x=35,y=295)
        mno.bind('<Enter>', fun.showtime)
        mno.bind('<Leave>', fun.showtimeends)
        mno.bind('<Return>',nx2)
        ques=ttk.Combobox(canv,value=sqt,textvariable=quesVar,font=('Book Antiqua', 15, 'bold'))
        ques.place(x=325,y=195)
        ans=Entry(canv,textvariable=ansVar,font=('Book Antiqua', 15, 'bold'))
        ans.place(x=325,y=295)
        ans.bind('<Enter>', fun.showtime)
        ans.bind('<Leave>', fun.showtimeends)
        gmail=Entry(canv,textvariable=emailVar,font=('Book Antiqua', 15, 'bold'))
        gmail.place(x=35,y=395)
        gmail.bind('<Enter>', fun.showtime)
        gmail.bind('<Leave>', fun.showtimeends)
        gmail.bind('<Return>',nx3)
        pasS=Entry(canv,textvariable=passVar,show='*',font=('Book Antiqua', 15, 'bold'))
        pasS.place(x=35,y=495)
        pasS.bind('<Enter>', fun.showtime)
        pasS.bind('<Leave>', fun.showtimeends)
        pasS.bind('<Return>',nx4)
        cpasS=Entry(canv,textvariable=cpassVar,show='*',font=('Book Antiqua', 15, 'bold'))
        cpasS.place(x=35,y=595)
        cpasS.bind('<Enter>', fun.showtime)
        cpasS.bind('<Leave>', fun.showtimeends)
        creat=Button(canv,text='Next', font=('Book Antiqua', 12, 'bold'), bd=1,relief=FLAT,bg='dodger blue',fg='White',
                     width=22, command=create)
        creat.place(x=34,y=625)
        creat.bind('<Enter>', fun.E_lg_login_btn)
        creat.bind('<Leave>', fun.L_lg_login_btn)
        back=Button(canv,text='Back', font=('Book Antiqua', 12, 'bold'), bd=1,relief=FLAT,bg='dodger blue',fg='White',
                     width=22, command=Back)
        back.place(x=34,y=665)
        back.bind('<Enter>', fun.E_lg_login_btn)
        back.bind('<Leave>', fun.L_lg_login_btn)
        

    def logPg():
        global mainImg

        def fgPas():
            
            
            def cnf(a,b):
                if ansVar.get()==dtr[0][5]:
                    a.config(state=NORMAL)
                    b.config(state=NORMAL)
                    messagebox.showinfo("Success","Now enter a new password")
                else:
                    messagebox.showinfo("Error","Wrong security pin entered")

            def save():
                a=dpassVar.get()
                b=cpassVar.get()
                if a!='':
                    if b!='':
                        if a==b:
                            mydb=sqlite3.connect('tourism.db')
                            mycr=mydb.cursor()
                            mycr.execute(f"update login set Password='{a}' where Email='{ml}'")
                            mydb.commit()
                            mydb.close()
                            crt.config(state=NORMAL)
                            log.config(state=NORMAL)
                            messagebox.showinfo("Success","Password changed successfully")
                            vas.destroy()
                        else:
                            messagebox.showinfo("Error","Passwords did not match"+"\n"+"Please enter same passwords")
                    else:
                        messagebox.showinfo("Error","Enter the password to confirm")
                else:
                    messagebox.showinfo("Error","Enter a password")

                
            def back():
                vas.destroy()
                ansVar.set('')
                dpassVar.set('')
                cpassVar.set('')
                crt.config(state=NORMAL)
                log.config(state=NORMAL)
            ml=emailVar.get()
            mydb=sqlite3.connect('tourism.db')
            mycr=mydb.cursor()
            mycr.execute(f"select * from login where Email='{ml}'")
            dtr=mycr.fetchall()
            mydb.close()
            if len(dtr)>0:
                crt.config(state=DISABLED)
                log.config(state=DISABLED)
                vas=Canvas(canv,height=190,width=280,bd=5,bg='#66b4c8')
                vas.place(x=280,y=180)

                spfrm = Frame(vas,  bg='#66b4c8', relief=FLAT,bd=2, height=20)
                spfrm.pack(fill='x', expand=True)

                pfrm = Frame(vas,  bg='#66b4c8', relief=FLAT,bd=2, height=20)
                pfrm.pack(fill='x', expand=True)

                btfrm = Frame(vas,  bg='#66b4c8', relief=FLAT,bd=2, height=20)
                btfrm.pack(fill='x', expand=True)

                sqlb=Label(spfrm,text=" "+dtr[0][4],bg='#66b4c8',fg='white',font=('Impact','10'))
                sqlb.pack(side=TOP,anchor=NW)

                sqent=Entry(spfrm,textvariable=ansVar,width=32,font=('Book Antiqua','12'))
                sqent.pack(after=sqlb,side=LEFT,padx=5)
                sqent.bind('<Enter>', fun.showtime)
                sqent.bind('<Leave>', fun.showtimeends)

                pslb=Label(pfrm,text="New Password:                      ",bg='#66b4c8',fg='white',font=('Impact','12'))
                pslb.grid(row=0,column=0)

                psent=Entry(pfrm,textvariable=dpassVar,show='*',state=DISABLED,font=('Book Antiqua','12'))
                psent.grid(row=0,column=1)

                cpslb=Label(pfrm,text="Confirm Password:               ",bg='#66b4c8',fg='white',font=('Impact','12'))
                cpslb.grid(row=1,column=0)

                cpsent=Entry(pfrm,textvariable=cpassVar,show='*',state=DISABLED,font=('Book Antiqua','12'))
                cpsent.grid(row=1,column=1)

                sqbt=Button(spfrm,text="Confirm",font=('Book Antiqua','9'),relief=FLAT,bg='dodger blue',fg='White',
                            command=lambda: cnf(psent,cpsent))
                sqbt.pack(after=sqent)
                sqbt.bind('<Enter>', fun.E_lg_login_btn)
                sqbt.bind('<Leave>', fun.L_lg_login_btn)

                sv=Button(btfrm,text="Save",width=15,font=('Book Antiqua','12'),relief=FLAT,bg='dodger blue',fg='White',command=save)
                sv.grid(row=0,column=0)
                sv.bind('<Enter>', fun.E_lg_login_btn)
                sv.bind('<Leave>', fun.L_lg_login_btn)

                bk=Button(btfrm,text="Back",width=15,font=('Book Antiqua','12'),relief=FLAT,bg='dodger blue',fg='White',command=back)
                bk.grid(row=0,column=1,padx=(12,0))
                bk.bind('<Enter>', fun.E_lg_login_btn)
                bk.bind('<Leave>', fun.L_lg_login_btn)

                         
            else:
                messagebox.showinfo("Information","Please enter the correct email first")

                

            
        def nxtfrm(event):
            pas.focus_set()

        def nxtfrmlg(event):
            logging()
        mainImg=ImageTk.PhotoImage(Image.open(r"pct1.png"))
        canv.create_image(0,0,anchor=NW,image=mainImg)
        canv.create_text(305,45,text='Goa Tourism',font=('Colonna MT','35'),fill='khaki1')
        canv.create_text(175,60,text='*****',font=('Centaur','11'),fill='khaki1')
        canv.create_text(423,66,text='*****',font=('Centaur','11'),fill='khaki1')
        canv.create_line(190,60,440,60,fill='khaki1',width=2)
        canv.create_line(160,65,410,65,fill='khaki1',width=2)        
        t1=canv.create_text(140,150,text='Login or create an account',font=('8'),fill='white')
        t2=canv.create_text(60,200,text='Email:',font=('Impact','18'),fill='white')
        t3=canv.create_text(80,300,text='Password:',font=('Impact','18'),fill='white')
        t4=canv.create_text(140,650,text="Don't have an account yet?",font=('8'),fill='white')
        
        email=Entry(canv,textvariable=emailVar,font=('Book Antiqua', 15, 'bold'))
        email.place(x=35,y=220)
        email.bind('<Enter>', fun.showtime)
        email.bind('<Leave>', fun.showtimeends)
        email.bind('<Return>', nxtfrm)
        email.focus_set()
        
        pas=Entry(canv,textvariable=passVar,show='*',font=('Book Antiqua', 15, 'bold'))
        pas.place(x=35,y=320)
        pas.bind('<Enter>', fun.showtime)
        pas.bind('<Leave>', fun.showtimeends)
        pas.bind('<Return>', nxtfrmlg)
        log=Button(canv,text='Log In', font=('Book Antiqua', 12, 'bold'), bd=1,relief=FLAT,bg='dodger blue',fg='White',
                         width=22, command=logging)
        log.place(x=34,y=355)
        log.bind('<Enter>', fun.E_lg_login_btn)
        log.bind('<Leave>', fun.L_lg_login_btn)

        flog=Button(canv,text='Forgot Password', font=('Book Antiqua', 12, 'bold'), bd=1,relief=FLAT,bg='dodger blue',fg='White',
                         width=22, command=fgPas)
        flog.place(x=34,y=395)
        flog.bind('<Enter>', fun.E_lg_login_btn)
        flog.bind('<Leave>', fun.L_lg_login_btn)
       
        crt=Button(canv,text='Create Account', font=('Book Antiqua', 12, 'bold'), bd=1,relief=FLAT,bg='dodger blue',fg='White',
                         width=22, command=lambda:createAcc(t1,t2,t3,t4,email,pas,log,crt,flog))
        crt.place(x=34,y=670)
        crt.bind('<Enter>', fun.E_lg_login_btn)
        crt.bind('<Leave>', fun.L_lg_login_btn)
    logPg()
    window.mainloop()
    

login()
