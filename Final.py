# Added expenses and udhaari spreadsheets and update function
# Beautified the GUI with ttkthemes and adjusted spaces using padx and pady 
import os
from tkinter import * 
from tkinter import ttk
import pandas as pd

import datetime
import tkinter.messagebox

from tkinter import filedialog
from ttkthemes import themed_tk as tk
from tkinter import font as tkFont

#reading different csv files 

df = pd.read_csv("Sales_Data.csv", parse_dates = ["Date"], index_col = "Date") 
df = df.fillna(0)

df2 = pd.read_csv("Udhaari.csv", parse_dates = ["Date"], index_col = "Date") 
df2 = df2.fillna(0)

df3 = pd.read_csv("Expenses.csv", parse_dates = ["Date"], index_col = "Date") 
df3 = df3.fillna(0)


No_of_bills_in_a_day=1
date = datetime.datetime.now().strftime("%Y-%m-%d")
#______________________________________________________________________________
""" Defining the Window """

root = tk.ThemedTk() 
root.get_themes()
root.set_theme("clam")
# themes that can be used- smog, radiance, vista, winxpblue,classic,clam,breeze,


root.title("Billing Software-MH") 
root.iconbitmap(r'images/icon.ico')





# Defining the Main Heading of Software

Tops = Frame(root,bg='orange',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='MAGGI HOUSE',bd=21,bg='black',fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)
#______________________________________________________________________________
""" Status Bar """


statusbar = ttk.Label(root)
statusbar.pack(side=BOTTOM, fill=X)


def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    statusbar.config(text="Mongia's"+   180*" "  + time, relief=SUNKEN, anchor=W, font = 'Times 10 italic')
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms
clock()

#______________________________________________________________________________
""" Creating the MENU BAR """

menubar = Menu(root)
root.config(menu=menubar)


#______________________________________________________________________________
""" SubMenu 1 - File """

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)    


#______________________________________________________________________________
""" File - Option Expenses """

def add_expenses_to_csv(name,amount):
    
    global date
    df3.loc[date,name]= df3.loc[date,name] +amount


def submit_exp():
    veg_exp = int(vegitables.get())
    add_expenses_to_csv("Vegetables",veg_exp)

    
    raw_exp = int(raw_materials.get())
    add_expenses_to_csv("Raw Materials",raw_exp)

    
    bake_exp = int(bakery.get())
    add_expenses_to_csv("Bakery",bake_exp)

    
    nood_exp = int(noodles.get())
    add_expenses_to_csv("Noodles(pkt)",nood_exp)

    
    
    gas_exp = int(cylinder.get())
    add_expenses_to_csv("Gas",gas_exp)
    

    home_exp = int(home.get())
    add_expenses_to_csv("Home Expenses",home_exp)

    
    other_exp = int(other.get())
    add_expenses_to_csv("Other Expenses",other_exp)

    
    
    df3.to_csv("Expenses.csv",date_format="%Y-%m-%d") 
    
    # Again setting values to 0 after pressing submit
    vegitables.set("0")
    raw_materials.set("0")
    bakery.set("0")
    noodles.set("0")
    cylinder.set("0")
    home.set("0")    
    other.set("0")


# defining variables
vegitables=StringVar()
raw_materials = StringVar()
bakery = StringVar()
noodles = StringVar()
cylinder = StringVar()
home = StringVar()
other = StringVar()



