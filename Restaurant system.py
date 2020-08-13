from tkinter import *
from tkinter.filedialog import asksaveasfile
import requests
from tkinter import simpledialog
from tkinter import messagebox
screen=Tk()
screen.geometry("900x600")
screen.title("Restaurant Counter System")
screen.configure(bg="brown")
def UIcreator(column,entries,amountlist,x1,x2,heading):
    Label(screen,width=20,height=20,fg="brown",borderwidth=3,relief="sunken").place(relx=x1-0.01,x=-2,y=100)
    Label(screen,text=heading,font=("Times New Roman",20),fg="brown").place(relx=x1+0.015,x=-2,y=90)
    for i in column:
        entries[i]=Entry(screen,state="disabled",font=("Times New Roman",10),text=amountlist[i][0],width=5)    
        x=Checkbutton(screen,command=update,font=("Times New Roman",10,"bold"),text=column[i][1],variable=column[i][0],onvalue=True,offvalue=False)
        x.place(relx=x1,x=2,y=column1[i][2])
        entries[i].place(relx=x2,x=-2,y=column1[i][2])
def foodcost(column,columnamount):
    s1=0
    for i in column:
        if column[i][0].get()==True:
            s1+=columnamount[i][0].get()*columnamount[i][1]
    return s1
def resetoptions():
    for i in column1:
        column1[i][0].set(False)
        column2[i][0].set(False)
        column3[i][0].set(False)
        column1entries[i].configure(state="disabled")
        column2entries[i].configure(state="disabled")
        column3entries[i].configure(state="disabled")
    for i in amounts:
        for j in amounts[i]:
            amounts[i][j][0].set(0)
def billings():
    sum1.set(foodcost(column1,amounts["column1"]))
    sum2.set(foodcost(column2,amounts["column2"]))
    sum3.set(foodcost(column3,amounts["column3"]))
    sum4.set(sum1.get()+sum2.get()+sum3.get())
    sum5.set(0.18*sum4.get())
    sum6.set(sum4.get()+sum5.get())
def check(column,entries):
    for i in column:
        if column[i][0].get()==True:
            entries[i].configure(state="normal")
        elif  column[i][0].get()==False:
            entries[i].configure(state="disabled")
def savefile():
    text="\t\t\t\t\t\tTHE BIG BITE RESTURAUNT\n\nS.No|  ITEM NAME  | QUANTITY | PRICE(in Rs) |"
    file=asksaveasfile(filetype=[("Text Document","*.txt")],defaultextension = "*.txt")
    file.write(text)
    count=1
    for i in column1:
        if column1[i][0].get()==True:
            file.write(f"\n {count}  |	{column1[i][1]}	  |	{amounts['column1'][i][0].get()}     |	{amounts['column1'][i][0].get()*amounts['column1'][i][1]}    	|")
            count+=1
        if column2[i][0].get()==True:
            file.write("\n {}    |	{}	  |	{}     |	{}    	    |".format(count,column2[i][1],amounts['column2'][i][0].get(),amounts['column2'][i][0].get()*amounts['column2'][i][1]))
            count+=1
        if column3[i][0].get()==True:
            file.write(f" \n{count}  |	{column3[i][1]}	  |	{amounts['column3'][i][0].get()}     |	{amounts['column3'][i][0].get()*amounts['column3'][i][1]}    	    |")
            count+=1
    file.write(f"\n\nTotal Cost:-Rs{sum4.get()}\nGST Percentage:-18%\nGST Cost:-Rs{sum5.get()}\nGrand Total:-Rs{sum6.get()}")
