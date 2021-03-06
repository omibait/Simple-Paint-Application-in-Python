from tkinter import *
import tkinter.messagebox

b1 = "up"
xold, yold = None, None

class Paint(object):

	def __init__(self):
		self.root = Tk()
		self.x = self.y = 0
		
		self.paint = Label(self.root,text="Paint",font="Elephent 25",bg="Sky blue",bd=3,relief="solid",width=50,height=2)
		self.paint.grid(row=0,column=0,columnspan=7)

		self.selectTool_label = Label(self.root,text="Select your Tool",font="Times 20",fg="dark blue",bd=1,relief="solid",width=50,height=1)
		self.selectTool_label.grid(row=1,column=0,columnspan=7)
		
		self.pen_btn = Button(self.root, text='Pen',width=10,bg="light green",font="Times 13 bold", command=self.pen)
		self.pen_btn.grid(row=4, column=0)
		
		self.line_btn = Button(self.root, text='Line',width=10,bg="light green",font="Times 13 bold", command=self.draw_line)
		self.line_btn.grid(row=4, column=1)

		self.rectangle_btn = Button(self.root, text='Rectangle',width=10,bg="light green",font="Times 13 bold", command=self.draw_rectangle)
		self.rectangle_btn.grid(row=4, column=2)
		
		self.circle_btn = Button(self.root,text="Circle",width=10,bg="light green",font="Times 13 bold", command=self.draw_circle)
		self.circle_btn.grid(row=4,column=3)
		
		self.eraser_btn = Button(self.root, text='Eraser',width=10,bg="light green",font="Times 13 bold", command=self.eraser)
		self.eraser_btn.grid(row=4, column=4)
		
		self.clearScreen_btn = Button(self.root, text='Clear Screen',width=10,bg="light green",font="Times 13 bold", command=self.clearScreen)
		self.clearScreen_btn.grid(row=6, column=1)
		
		self.quit_btn = Button(self.root, text='Quit',width=10,bg="light green",font="Times 13 bold", command=self.quit)
		self.quit_btn.grid(row=6, column=3)
		
		self.canvas = Canvas(self.root, bg='white', width=1000, height=500,cursor="cross")
		self.canvas.grid(row=5, columnspan=5)
		
		self.old_x = None
		self.old_y = None
	
		self.root.mainloop()
		
	def pen(self):
		self.canvas.bind('<B1-Motion>', self.motionPen)
		self.canvas.bind('<ButtonPress-1>',self.on_button_pressPen)
		self.canvas.bind('<ButtonRelease-1>',self.on_button_releasePen)
		
		
	def draw_line(self):
		self.canvas.bind("<ButtonPress-1>", self.on_button_pressLine)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_releaseLine)
		
		
	def draw_rectangle(self):
		self.canvas.bind("<ButtonPress-1>", self.on_button_pressRectangle)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_releaseRectangle)
		
		
	def draw_circle(self):
		self.canvas.bind("<ButtonPress-1>", self.on_button_pressCircle)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_releaseCircle)
		
		
	def eraser(self):
		self.canvas.bind('<B1-Motion>', self.motionEraser)
		self.canvas.bind('<ButtonPress-1>',self.on_button_pressEraser)
		self.canvas.bind('<ButtonRelease-1>',self.on_button_releaseEraser)
		
		
	def clearScreen(self):
		answer=tkinter.messagebox.askquestion("Reset","You want to Clear your Progress")	
		if answer=="yes":
			self.canvas.delete("all")
			
		if answer=="no":
			pass
		
	def quit(self):
		answer=tkinter.messagebox.askquestion("Quit","Want to Quit")
		if answer=="yes":
			self.root.destroy()
		if answer=="no":
			pass
	

	def on_button_pressLine(self, event):
		self.x = event.x
		self.y = event.y


	def on_button_releaseLine(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.canvas.create_line(x0,y0,x1,y1)
		

	def on_button_pressRectangle(self, event):
		self.x = event.x
		self.y = event.y

	def on_button_releaseRectangle(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.canvas.create_rectangle(x0,y0,x1,y1)
		
				
	def on_button_pressCircle(self, event):
		self.x = event.x
		self.y = event.y


	def on_button_releaseCircle(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.canvas.create_oval(x0,y0,x1,y1)
		
		
	def on_button_pressPen(self,event):
		global b1
		b1 = "down"          


	def on_button_releasePen(self,event):
		global b1, xold, yold
		b1 = "up"
		xold = None         
		yold = None


	def motionPen(self,event):
		if b1 == "down":
			global xold, yold
			if xold is not None and yold is not None:
				event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)                      
			xold = event.x
			yold = event.y
			
	
	def on_button_pressEraser(self,event):
		global b1
		b1 = "down"          


	def on_button_releaseEraser(self,event):
		global b1, xold, yold
		b1 = "up"
		xold = None         
		yold = None


	def motionEraser(self,event):
		if b1 == "down":
			global xold, yold
			if xold is not None and yold is not None:
				event.widget.create_line(xold,yold,event.x,event.y,fill="white",width=10,smooth=TRUE)
			xold = event.x
			yold = event.y

if __name__ == '__main__':
	Paint()