def Expenses():
    
    
    newWindow_expenses = tkinter.Toplevel(root)    

    
    veg=Label(newWindow_expenses,text='Vegetables            :   Rs ')
    vegitables.set("0")
    e1=tkinter.Entry(newWindow_expenses,textvariable=vegitables)
    veg.grid(row=2,column=0,padx=5,pady=5)
    e1.grid(row=2,column=1,padx=5,pady=5)
    e1.focus_set()  
    e1.icursor(1)
    
    
    raw=Label(newWindow_expenses,text='Raw Materials      :   Rs ')
    raw_materials.set("0")
    e2=tkinter.Entry(newWindow_expenses,textvariable=raw_materials)
    raw.grid(row=3,column=0,padx=5,pady=5)
    e2.grid(row=3,column=1,padx=5,pady=5)
    e2.icursor(1)
    
    
    bake=Label(newWindow_expenses,text='Bakery                  :   Rs ')
    bakery.set("0")
    e3=tkinter.Entry(newWindow_expenses,textvariable=bakery)
    bake.grid(row=4,column=0,padx=5,pady=5)
    e3.grid(row=4,column=1,padx=5,pady=5)
    e3.icursor(1)  
    
    
    noodle=Label(newWindow_expenses,text='Noodles                :   Pkt ')
    noodles.set("0")
    e4=tkinter.Entry(newWindow_expenses,textvariable=noodles)
    noodle.grid(row=5,column=0,padx=5,pady=5)
    e4.grid(row=5,column=1,padx=5,pady=5)
    e4.icursor(1)  
    
    
    cyl=Label(newWindow_expenses,text='Gas                       :   Rs ')
    cylinder.set("0")
    e5=tkinter.Entry(newWindow_expenses,textvariable=cylinder)
    cyl.grid(row=6,column=0,padx=5,pady=5)
    e5.grid(row=6,column=1,padx=5,pady=5)
    e5.icursor(1)
    
    
    house=Label(newWindow_expenses,text='Home Expenses   :   Rs ')
    home.set("0")
    e6=tkinter.Entry(newWindow_expenses,textvariable=home)
    house.grid(row=7,column=0,padx=5,pady=5)
    e6.grid(row=7,column=1,padx=5,pady=5)
    e6.icursor(1)
    
    others=Label(newWindow_expenses,text='Other Expenses  :   Rs ')
    other.set("0")
    e7=tkinter.Entry(newWindow_expenses,textvariable=other)
    others.grid(row=8,column=0,padx=5,pady=5)
    e7.grid(row=8,column=1,padx=5,pady=5)
    e7.icursor(1)
    
    
    
    
    



    newBtn = ttk.Button(newWindow_expenses,text = "Submit",command=submit_exp)
    newBtn.grid(row=9,column=2,padx=10)
    
    
    
#______________________________________________________________________________
""" File - Option Udhari """


def add_udhaari_to_csv(name,amount):
    
    global date
    df2.loc[date,name]= df2.loc[date,name] +amount


def submit_udhari():
    amul_udh = int(Amul.get())
    add_udhaari_to_csv("Amul",amul_udh)
    
    sunny_bakery_udh = int(Sunny_bakery.get())
    add_udhaari_to_csv("Sunny Bakery",sunny_bakery_udh)
 
    df2.to_csv("Udhaari.csv",date_format="%Y-%m-%d")  
    
    Amul.set("0")
    Sunny_bakery.set("0")


# Defining Variables
Amul=StringVar()
Sunny_bakery = StringVar()


def Udhari():
    
    
    newWindow_udhari = tkinter.Toplevel(root)    

    
    amul_label=Label(newWindow_udhari,text='Amul                 :   Rs ')
    Amul.set("0")
    e1=tkinter.Entry(newWindow_udhari,textvariable=Amul)
    amul_label.grid(row=2,column=0,padx=5,pady=5)
    e1.grid(row=2,column=1,padx=5,pady=5)
    e1.focus_set()  
    e1.icursor(1)
    
    
    Sunny_bakery_label=Label(newWindow_udhari,text='Sunny Bakery      :   Rs ')
    Sunny_bakery.set("0")
    e2=tkinter.Entry(newWindow_udhari,textvariable=Sunny_bakery)
    Sunny_bakery_label.grid(row=3,column=0,padx=5,pady=5)
    e2.grid(row=3,column=1,padx=5,pady=5)
    e2.icursor(1)
    

    newBtn = ttk.Button(newWindow_udhari,text = "Submit",command=submit_udhari)
    newBtn.grid(row=5,column=2,padx=10)
        
    

#______________________________________________________________________________
""" Dropdown of File """


subMenu.add_command(label="Expenses", command = Expenses)
subMenu.add_command(label="Udhari", command = Udhari)
subMenu.add_command(label="Exit", command=root.destroy)


#______________________________________________________________________________
""" SubMenu 2 - Help """

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help",menu=subMenu)

def about_us():
    tkinter.messagebox.showinfo('Maggi House','This is a Billing Software made by Vishesh Mongia.')
subMenu.add_command(label="About Us", command = about_us)


#______________________________________________________________________________
""" Left Frame """

