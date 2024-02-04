

from tkinter import *
from PIL import Image, ImageTk
from threading import Thread

## Hide pygame msg
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

class Notification:
	def __init__(self):
		self.win = Tk()
		self.title = 'notification '
		self.icon_path = ''
		self.audio_path = ''
	
		self.icon = None
		self.description = 'this is notification for test :)'
		self.background = '#2c3e50'

		

		self.width = 500
		self.height = 200
		self.x = (self.win.winfo_screenwidth() - self.width) - 20
		self.y = (self.win.winfo_screenheight() - self.height) - 60

	def play_sound(self):
		def play():
			pygame.mixer.init()
			pygame.mixer.music.load(self.audio_path)
			pygame.mixer.music.play()

		Thread(target=play).start()

	def close(self):
		self.win.destroy()

	def show(self):
		
		if self.background == 'white':
			self.font_color = 'black'
		else:
			self.font_color = 'white'
		
		self.icon = ImageTk.PhotoImage(Image.open(self.icon_path).resize((30,30)))

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


