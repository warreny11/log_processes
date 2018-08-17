import serial
import SCRIPT
import Tkinter as tk
import ttk
import threading
import time
import io

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

        self.baud_entry = tk.Entry(width = 7)
        self.baud_entry.place(x = 500, y = 365)

        self.port_entry = tk.Entry(width = 7)
        self.port_entry.place(x = 600, y = 365)

        self.button_var = tk.IntVar()
        radio_1 = tk.Radiobutton(text = "Windows", variable = self.button_var, value = 1).place(x = 500, y = 315)
        radio_2 = tk.Radiobutton(text = "Linux", variable = self.button_var, value = 2).place(x = 600, y = 315)
        radio_3 = tk.Radiobutton(text = "Mac", variable = self.button_var, value = 3).place(x = 700, y = 315)

        connectbutton = tk.Button(self,text = "Connect", command = self.connect())
        connectbutton.place(x = 600, y = 400)

    def connect(self): 
        
        version_ = self.button_var.get()
        print version_
        global serial_object
        port = self.port_entry.get()
        baud = self.baud_entry.get() 
        
        try:
            if version_ == 2:
                try:
                    serial_object = serial.Serial('/dev/tty' + str(port), baud)
                
                except:
                    print "Cant Open Specified Port"

            elif version_ == 1:
                serial_object = serial.Serial('COM' + str(port), baud)

            elif version_ == 3:
                serial_object = serial.Serial('/dev/tty.' + str(port), baud)

        except ValueError:
            print "Enter Baud and Port"
            return

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