leftframe = Frame(root)
leftframe.pack(side=LEFT,padx=30,pady=30)

#______________________________________________________________________________
""" Icons of left frame """

#______________________________________________________________________________
""" Burger """

# Cream Burger
def cream_burger():
    price = 30
    qty = int(qnt.get())
    
    add_to_playlist("Cream Burger", price,qty)
    qnt.set("0")
 
# Cheese Burger
def cheese_burger():
    price = 100  
    qty = int(qnt.get())
    
    add_to_playlist("Cheese Burger", price,qty)
    qnt.set("0")
       
# New window which will pop up on clicking on Burger
def createNewWindow_burger():
    newWindow_burger = tkinter.Toplevel(root)
    burgerBtn = ttk.Button(newWindow_burger,text="Cream Burger             30",command = cream_burger)#Length = 20
    burgerBtn.grid(row=0,column=0,padx=10)
    cheeseBtn = ttk.Button(newWindow_burger,text="Cheese Burger          100",command = cheese_burger)
    cheeseBtn.grid(row=1,column=0,padx=10)
    

        
burgerPhoto = PhotoImage(file='images/burger.png')
burgerBtn = ttk.Button(leftframe,image=burgerPhoto,command=createNewWindow_burger)
burgerBtn.grid(row=0,column=0,padx=10)

#______________________________________________________________________________
""" Dosa """

# Cream Burger
def masala_dosa():
    price = 70
    qty = int(qnt.get())
    
    add_to_playlist("Masala Dosa", price,qty)
    qnt.set("0")
 
# Cheese Burger
def plain_dosa():
    price = 60  
    qty = int(qnt.get())
    
    add_to_playlist("Plain Dosa", price, qty)
    qnt.set("0")
       
# New window which will pop up on clicking on Burger
def createNewWindow_dosa():
    newWindow_dosa = tkinter.Toplevel(root)
    
    masala_dosa_Btn = ttk.Button(newWindow_dosa,text="Masala Dosa              70",command = masala_dosa)#Length = 20
    masala_dosa_Btn.grid(row=0,column=0,padx=10)
    
    plain_dosa_Btn = ttk.Button(newWindow_dosa,text="Plain Dosa                  60",command = plain_dosa)
    plain_dosa_Btn.grid(row=1,column=0,padx=10)
    
dosaPhoto = PhotoImage(file='images/dosa.png')
dosaBtn = ttk.Button(leftframe, image=dosaPhoto,command=createNewWindow_dosa)
dosaBtn.grid(row=0,column=1,padx=10)


#______________________________________________________________________________
""" Noodles """

# Cream Burger
def veg_chowmein():
    price = 70
    qty = int(qnt.get())
    
    add_to_playlist("Veg Chowmein", price,qty)

    qnt.set("0")
 
# Cheese Burger
def singapuri_chowmein():
    price = 100 
    qty = int(qnt.get())
    
    add_to_playlist("Singapuri Chowmein", price,qty)

    qnt.set("0")
       
# New window which will pop up on clicking on Burger
def createNewWindow_chowmein():
    newWindow_chowmein = tkinter.Toplevel(root)
    
    veg_chowmein_Btn = ttk.Button(newWindow_chowmein,text="Veg Chowmein              70",command = veg_chowmein)#Length = 28
    veg_chowmein_Btn.grid(row=0,column=0,padx=10)
    
    singapuri_chowmein_Btn = ttk.Button(newWindow_chowmein,text="Singapuri Chowmein    100",command = singapuri_chowmein)
    singapuri_chowmein_Btn.grid(row=1,column=0,padx=10)
    
    
noodlesPhoto = PhotoImage(file='images/noodles.png')
noodlesBtn = ttk.Button(leftframe, image=noodlesPhoto,command = createNewWindow_chowmein)
noodlesBtn.grid(row=0,column=2,padx=10)

shakesPhoto = PhotoImage(file='images/shakes.png')
shakesBtn = ttk.Button(leftframe, image=shakesPhoto)
shakesBtn.grid(row=1,column=0,padx=10)

snacksPhoto = PhotoImage(file='images/snacks.png')
snacksBtn = ttk.Button(leftframe, image=snacksPhoto)
snacksBtn.grid(row=1,column=1,padx=10)


#______________________________________________________________________________
""" Quantity """

qnt=StringVar()

