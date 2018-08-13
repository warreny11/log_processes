import serial
import SCRIPT
import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class SeatrecControlHub(tk.Tk):

    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        frame = StartPage(container,self)
        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text = "Start Page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

app = SeatrecControlHub()
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

