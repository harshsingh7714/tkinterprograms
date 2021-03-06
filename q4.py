from tkinter import*
from turtle import width
root=Tk()
v=IntVar()

root.title('Flyer Details')
Label(root,text='BookingId: ').grid(row=0,column=0)
Entry(root,width=35).grid(row=0,column=1)
Label(root,text='Passenger Name: ').grid(row=1,column=0)
Entry(root,width=35).grid(row=1,column=1)
Label(root,text='Contact No: ').grid(row=2,column=0)
Entry(root,width=35).grid(row=2,column=1)
Label(root,text='Flight: ').grid(row=3,column=0)
Entry(root,width=35).grid(row=3,column=1)
Label(root,text='Source: ').grid(row=4,column=0)

Radiobutton(root,text='Delhi',variable=v,value=1).grid(row=4,column=1)
Radiobutton(root,text='Mumbai',variable=v,value=2).grid(row=4,column=2)
Label(root,text='Destination: ').grid(row=5,column=0)

Radiobutton(root,text='Chennai',variable=v,value=1).grid(row=5,column=1)
Radiobutton(root,text='Kolkata',variable=v,value=2).grid(row=5,column=2)
Label(root,text='Duration: ').grid(row=6,column=0)
Spinbox(root,from_= 0,to= 10).grid(row=6,column=1)
Button(root,text='Insert').grid(row=7,column=0)
Button(root,text='Update').grid(row=7,column=1)
Button(root,text='Delete').grid(row=8,column=0)
Button(root,text='Select').grid(row=8,column=1)
Button(root,text='Submit',command=root.destroy).grid(row=8,column=2)
root.mainloop()