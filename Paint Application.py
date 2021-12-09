from tkinter import *
import tkinter.messagebox

b1 = "up"
xold, yold = None, None

class Paint(object):

	def __init__(self):
		self.root = Tk()
		self.x = self.y = 0
		
		self.lb1=Label(self.root,text="Paint",font="Elephent 25",bg="Sky blue",bd=3,relief="solid",width=50,height=2)
		self.lb1.grid(row=0,column=0,columnspan=7)

		self.lb2=Label(self.root,text="Select your Tool",font="Times 20",fg="dark blue",bd=1,relief="solid",width=50,height=1)
		self.lb2.grid(row=1,column=0,columnspan=7)
		
		self.pen = Button(self.root, text='Pen',width=10,bg="light green",font="Times 13 bold", command=self.pen)
		self.pen.grid(row=4, column=0)
		
		self.line = Button(self.root, text='Line',width=10,bg="light green",font="Times 13 bold", command=self.line)
		self.line.grid(row=4, column=1)

		self.rect = Button(self.root, text='Rectangle',width=10,bg="light green",font="Times 13 bold", command=self.rect)
		self.rect.grid(row=4, column=2)
		
		self.circle=Button(self.root,text="Circle",width=10,bg="light green",font="Times 13 bold", command=self.circle)
		self.circle.grid(row=4,column=3)
		
		self.er = Button(self.root, text='Eraser',width=10,bg="light green",font="Times 13 bold", command=self.eraser)
		self.er.grid(row=4, column=4)
		
		self.cl = Button(self.root, text='Clear Screen',width=10,bg="light green",font="Times 13 bold", command=self.cl)
		self.cl.grid(row=6, column=1)
		
		self.qt = Button(self.root, text='Quit',width=10,bg="light green",font="Times 13 bold", command=self.qt)
		self.qt.grid(row=6, column=3)
		
		self.c = Canvas(self.root, bg='white', width=1000, height=500,cursor="cross")
		self.c.grid(row=5, columnspan=5)
		
		self.old_x = None
		self.old_y = None
	
		self.root.mainloop()
		
	def pen(self):
		self.c.bind('<B1-Motion>', self.motionP)
		self.c.bind('<ButtonPress-1>',self.b1downP)
		self.c.bind('<ButtonRelease-1>',self.b1upP)
		
		
	def line(self):
		self.c.bind("<ButtonPress-1>", self.on_button_pressL)
		self.c.bind("<ButtonRelease-1>", self.on_button_releaseL)
		
		
	def rect(self):
		self.c.bind("<ButtonPress-1>", self.on_button_pressR)
		self.c.bind("<ButtonRelease-1>", self.on_button_releaseR)
		
		
	def circle(self):
		self.c.bind("<ButtonPress-1>", self.on_button_pressC)
		self.c.bind("<ButtonRelease-1>", self.on_button_releaseC)
		
		
	def eraser(self):
		self.c.bind('<B1-Motion>', self.motionE)
		self.c.bind('<ButtonPress-1>',self.b1downE)
		self.c.bind('<ButtonRelease-1>',self.b1upE)
		
		
	def cl(self):
		answer=tkinter.messagebox.askquestion("Reset","You want to Clear your Progress")
		
		if answer=="yes":
			self.c.delete("all")
			
		if answer=="no":
			pass
		
	def qt(self):
		answer=tkinter.messagebox.askquestion("Quit","Want to Quit")
		
		
		if answer=="yes":
			self.root.destroy()
			
		if answer=="no":
			pass
	
		
	def on_button_pressL(self, event):
		self.x = event.x
		self.y = event.y

	def on_button_releaseL(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.c.create_line(x0,y0,x1,y1)
		

		
	def on_button_pressR(self, event):
		self.x = event.x
		self.y = event.y

	def on_button_releaseR(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.c.create_rectangle(x0,y0,x1,y1)
		
		
		
		
	def on_button_pressC(self, event):
		self.x = event.x
		self.y = event.y

	def on_button_releaseC(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.c.create_oval(x0,y0,x1,y1)
		
		
		

	def b1downP(self,event):
		global b1
		b1 = "down"          
                       
	def b1upP(self,event):
		global b1, xold, yold
		b1 = "up"
		xold = None         
		yold = None

	def motionP(self,event):
		if b1 == "down":
			global xold, yold
			if xold is not None and yold is not None:
				event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)
                      
			xold = event.x
			yold = event.y
			
			

	def b1downE(self,event):
		global b1
		b1 = "down"          
                       
	def b1upE(self,event):
		global b1, xold, yold
		b1 = "up"
		xold = None         
		yold = None

	def motionE(self,event):
		if b1 == "down":
			global xold, yold
			if xold is not None and yold is not None:
				event.widget.create_line(xold,yold,event.x,event.y,fill="white",width=10,smooth=TRUE)
			xold = event.x
			yold = event.y

if __name__ == '__main__':
	Paint()