quan=Label(leftframe,text='Quantity :')
e2=tkinter.Entry(leftframe,width=15,bd=3,textvariable=qnt)
qnt.set("0")

quan.grid(row=2,column=0,padx=5,pady=5)
e2.grid(row=2,column=1,padx=5,pady=5)
e2.focus_set()
e2.icursor(1)

#______________________________________________________________________________
""" Right Frame = TopFrame + MiddleFrame + BottomFrame """

rightframe=Frame(root)
rightframe.pack(pady=30)


"""Right Frame Starts From Here"""
#______________________________________________________________________________
""" Top Frame (in Right Frame) """


topframe = Frame(rightframe)
topframe.pack()


#______________________________________________________________________________
""" Middle Frame (in Right Frame) """

middleframe = Frame(rightframe)
middleframe.pack(pady=30,padx=30)

#______________________________________________________________________________
""" Visible text above the list """

lengthlabel = ttk.Label(middleframe, text = 'Bill' , relief=GROOVE, anchor=E, font = 'Times 25 italic')
lengthlabel.pack(pady=5)


#______________________________________________________________________________
""" List  (in Right Frame) """



playlist = []
playlistbox = Listbox(rightframe)
playlistbox.pack(padx=10,pady=10,fill=tkinter.BOTH,expand=True)


#______________________________________________________________________________
# pre-requisites of space_of_text

listFont = tkFont.Font(font=playlistbox.cget("font"))
# Define spacing between left and right strings in terms of single "space" length
# find longest string in the left strings




longestLength = 172

# Defining a function to calculate space required between two texts so that alignment is correct
def space_of_text(name_item):

    text_space = listFont.measure(name_item)

    return text_space


#______________________________________________________________________________
# Beautifying listbox and adding required things before the items and their prices

text="MAGGI HOUSE".center(75," ") 

playlistbox.insert(0,text)
playlist.insert(0,0)
playlistbox.itemconfig(0, {'fg':'blue'})



text_bill = "Bill No."+ str(100+No_of_bills_in_a_day) + 55*" " + date
playlistbox.insert(1,text_bill)
playlist.insert(1,0)


text2="__ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __"
playlistbox.insert(2,text2)
playlist.insert(2,0)


text3="Item"
text3_space = space_of_text(text3)
playlistbox.insert(3,text3 +  (75-text3_space) * " " + "Qty" + (18) * " "+ "Price")
playlist.insert(3,0)



text4 = 71 *" "
playlistbox.insert(4,text4)
playlist.insert(4,0)


item_list = []
quantity_list = []

#______________________________________________________________________________
# Defining the function to add items to list

