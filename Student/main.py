from tkinter import*
from tkinter import ttk
import sqlite3

'''c=sqlite3.connect("Student.db")
cursor=c.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Student( ID INTEGER, NAME VARCHAR(20),AGE INTEGER, DOB VARCHAR(20),GENDER VARCHAR(20),CITY VARCHAR(20))")
c.commit()
c.close()
print("created")'''


class Student:
    def __init__(self,main):
        self.main=main
        self.T_Frame= Frame(self.main,height=100 , width=1000,background="gray",bd=2 ,relief=GROOVE)
        self.T_Frame.pack()
        self.Title= Label(self.T_Frame,text="Student management Sysytem",font="TimesNewRoman 20 bold",width=1000, bg="gray")
        self.Title.pack()

        self.T_Frame_1 = Frame(self.main, height=600, width=500,bg="gray",bd=2,relief=GROOVE)
        self.T_Frame_1.pack(side=LEFT)

        Label(self.T_Frame_1,text="Student Details",bg="gray",font="arial 14 bold",relief=GROOVE).place(x=20,y=20)

        self.id= Label(self.T_Frame_1,text="id",bg="gray",font="arial 14 bold",relief=GROOVE)
        self.id.place(x=40,y=70)
        self.id_Entry =Entry(self.T_Frame_1,width=40)
        self.id_Entry.place(x=150, y=70)

        self.Name = Label(self.T_Frame_1, text="Name", bg="gray", font="arial 14 bold", relief=GROOVE)
        self.Name.place(x=40, y=110)
        self.Name_Entry = Entry(self.T_Frame_1, width=40)
        self.Name_Entry.place(x=150, y=110)

        self.Age = Label(self.T_Frame_1, text="Age", bg="gray", font="arial 14 bold", relief=GROOVE)
        self.Age.place(x=40, y=150)
        self.Age_Entry = Entry(self.T_Frame_1, width=40)
        self.Age_Entry.place(x=150, y=150)

        self.DOB = Label(self.T_Frame_1, text="DOB", bg="gray", font="arial 14 bold", relief=GROOVE)
        self.DOB.place(x=40, y=190)
        self.DOB_Entry = Entry(self.T_Frame_1, width=40)
        self.DOB_Entry.place(x=150, y=190)

        self.Gender = Label(self.T_Frame_1, text="Gender", bg="gray", font="arial 14 bold", relief=GROOVE)
        self.Gender.place(x=40, y=230)
        self.Gender_Entry = Entry(self.T_Frame_1, width=40)
        self.Gender_Entry.place(x=150, y=230)

        self.City = Label(self.T_Frame_1, text="City", bg="gray", font="arial 14 bold", relief=GROOVE)
        self.City.place(x=40, y=270)
        self.City_Entry = Entry(self.T_Frame_1, width=40)
        self.City_Entry.place(x=150, y=270)


        self.Button_Frame=Frame(self.T_Frame_1,height=250,width=250,bd=2,bg="gray",relief=GROOVE)
        self.Button_Frame.place(x=100,y=300)

        self.Add= Button(self.Button_Frame,text="ADD",width=25,font="arial 12 bold",command=self.Add)
        self.Add.pack()
        self.Delete = Button(self.Button_Frame, text="DELETE", width=25, font="arial 12 bold",command=self.Delete)
        self.Delete.pack()
        self.Update = Button(self.Button_Frame, text="UPDATE", width=25, font="arial 12 bold",command=self.Update)
        self.Update.pack()
        self.Clear = Button(self.Button_Frame, text="CLEAR", width=25, font="arial 12 bold",command=self.Clear)
        self.Clear.pack()


        self.T_Frame_2 =  Frame(self.main, height=600, width=600,bg="gray",bd=2,relief=GROOVE)
        self.T_Frame_2.pack(side=RIGHT)

        self.tree=ttk.Treeview(self.T_Frame_2,columns=("c1","c2","c3","c4","c5","c6"),show="headings",height=30)

        self.tree.column("#1",anchor=CENTER,width=60)
        self.tree.heading("#1",text="ID")

        self.tree.column("#2", anchor=CENTER,width=100)
        self.tree.heading("#2", text="NAME")

        self.tree.column("#3", anchor=CENTER, width=100)
        self.tree.heading("#3", text="AGE")

        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="DOB")

        self.tree.column("#5", anchor=CENTER, width=115)
        self.tree.heading("#5", text="GENDER")

        self.tree.column("#6", anchor=CENTER, width=120)
        self.tree.heading("#6", text="CITY")
        
        self.tree.pack()
        
    def Add(self):
         id= self.id_Entry.get()
         Name= self.Name_Entry.get()
         Age= self.Age_Entry.get()
         DOB= self.DOB_Entry.get()
         Gender= self.Gender_Entry.get()
         City= self.City_Entry.get()
         c = sqlite3.connect("Student.db")
         cursor=c.cursor()
         cursor.execute("INSERT INTO Student(ID,NAME,AGE,DOB,GENDER,CITY)VALUES(?,?,?,?,?,?)",(id,Name,Age,DOB,Gender,City))
         c.commit()
         c.close()
         print("inserted")
         self.tree.insert("",index=0,values=(id,Name,Age,DOB,Gender,City))

    def Delete(self):
        item=self.tree.selection()[0]
        selected_item=self.tree.item(item)['values'][0]
        print(selected_item)
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("DELETE FROM Student WHERE ID={}".format(selected_item))
        c.commit()
        c.close()
        self.tree.delete(item)

    def Update(self):
        id = self.id_Entry.get()
        Name = self.Name_Entry.get()
        Age = self.Age_Entry.get()
        DOB = self.DOB_Entry.get()
        Gender = self.Gender_Entry.get()
        City = self.City_Entry.get()
        item=self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("UPDATE Student SET ID=?,NAME=?,AGE=?,DOB=?,GENDER=?,CITY=? WHERE ID=?",(selected_item,Name,Age,DOB,Gender,City,selected_item))
        c.commit()
        c.close()
        print("Updated")
        self.tree.item(item,values=(id,Name,Age,DOB,Gender,City))

    def Clear(self):
        self.id_Entry.delete(0,END)
        self.Name_Entry.delete(0, END)
        self.Age_Entry.delete(0, END)
        self.DOB_Entry.delete(0, END)
        self.Gender_Entry.delete(0, END)
        self.City_Entry.delete(0, END)


main=Tk()
main.title("Student Management System")
main.resizable(False,False)
main.geometry("1200x600")


Student(main)
main.mainloop()

