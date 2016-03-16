import Tkinter as tk
import tkMessageBox, tkFileDialog, win32con, tkColorChooser, ctypes

class Window(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)   
		self.color = ((255, 250, 255), "#aaabab")
		self.configure(background = self.color[1]) ###ababab               
		self.master = master
		self.init_window()
		
	def init_window(self):
		self.pack(fill = tk.BOTH, expand = 1)

		# create a menu instance
		menu = tk.Menu(self.master)
		self.master.config(menu = menu)

		# create the file object
		file = tk.Menu(menu, tearoff = False)
		# command of the file menu
		file.add_command(label = "New", command = self.New)
		file.add_command(label = "Open", command = self.Open)
		file.add_command(label = "Save", command = self.Save)
		file.add_command(label = "Save as...", command = self.Save_as)
		file.add_separator()
		file.add_command(label = "Exit", command = client_exit)
		#added "file" to menu
		menu.add_cascade(label = "File", menu = file)

		# create the edit object
		edit = tk.Menu(menu, tearoff = False)
		# command of the edit menu
		edit.add_command(label = "Change Background", 
								command = self.change_bgn)
		#added "edit" to our menu
		menu.add_cascade(label = "Edit", menu = edit)
		
		# create the options object
		options = tk.Menu(menu, tearoff = False)
		# command of the options menu
		options.add_command(label = "New", command = self.New)
		options.add_command(label = "Open", command = self.Open)
		options.add_command(label = "Save", command = self.Save)
		options.add_command(label = "Save as...", command = self.Save_as)
		options.add_separator()
		options.add_command(label = "Exit", command = self.New)
		#added "Options" to menu
		menu.add_cascade(label = "Options", menu = options)
		
		# create the help object
		help = tk.Menu(menu, tearoff = False)
		# command of the help menu
		help.add_command(label = "New", command = self.New)
		help.add_command(label = "Open", command = self.Open)
		help.add_command(label = "Save", command = self.Save)
		help.add_separator()
		help.add_command(label = "About OpenPlot", 
									command = self.New)
		#added "help" to menu
		menu.add_cascade(label = "Help", menu = help)
		
	def New(self):
		global Top
		self.__NewWindow('Main', 250, 300)
		

	def Open(self):
		tkFileDialog.askopenfilename()

	def Save(self):
		pass

	def Save_as(self):
		pass

	def change_bgn(self):
		self.color = tkColorChooser.askcolor(initialcolor = self.color[1])
		self.configure(background = self.color[1]) ###ababab

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
				icon = 'warning', default = "yes"):
			root.destroy() #exit() root.quit()

class FLASHWINFO(ctypes.Structure): 
    _fields_ = [('cbSize', ctypes.c_uint), 
                ('hwnd', ctypes.c_uint), 
                ('dwFlags', ctypes.c_uint), 
                ('uCount', ctypes.c_uint), 
                ('dwTimeout', ctypes.c_uint)]
		
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
    root.iconbitmap(default = 'C:\Users\dartz\Desktop\iconlog.ico')
    #root.resizable(width='FALSE', height='FALSE')
    app = Window(root)
    # app.pack(side="top", fill="both", expand=True)
    root.protocol("WM_DELETE_WINDOW", client_exit)
    root.mainloop()
