from tkinter import *

root=Tk()

root.geometry("1500x700")
root.title("Foodie")

expression=""

"""def clear():
    global expression
    expression=""
    displayvalue.set(expression)

def equal():
    global expression
    result=str(eval(expression))
    displayvalue.set(result)

def btnclick(num):
    global expression
    expression += str(num)
    displayvalue.set(expression)
"""



totalprice=0


gstsum=0

totalsum=0

order=1

def TotalOrder():
    global totalprice
    global gstsum
    global totalsum
    eggrolltotal=int(eggroll.get())*25
    chowmeintotal=int(chowmein.get())*30
    momostotal=int(momos.get())*40
    idlitotal=int(idli.get())*30
    dosatotal=int(dosa.get())*60
    burgertotal=int(burger.get())*40
    cutlettotal=int(cutlet.get())*40
    pastrytotal=int(pastry.get())*20

    totalprice=eggrolltotal+chowmeintotal+momostotal+idlitotal+dosatotal+burgertotal+cutlettotal+pastrytotal
    subtotal.set(totalprice)

    gstsum=totalprice*5/100
    gst.set(gstsum)


    totalsum=totalprice+gstsum
    total.set(totalsum)
    
    

def CloseApp():
    root.destroy()
    
def clearitem():
    global expression
    expression="0"
    eggroll.set(expression)
    chowmein.set(expression)
    momos.set(expression)
    idli.set(expression)
    dosa.set(expression)
    burger.set(expression)
    cutlet.set(expression)
    pastry.set(expression)
    subtotal.set(expression)
    gst.set(expression)
    total.set(expression)


def gstitem():
    global gst
    gst=(totalprice*5)/100
    gst.set(gst)

def Reset():
    global order
    global expression
    expression="0"
    eggroll.set(expression)
    chowmein.set(expression)
    momos.set(expression)
    idli.set(expression)
    dosa.set(expression)
    burger.set(expression)
    cutlet.set(expression)
    pastry.set(expression)
    subtotal.set(expression)
    gst.set(expression)
    total.set(expression)

    order+=1
    orderid.set(order)

def price():
    child=Tk(root)
    child.mainloop()



###########     HEADING     #############

Top = Frame(root,width=1600,height=100)
Top.pack(side=TOP)

Left=Frame(root,width=900,height=800)
Left.pack(side=LEFT)

Right=Frame(root,width=640,height=800)
Right.pack(side=RIGHT,padx=10)


brand=Label(Top,text="FOODIE",fg='steel blue',anchor='center',font=('Arial',40,"bold"))
brand.grid(row=0,column=0)

slug=Label(Top,text='Taste The World',font=('Arial',22),fg='grey',anchor='n')
slug.grid(row=1,column=0)



#############################           RECIPIE     #######################################################

eggroll=StringVar()
eggroll.set('0')
chowmein=StringVar()
chowmein.set('0')
momos=StringVar()
momos.set('0')
idli=StringVar()
idli.set('0')
dosa=StringVar()
dosa.set('0')
burger=StringVar()
burger.set('0')
tikka=StringVar()
tikka.set('0')
cutlet=StringVar()
cutlet.set('0')
pastry=StringVar()
pastry.set('0')
subtotal=StringVar()
subtotal.set("0")
orderid=StringVar()
orderid.set("1")
gst=StringVar()
gst.set("0")
total=StringVar()
total.set("0")

eggroll_label=Label(Left,text='Eggroll',fg='steel blue',font=('Arial',20),bd=10)
chowmein_label=Label(Left,text='Chowmein',fg='steel blue',font=('Arial',20),bd=10)
momos_label=Label(Left,text='Momos',fg='steel blue',font=('Arial',20),bd=10)
idli_label=Label(Left,text='Idli',fg='steel blue',font=('Arial',20),bd=10)
dosa_label=Label(Left,text='Dosa',fg='steel blue',font=('Arial',20),bd=10)
burger_label=Label(Left,text='Burger',fg='steel blue',font=('Arial',20),bd=10)
cutlet_label=Label(Left,text='Cutlet',fg='steel blue',font=('Arial',20),bd=10)
pastry_label=Label(Left,text='Pastry',fg='steel blue',font=('Arial',20),bd=10)

