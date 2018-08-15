import serial
import io
import Tkinter
from Tkinter import*
import ttk
import threading
import time

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


class SeatrecControlHub(Tk):

    def __init__(self,*args,**kwargs):
        
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, "Seatrec Control Hub")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        menubar = Menu(container)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, Seatrec_Control_Hub):

            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(StartPage)

        try:
            Tk.iconbitmap(self, default="seatrec_LQ1_icon.ico")
        except:
            # tk.Tk.iconbitmap(self, default="seatrec (1).png")
            pass

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


    
class StartPage(Frame):

    def __init__(self,parent, controller):
        Frame.__init__(self, parent)
        label = Label(self,text = "Seatrec Status Checker : Connection to serial port required.", font = LARGE_FONT)
        label.pack(side = "top", fill = "x", pady=10)

        baud_label = Label(self,text = "Baud")
        baud_label.place(x = 500, y = 340)
        port_label = Label(self,text = "Port (without tty)")
        port_label.place(x = 600, y = 340)

        self.baud_entry = Entry(self,width = 7)
        self.baud_entry.place(x = 500, y = 365)

        self.port_entry = Entry(self,width = 7)
        self.port_entry.place(x = 600, y = 365)

        self.button_var = IntVar()

        self.radio_1 = Radiobutton(text = "Windows", variable = self.button_var, value = 1).place(x = 500, y = 315)
        self.radio_2 = Radiobutton(text = "Linux", variable = self.button_var, value = 2).place(x = 600, y = 315)
        self.radio_3 = Radiobutton(text = "Mac", variable = self.button_var, value = 3).place(x = 700, y = 315)
        

        self.version_ = self.button_var.get()

        connectbutton = Button(self,text = "Connect", command = self.connect)
        connectbutton.place(x = 600, y = 375)
       
    def connect(self, parent,controller): 
        Frame.__init__(self, parent)


        
        print self.version_
        self.port = self.port_entry.get()
        self.baud = self.baud_entry.get() 

        try:
            if self.version_ == 2:
                try:
                    ser = serial.Serial('/dev/tty' + str(self.port), self.baud)
                    if ser.is_open:
                        lambda: controller.show_frame(Seatrec_Control_Hub)
                
                except:
                    lambda: popupmsg("Unable to Connect")

            elif self.version_ == 1:
                try:
                    ser = serial.Serial('COM' + str(self.port), self.baud)
                    if ser.is_open:
                        lambda: controller.show_frame(Seatrec_Control_Hub)

                except:
                    lambda: popupmsg("Unable to Connect")

            elif self.version_ == 3:
                try:
                    ser = serial.Serial('/dev/tty.' + str(self.port), self.baud)
                    if ser.is_open:
                        lambda: controller.show_frame(Seatrec_Control_Hub)

                except:
                    lambda: popupmsg("Unable to Connect")

        except ValueError:
            lambda: popupmsg("Please Re-enter Port and Baud")
            return
        
class Seatrec_Control_Hub(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self,text = "Seatrec Control Hub", font = LARGE_FONT)
        label.pack(pady=10,padx=10)


        reconnectbutton = ttk.Button(self, text="Reconnect", command=lambda: controller.show_frame(StartPage))
        reconnectbutton.pack()

 

app = SeatrecControlHub()
app.geometry("1280x720")
app.mainloop()