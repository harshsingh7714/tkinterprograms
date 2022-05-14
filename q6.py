from tkinter import*
from turtle import width
root=Tk()
v=IntVar()

root.title('Customer Loan Details')
Label(root,text='Annual Rate: ').grid(row=0,column=0)
Entry(root,width=35).grid(row=0,column=1)
Label(root,text='Number of Payments: ').grid(row=2,column=0)
Entry(root,width=35).grid(row=2,column=1)
Label(root,text='Loan Principle: ').grid(row=4,column=0)
Entry(root,width=35).grid(row=4,column=1)
Label(root,text='Monthly payment: ').grid(row=6,column=0)
Entry(root,width=35).grid(row=6,column=1)
Label(root,text='Remaining Loan: ').grid(row=8,column=0)
Entry(root,width=35).grid(row=8,column=1)

Button(root,text='Final Balance').grid(row=10,column=0)
Button(root,text='Monthly Payment').grid(row=10,column=1)
Button(root,text='Quit',command=root.destroy).grid(row=10,column=2)
root.mainloop()