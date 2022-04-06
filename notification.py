

from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
from threading import Thread

class Notification:
	def __init__(self):
		self.win = Tk()
		self.title = 'notification '
		self.icon = ImageTk.PhotoImage(Image.open('icons/notification.png').resize((30,30)))
		self.description = 'this is notification for test :)'
		self.background = '#2c3e50'

		if self.background != 'white':
			self.font_color = 'black'
		else:
			self.font_color = 'white'

		self.width = 500
		self.height = 200
		self.x = (self.win.winfo_screenwidth() - self.width) - 20
		self.y = (self.win.winfo_screenheight() - self.height) - 60

	def play_sound(self):
		def play():
			playsound('audio/1.mp3')

		Thread(target=play).start()

	def close(self):
		self.win.destroy()

	def show(self):

		self.win.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
		self.win.overrideredirect(True)
		self.win.config(bg = self.background)

		self.play_sound()

		# create icon
		n_icon = Label(self.win, image = self.icon, bg = self.background)
		n_icon.image = self.icon
		n_icon.place(x = 10, y = 10)

		# create titel
		titel = Label(self.win, text = self.title, bg = self.background, fg=self.font_color, font = ('san-serf', 15))
		titel.place(x = 60, y = 10)

		# create close bt
		close_image = ImageTk.PhotoImage(Image.open('icons/close.png').resize((20,20)))
		close_bt = Button(self.win, image = close_image, bd = 0, bg = self.background, command = self.close)
		close_bt.place(x = self.width - 40, y = 10)

		# create description
		description = Label(self.win, text = self.description, bg = self.background, fg=self.font_color, font = ('san-serf', 13))
		description.place(x = 10, y = 70)

		self.win.after(50000, self.close)

		self.win.mainloop()




notify = Notification()
notify.background = 'white'
notify.description = 'hi this is tkinter notification test \nhi this is tkinter notification test'
notify.show()