import serial
import SCRIPT
import tkinter as tk
import ttk

LARGE_FONT = ("Verdana", 12)

class SeatrecControlHub(tk.Tk):

    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="seatrec_LQ1_icon.ico")
        tk.Tk.wm_title(self, "Seatrec Control Hub")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage, Seatrec_Control_Hub):

            frame = F(container,self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(F)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def connect():
    print "hey"
    

class StartPage(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text = "Start Page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        
        # radio_1 = ttk.Radiobutton(text = "Windows", variable = button_var, value = 1).place(x = 10, y = 315)
        # radio_2 = ttk.Radiobutton(text = "Linux", variable = button_var, value = 2).place(x = 110, y = 315)
        # radio_3 = ttk.Radiobutton(text = "Mac", variable = button_var, value = 3).place(x = 210, y = 315)


        connectbutton = ttk.Button(self, text="Connect", command=connect)
        connectbutton.pack()

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