def add_to_playlist(product,price,quantity):
    
    e2.focus_set()
    e2.icursor(1)
    
    if printed == 0:
        index = 5 # Starts from 4 because we have used upto 3 in beautifying list
    
        product_space= space_of_text(product)
        playlistbox.insert(index, product + (int(180-product_space)//3) * " " + str(quantity) + (66//3) * " " +str(price*quantity)+" Rs")
        playlist.insert(index,price*quantity)
    
        item_list.append(product)
        quantity_list.append(quantity)

        amount=sum(playlist)
        lengthlabel['text'] = "Amount to be paid = Rs "+ str(amount) 
        index += 1
        
    else:
        tkinter.messagebox.showinfo('Bill is Printed','Now you cannot change the bill.')
        
    

    
#______________________________________________________________________________
""" Bottom Frame """

bottomframe = Frame(rightframe)
bottomframe.pack(pady=30,padx=30)

#______________________________________________________________________________
# Total amount text at bottomframe
lengthlabel = ttk.Label(bottomframe, text = 'Amount to be paid = Rs 00')
lengthlabel.grid(row=0,column=0,pady=5)    

#______________________________________________________________________________
""" Print and Delete Buttons"""


def add_to_csv(item_list,quantity_list):
    
    global date
    for i in range(len(item_list)):
            
        df.loc[date,item_list[i]]= df.loc[date,item_list[i]] + quantity_list[i]
        
def add_total_to_csv(date,total_sum):
    
    df.loc[date,"Total"] = df.loc[date,"Total"] + total_sum


printed = FALSE
# Defining Print Function


def print_total():
    
    
    e2.focus_set()
    e2.icursor(1)  
    

    global date
    global No_of_bills_in_a_day
    global printed
    
    if printed == 0:
        
        MsgBox = tkinter.messagebox.askquestion ('Print the Bill','Are you sure you want to print the bill... You will not be able to edit the bill again',icon = 'warning')
        if MsgBox == 'yes':
        
            ind = len(playlist)
            amount = sum(playlist)
            product = "Total"
    
            total_space = space_of_text(product)
    
            playlistbox.insert(ind,text2)  # Inserting dotted line before total
            playlist.insert(ind,0)
    
            playlistbox.insert(ind+1, product + ((180 - total_space)//3) * " " + str(sum(quantity_list)) + (66//3) * " " + str(amount)+ " Rs")
            playlist.insert(ind+1,0)   # Inserting the Total statement
            lengthlabel['text'] = "Amount to be paid = Rs "+ str(amount)
         
            No_of_bills_in_a_day = No_of_bills_in_a_day + 1
            updated_bill_no = "Bill No."+ str(100+No_of_bills_in_a_day) +  55*" " + date
            playlistbox.delete(1)
            playlistbox.insert(1,updated_bill_no)
         

            printed = TRUE
            

            add_total_to_csv(date,amount)
            add_to_csv(item_list,quantity_list)        
            df.to_csv("Sales_Data.csv",date_format="%Y-%m-%d")  

         
         
        else:
            
            printed = FALSE
            pass
             #tkinter.messagebox.showinfo('Return','You will now return to the application screen')
        
    else:
        
        tkinter.messagebox.showinfo('OOPS','The bill is already printed')
        pass
        

    
printBtn = ttk.Button(bottomframe, text = "Print", command=print_total)
printBtn.grid(row=1,column=0,pady=5)



# Defining Delete Function
def del_item():
    
    e2.focus_set()
    e2.icursor(1)  

    global printed
    if printed==0 :
        try:
            selected_item = playlistbox.curselection()
            selected_item = int(selected_item[0])
            playlistbox.delete(selected_item)
            playlist.pop(selected_item)
            
            item_list.reverse()
            item_list.pop(selected_item-5)
            item_list.reverse()
            
            
            quantity_list.reverse()
            quantity_list.pop(selected_item-5)
            quantity_list.reverse()

            amount=sum(playlist)
            lengthlabel['text'] = "Amount to be paid = Rs "+ str(amount)
            
            
            
            e2.focus_set()
            e2.icursor(1)
        
        except:
            tkinter.messagebox.showerror('Item not Selected','Please select an item to Delete.')
    else:
        
        tkinter.messagebox.showinfo('Bill is Printed','Now you cannot change the bill.')
        
        
    

    
delBtn = ttk.Button(bottomframe,text = "Delete",command=del_item)
delBtn.grid(row=1,column=1,padx=10)



# Defining New Bill Function

def new_bill():
    
    e2.focus_set()
    e2.icursor(1)   
    
    
    global printed    
    printed = FALSE
    
    qnt.set("0")
    
    lengthlabel['text'] = "Amount to be paid = Rs 00"
    
    quantity_list.clear()    
    item_list.clear()     
    
    i=5
    
    while len(playlist)!=5:

        playlistbox.delete(i)
        playlist.pop(i)
        

        

newBtn = ttk.Button(bottomframe,text = "New Bill",command=new_bill)
newBtn.grid(row=2,column=1,padx=10)

    

#______________________________________________________________________________
""" Closing The Window-Root """

def on_closing():
    

    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_closing) # Over riding red cross
root.mainloop() 

""" Summary """
# 1- First of all Menu bar and Status bar are made
# 2- Then whole window is divided in two parts - Left and Right 
# 3- Then Right side is defined which is further divided into Top, Middle and Bottom Frames
# 4- Then Top frame containing (Length and Current) Time of Song is defined
# 5- Then Middle frame containing (Play , Pause and Stop) options is defined
# 6- Then Bottom frame containing (Rewind , Mute and Volume Scale) options is defined  
# 7- Then the window is closed    
    
# Styles that can be used - normal,bold,roman,italic,underline,overstrike
# Fonts that can be used - Arial, ComicSans, Fixedsys, MS Sans Serif, MS Serif, Courier New (Courier)
# Times New Roman(Times), Verdana  
    