from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    publication = bookInfo5.get()
    vol = bookInfo6.get()
    pub_year = bookInfo7.get()

    
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"','"+publication+"','"+vol+"','"+pub_year+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)
    print(publication)
    print(vol)
    print(pub_year)


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,bookInfo7,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Password"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#DEB6AB")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1, relheight=0.06)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.06)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.2, relheight=0.06)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.06)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.3, relheight=0.06)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.06)
            
    # publication
    lb5 = Label(labelFrame,text="Publication : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.4, relheight=0.06)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.06)

     # volume
    lb6 = Label(labelFrame,text="Volume : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.5, relheight=0.06)
        
    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.06)

     # publication year
    lb7 = Label(labelFrame,text="Publication Year: ", bg='black', fg='white')
    lb7.place(relx=0.05,rely=0.6, relheight=0.06)
        
    bookInfo7 = Entry(labelFrame)
    bookInfo7.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.06)

    # Book Status
    lb4 = Label(labelFrame,text="Book Status", bg='black', fg='white') 
    lb4.place(relx=0.05,rely=0.7, relheight=0.06)   
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.06)
        
    #Submit Button
    SubmitBtn = Button(labelFrame,text="ADD",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(labelFrame,text="BACK",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()