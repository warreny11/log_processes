import serial
import Tkinter as tk
import ttk
import threading
import time
import io
import platform

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
            pass
            
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

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text = "Start Page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        baud_label = tk.Label(self,text = "Baud")
        baud_label.place(x = 500, y = 340)
        port_label = tk.Label(self,text = "Port")
        port_label.place(x = 600, y = 340)

        baud_entry = tk.Entry(self,width = 7)
        baud_entry.place(x = 500, y = 365)

        port_entry = tk.Entry(self,width = 7)
        port_entry.place(x = 600, y = 365)

        self.port = port_entry.get()
        self.baud = baud_entry.get()

        connectbutton = tk.Button(self,text = "Connect", command = self.connect) 
        connectbutton.place(x = 600, y = 400)

        nextbutton = tk.Button(self, text = "Next", command = lambda : controller.show_frame(Seatrec_Control_Hub))
        nextbutton.place(x = 600, y = 500)
            
        
    def connect(self): 

        system = platform.system()

        poss_systems =[
                ("Windows", "1"),
                ("Linux", "2"),
                ("Darwin", "3"),
            ]

        for text,modes in poss_systems:
            if system == text:
                # print system
                self.version_ = int(modes)
                # print self.version_

        port = self.port
        baud = self.baud

        sys_list = [("Windows","1","COM"),
                    ("Linux", "2","/dev/tty"),
                    ("Mac", "3","/dev/tty.")]

        for types, nums, ports in sys_list:
            if self.version_ == int(nums):
                try:
                    ser = serial.Serial(ports + str(port), baud)
                    if ser.is_open :
                        popupmsg("Running " + types + ": Connected... Please click Next")
                        print "Connected..."
                        return 0
                    else :
                        print "Unable to connect..."
                        popupmsg("Unable to connect...")
                        return -1 
                except:
                    popupmsg("Running " + types + ": Cant Open Specified Port, Try Again")
                    print "Running " + types + ": Cant Open Specified Port"
      

class Seatrec_Control_Hub(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = "Seatrec Control Hub", font = LARGE_FONT)
        label.pack(pady=10,padx=10)



        reconnectbutton = ttk.Button(self, text="Reconnect", command=lambda: controller.show_frame(StartPage))
        reconnectbutton.place(x = 900, y = 600)

app = SeatrecControlHub()
app.geometry("1280x720")
app.mainloop()