import serial
import SCRIPT
import Tkinter as tk
import ttk

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

class SeatrecControlHub(tk.Tk):

    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        try:
            tk.Tk.iconbitmap(self, default="seatrec_LQ1_icon.ico")
        except:
            # tk.Tk.iconbitmap(self, default="seatrec (1).png")
            pass

        tk.Tk.wm_title(self, "Seatrec Control Hub")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, Seatrec_Control_Hub):

            frame = F(container,self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def connect():
    print "hey"
    

class StartPage(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text = "Seatrec Status Checker : Connection to serial port recquired.", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

    


        connectbutton = ttk.Button(self, text="Connect", command=connect)
        connectbutton.pack()

        contbutton = ttk.Button(self, text="Continue",
                            command=lambda: controller.show_frame(Seatrec_Control_Hub))
        contbutton.pack()

        

class Seatrec_Control_Hub(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = "Seatrec Control Hub", font = LARGE_FONT)
        label.pack(pady=10,padx=10)



        reconnectbutton = ttk.Button(self, text="Reconnect", command=lambda: controller.show_frame(StartPage))
        reconnectbutton.pack()

 

app = SeatrecControlHub()
app.geometry("1280x720")
app.mainloop()



# class Dialog(Frame):


#     def __init__(self, master):
#         Frame.__init__(self, master)
#         self.list = Listbox(self, selectmode=EXTENDED)
#         self.list.pack(fill=BOTH, expand=1)
#         self.current = None
#         self.poll() # start polling the list

#     def poll(self):
#         now = self.list.curselection()
#         if now != self.current:
#             self.list_has_changed(now)
#             self.current = now
#         self.after(250, self.poll)

#     def list_has_changed(self, selection):
#         print "selection is", selection

# def Test_Connection():
#     print "Testing Connection..."
#     port = "/dev/tty.usbserial"
#     baud = 9600
#     my_SL1_connection = SCRIPT.Connection(port,baud)
#     my_SL1_connection.connect(port,baud)
#     print my_SL1_connection.ser.is_open()
#     if my_SL1_connection.ser.is_open() == True:
#         print "Pass"
#     else :
#         print "Fail"

# Test_Connection()