eggroll_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=eggroll,justify=RIGHT)
chowmein_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=chowmein,justify=RIGHT)
momos_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=momos,justify=RIGHT)
idli_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=idli,justify=RIGHT)
dosa_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=dosa,justify=RIGHT)
burger_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=burger,justify=RIGHT)
cutlet_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=cutlet,justify=RIGHT)
pastry_entry=Entry(Left,font=('Arial',16),bd=6,textvariable=pastry,justify=RIGHT)

eggroll_label.grid(row=0,column=0)
eggroll_entry.grid(row=0,column=1)

chowmein_label.grid(row=0,column=2)
chowmein_entry.grid(row=0,column=3)

momos_label.grid(row=1,column=0)
momos_entry.grid(row=1,column=1)

idli_label.grid(row=1,column=2)
idli_entry.grid(row=1,column=3)

dosa_label.grid(row=2,column=0)
dosa_entry.grid(row=2,column=1)

burger_label.grid(row=2,column=2)
burger_entry.grid(row=2,column=3)

cutlet_label.grid(row=3,column=0)
cutlet_entry.grid(row=3,column=1)

pastry_label.grid(row=3,column=2)
pastry_entry.grid(row=3,column=3)



###############################     BUTTON      ###############################

totalbutton=Button(Left,text='Total',bd=7,width=13,height=2,font=('Arial',18),command=TotalOrder)
##pricebutton=Button(Left,text='Price',bd=7,width=13,height=2,font=('Arial',18))
clearbutton=Button(Left,text='Clear',bd=7,width=13,height=2,font=('Arial',18),command=clearitem)
exitsbutton=Button(Left,text='Exit',bd=7,width=13,height=2,font=('Arial',18),command=CloseApp)
resetbutton=Button(Left,text='Reset',bd=8,font=('Arial',25),width=20,bg='yellow',command=Reset)

##pricebutton.grid(row=4,column=0,padx=10)
totalbutton.grid(row=4,column=1,padx=10)
clearbutton.grid(row=4,column=2,padx=10)
exitsbutton.grid(row=4,column=3,padx=10)
resetbutton.grid(row=5,column=1,columnspan=3,pady=30,ipadx=15)



###############################     RIGHT       #####################################


subtotalEntry=Entry(Right,justify=RIGHT,width=20,font=('Arial',16),bd=4,textvariable=subtotal)
subtotalLabel=Label(Right,text='Subtotal',width=7,font=('Arial',20))

gstEntry=Entry(Right,justify=RIGHT,width=20,font=('Arial',16),bd=4,textvariable=gst)
gstLabel=Label(Right,text='GST(5%)',width=10,font=('Arial',17))

orderidEntry=Entry(Right,justify=RIGHT,width=20,font=('Arial',16),bd=4,textvariable=orderid)
orderidLabel=Label(Right,text='Order ID',width=7,font=('Arial',20))

totalEntry=Entry(Right,justify=RIGHT,width=20,font=('Arial',16),bd=4,textvariable=total)
totalLabel=Label(Right,text='Total',width=7,font=('Arial',20))


subtotalLabel.grid(row=0,column=0,padx=10,pady=10)
subtotalEntry.grid(row=0,column=1,padx=4,pady=10)

gstLabel.grid(row=1,column=0,pady=10)
gstEntry.grid(row=1,column=1,pady=10)

orderidLabel.grid(row=2,column=0,pady=10)
orderidEntry.grid(row=2,column=1,pady=10)

totalLabel.grid(row=3,column=0,pady=10)
totalEntry.grid(row=3,column=1,pady=10)





##root.attributes("-fullscreen",True)
root.mainloop()