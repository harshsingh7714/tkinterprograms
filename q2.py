from tkinter import*
from turtle import width
root=Tk()
v=IntVar()

root.title('Banking Form')
Label(root,text='CustomerId: ').grid(row=0,column=0)
Entry(root,width=35).grid(row=0,column=1)
Label(root,text='Customer Name: ').grid(row=1,column=0)
Entry(root,width=35).grid(row=1,column=1)
Label(root,text='Branch: ').grid(row=2,column=0)
Entry(root,width=35).grid(row=2,column=1)
Label(root,text='City: ').grid(row=3,column=0)
Entry(root,width=35).grid(row=3,column=1)
Label(root,text='Gender: ').grid(row=4,column=0)

Radiobutton(root,text='Male',variable=v,value=1).grid(row=4,column=1)
Radiobutton(root,text='Female',variable=v,value=2).grid(row=4,column=2)
Label(root,text='Age: ').grid(row=5,column=0)
Scale(root,from_= 19,to= 100,orient=HORIZONTAL).grid(row=5,column=1)
Button(root,text='Insert').grid(row=6,column=0)
Button(root,text='Update').grid(row=6,column=1)
Button(root,text='Delete').grid(row=7,column=0)
Button(root,text='Select').grid(row=7,column=1)
Button(root,text='Submit').grid(row=7,column=2)
root.mainloop()