def messages():
    phonenumber=simpledialog.askinteger("User details","Enter your Phone number")
    try:
        text="\t\t\t\t\t\tTHE BIG BITE RESTURAUNT\n\nS.No|  ITEM NAME  | QUANTITY | PRICE(in Rs) |"
        count=1
        for i in column1:
            if column1[i][0].get()==True:
                text+=f"\n {count}  |	{column1[i][1]}	  |	{amounts['column1'][i][0].get()}     |	{amounts['column1'][i][0].get()*amounts['column1'][i][1]}    	|"
                count+=1
            if column2[i][0].get()==True:
                text+=("\n {}    |	{}	  |	{}     |	{}    	    |".format(count,column2[i][1],amounts['column2'][i][0].get(),amounts['column2'][i][0].get()*amounts['column2'][i][1]))
                count+=1
            if column3[i][0].get()==True:
                text+=f" \n{count}  |	{column3[i][1]}	  |	{amounts['column3'][i][0].get()}     |	{amounts['column3'][i][0].get()*amounts['column3'][i][1]}    	    |"
                count+=1
        url = "https://www.fast2sms.com/dev/bulk"
        payload=f"sender_id=FSTSMS&message={text}&language=english&route=p&numbers={phonenumber}"
        headers = {'authorization': "CEFRHdl6c81a7Z04zwhMqSUBDWYNmjI3pn2GQ9kTVrvbeKyPLxbC7HpUVnstBw1l94rOJLNdciYqejZo",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache"}
        response = requests.request("POST", url, data=payload, headers=headers)
    except:
        messagebox.showerror("Error","Enter valid number")
def update():
    check(column1,column1entries)
    check(column2,column2entries)
    check(column3,column3entries)
Label(screen,text="The BIG BITE Resturaunt",fg="yellow",bg="brown",font=("Times New Roman",30),borderwidth=3,relief="sunken").place(relx=0.2,x=-2,y=10)
global column1,column2,column3,column1entries,column2entries,column3entries
column1={1:[BooleanVar(),"Roti",120],2:[BooleanVar(),"Daal",150],3:[BooleanVar(),"Fish",180],4:[BooleanVar(),"Sabji",210],5:[BooleanVar(),"Kebab",240],6:[BooleanVar(),"Rice",270],7:[BooleanVar(),"Mutton",300],8:[BooleanVar(),"Paneer",330],9:[BooleanVar(),"Chicken",360]}
column2={1:[BooleanVar(),"Lassi",120],2:[BooleanVar(),"Coffee",150],3:[BooleanVar(),"Faluda",180],4:[BooleanVar(),"Shikanji",210],5:[BooleanVar(),"Jal-jeera",240],6:[BooleanVar(),"Tea",270],7:[BooleanVar(),"Juice",300],8:[BooleanVar(),"Milk",330],9:[BooleanVar(),"Pepsi",360]}
column3={1:[BooleanVar(),"Oreo",120],2:[BooleanVar(),"Apple",150],3:[BooleanVar(),"Kitkat",180],4:[BooleanVar(),"Vanilla",210],5:[BooleanVar(),"Banana",240],6:[BooleanVar(),"Brownie",270],7:[BooleanVar(),"Litchi",300],8:[BooleanVar(),"Mango",330],9:[BooleanVar(),"Rainbow",360]}
column1entries,column2entries,column3entries={},{},{}
amounts={"column1":{1:[IntVar(),5],2:[IntVar(),20],3:[IntVar(),85],4:[IntVar(),30],5:[IntVar(),70],6:[IntVar(),20],7:[IntVar(),100],8:[IntVar(),60],9:[IntVar(),60]},"column2":{1:[IntVar(),40],2:[IntVar(),30],3:[IntVar(),30],4:[IntVar(),30],5:[IntVar(),20],6:[IntVar(),10],7:[IntVar(),60],8:[IntVar(),30],9:[IntVar(),20]},"column3":{1:[IntVar(),200],2:[IntVar(),200],3:[IntVar(),250],4:[IntVar(),300],5:[IntVar(),250],6:[IntVar(),400],7:[IntVar(),350],8:[IntVar(),400],9:[IntVar(),450]}}
UIcreator(column1,column1entries,amounts["column1"],0.06,0.15,"Food")
UIcreator(column2,column2entries,amounts["column2"],0.26,0.35,"Drinks")
UIcreator(column3,column3entries,amounts["column3"],0.46,0.55,"cakes")
global sum1,sum2,sum3,sum4,sum5,sum6
sum1,sum2,sum3,sum4,sum5,sum6=DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()
Label(screen,text="Cost of Food",font=("Times New Roman",15),bg="brown").place(relx=0.05,x=-2,y=450)
Entry(screen,state="readonly",text=sum1,font=("Times New Roman" ,15),borderwidth=3,relief="sunken").place(relx=0.189,x=-2,y=450)
Label(screen,text="Cost of Drinks",font=("Times New Roman",15),bg="brown").place(relx=0.05,x=-2,y=490)
Entry(screen,state="readonly",text=sum2,font=("Times New Roman" ,15),borderwidth=3,relief="sunken").place(relx=0.19,x=-2,y=490)
Label(screen,text="Cost of Cakes",font=("Times New Roman",15),bg="brown").place(relx=0.05,x=-2,y=530)
Entry(screen,state="readonly",text=sum3,font=("Times New Roman" ,15),borderwidth=3,relief="sunken").place(relx=0.19,x=-2,y=530)
Label(screen,text="Total Cost",font=("Times New Roman",15),bg="brown").place(relx=0.45,x=-2,y=450)
Entry(screen,text=sum4,font=("Times New Roman",15),borderwidth=3,relief="sunken").place(relx=0.589,x=-2,y=450)
Label(screen,text="GST Cost",font=("Times New Roman",15),bg="brown").place(relx=0.45,x=-2,y=490)
Entry(screen,text=sum5,font=("Times New Roman",15),borderwidth=3,relief="sunken").place(relx=0.589,x=-2,y=490)
Label(screen,text="Grand Total",font=("Times New Roman",15),bg="brown").place(relx=0.45,x=-2,y=530)
Entry(screen,text=sum6,font=("Times New Roman",15),borderwidth=3,relief="sunken").place(relx=0.589,x=-2,y=530)
Button(screen,text="Submit",command=billings,font=("Times New Roman" , 10)).place(relx=0.8,x=-2,y=570)
Button(screen,text="Reset",command=resetoptions,font=("Times New Roman" , 10)).place(relx=0.875,x=-2,y=570)
Button(screen,text="Save Bill",command=savefile,font=("Times New Roman", 10)).place(relx=0.575,x=-2,y=570)
Button(screen,text="send message",command=messages,font=("Times New Roman",10)).place(relx=0.65,x=-2,y=570)
mainloop()
