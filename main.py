# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:31:37 2016

@author: dartz
"""

import Tkinter as tk
import tkMessageBox, tkFileDialog, win32con, tkColorChooser, ctypes, ttk
#import BluetoothModule as Bt

class Window(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)   
		self.color = ((200, 200, 200), "#c8c8c8") #570073
		self.config(background = self.color[1]) ###ababab      
		self.grid()         
		self.master = master
		self.init_window()
		
		'''Frame1 = tk.Frame(master, bg="red")
		Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, 
								sticky = tk.W+tk.E+tk.N+tk.S) 
		Frame2 = tk.Frame(master, bg="blue")
		Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, 
								sticky = tk.W+tk.E+tk.N+tk.S)
		Frame3 = tk.Frame(master, bg="green")
		Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, 
								sticky = tk.W+tk.E+tk.N+tk.S)
		'''
	def init_window(self):
		style = ttk.Style()
		style.configure("BW.TLabel", background = "white")
		style.map("TLabel", background = [('pressed', '!disabled', '#570073'), 
								('active', '#570073')])

		# create a menu instance
		self.menu = tk.Menu(self.master)
		self.master.config(menu = self.menu)
		
		photo = tk.PhotoImage(file = 'icons/ezgif.com-resize.gif',
						master = self.menu)
		tk.toolbar = ttk.Frame(self.master, style = "BW.TLabel")
		ttk.Separator(self.master, orient = tk.VERTICAL)
		tk.toolbar.pack(side = tk.TOP, fill = tk.X)
		exitButton = ttk.Button(tk.toolbar, image = photo, style = "TLabel")
		exitButton.image = photo # keep a reference!
		exitButton.pack(side = tk.LEFT, padx = 1, pady = 1)
		#bicepFrame = ttk.Frame(self.master, padding="4 4 8 8")
		#ttk.Label(bicepFrame, text="Capacitor Converter", anchor="center")
		self.pack(fill = tk.BOTH, expand = True)		
		
		# create the file object
		file = tk.Menu(self.menu, tearoff = False)
		# command of the file menu
		file.add_command(label = "New", accelerator='Ctrl+N', 
					command = self.New)
		file.add_command(label = "Open", accelerator='Ctrl+O',
					command = self.Open)
		file.add_command(label = "Save", accelerator='Ctrl+S',
					command = self.Save)
		file.add_command(label = "Save as ...", accelerator='Ctrl+May+S',
					command = self.Save_as)
		file.add_separator()
		file.add_command(label = "Exit", accelerator='Ctrl+Q',
					command = client_exit)
		#added "file" to menu
		self.menu.add_cascade(label = "File", menu = file)

		# create the edit object
		edit = tk.Menu(self.menu, tearoff = False)
		# command of the edit menu
		edit.add_command(label = "Change Background", 
					command = self.change_bgn)
		#added "edit" to our menu
		self.menu.add_cascade(label = "Edit", menu = edit)
		#icons = (tk.PhotoImage(file = sys.argv[1]))
		
           # create the run object
		run = tk.Menu(self.menu, tearoff = False)
		# command of the run menu
		run.add_command(label = "Run",  image = photo,
				compound = tk.LEFT, command = self.enable_menu)
		run.add_command(label = "Stop", command = self.disable_menu)
		run.add_command(label = "Save", command = self.Save)
		run.add_command(label = "Save as...", command = self.Save_as)
		run.add_separator()
		run.add_command(label = "Exit", command = self.New)
		#added "Run" to menu
		self.menu.add_cascade(label = "Run", menu = run)
  
		# create the options object
		options = tk.Menu(self.menu, tearoff = False)
		# command of the options menu
		options.add_command(label = "New", command = self.New)
		options.add_command(label = "Open", command = self.Open)
		options.add_command(label = "Save", command = self.Save)
		options.add_command(label = "Save as...", command = self.Save_as)
		options.add_separator()
		options.add_command(label = "Exit", command = self.New)
		#added "Options" to menu
		self.menu.add_cascade(label = "Options", menu = options)
		
		# create the help object
		help = tk.Menu(self.menu, tearoff = False)
		# command of the help menu
		help.add_command(label = "New", command = self.New)
		help.add_command(label = "Open", command = self.Open)
		help.add_command(label = "Save", command = self.Save)
		help.add_separator()
		help.add_command(label = "About OpenPlot", 
					command = self.New)
		#added "help" to menu
		self.menu.add_cascade(label = "Help", menu = help)
		
	def New(self):
		global Top
		self.__NewWindow('Main', 350, 500)
		self.prop = Properties(self.top)
		print(self.prop.value)

	def Open(self):
		tkFileDialog.askopenfilename()

	def Save(self):
		self.master.attributes("-fullscreen", True)

	def Save_as(self):
		self.master.attributes("-fullscreen", False)

	def change_bgn(self):
		self.color = tkColorChooser.askcolor(initialcolor = self.color[1])
		self.configure(background = self.color[1]) ###ababab
		print(self.color[1])
  
	def enable_menu(self):
           self.menu.entryconfig("File", state="normal")

	def disable_menu(self):
           self.menu.entryconfig("File", state="disabled")

	def __NewWindow(self,name,w,h):
		global ws, hs
		self.top = tk.Toplevel(self.master)
		self.top.focus_set()
		self.top.transient(self)
		self.top.grab_set()
		x, y = (ws/2) - (w/2), (hs/2) - (h/2)
		self.top.geometry("%dx%d+%d+%d" % (w, h, x, y))
		self.top.resizable(width='FALSE', height='FALSE')
		self.top.bind("<ButtonPress>", self.flash)
		#Bt.FindDevice()

	def flash(self, event):
		if self.top.winfo_containing(event.x_root, event.y_root) != self.top:
			self.top.bell()
			number_of_flashes = 3
			flash_time = 80
			info = FLASHWINFO(0,
							  ctypes.windll.user32.GetForegroundWindow(),
							  win32con.FLASHW_ALL,
							  number_of_flashes,
							  flash_time)
			info.cbSize = ctypes.sizeof(info) 
			ctypes.windll.user32.FlashWindowEx(ctypes.byref(info))

def client_exit(*self):
		if tkMessageBox.askyesno("OpenPlot", 
				"Are you sure you want to exit?", 
				icon = 'warning', default = "no"):
			root.destroy() #exit() root.quit()

class FLASHWINFO(ctypes.Structure): 
    _fields_ = [('cbSize', ctypes.c_uint), 
                ('hwnd', ctypes.c_uint), 
                ('dwFlags', ctypes.c_uint), 
                ('uCount', ctypes.c_uint), 
                ('dwTimeout', ctypes.c_uint)]

class Properties(tk.Toplevel):
	def __init__(self, mFrame):
		self.parent = mFrame
		self.value = "name"
		
if __name__ == "__main__":
    root = tk.Tk()
    w, h = 800, 600
    ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    #root.wm_state('zoomed')
    root.minsize(str(w),str(h))
    root.title('')
    #root.overrideredirect(True)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.iconbitmap(default = 'icons/HealthPatient.ico')
    #root.resizable(width='FALSE', height='FALSE')
    app = Window(root)
    # app.pack(side="top", fill="both", expand=True)
    root.protocol("WM_DELETE_WINDOW", client_exit)
    root.bind('<Control-q>', client_exit)
    root.mainloop()
