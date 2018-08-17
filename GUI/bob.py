import serial
import io
from Tkinter import*
import ttk
import threading
import time

gui = Tk()
gui.title("Seatrec Serial Interface")

class Connection():

    def __init__(self):
        pass
    
    def connect(self): 
        version_ = button_var.get()
        print version_
        self.port = port_entry.get()
        self.baud = baud_entry.get() 

        try:
            if version_ == 2:
                try:
                    ser = serial.Serial('/dev/tty' + str(self.port), self.baud)
                    print "connected"
                
                except:
                    print "Cant Open Specified Port"
                    
            elif version_ == 1:
                try:
                    ser = serial.Serial('COM' + str(self.port), self.baud)
                    if ser.is_open:
                        print "connected"

                except:
                    print "Cant Open Specified Port"

            elif version_ == 3:
                try:
                    ser = serial.Serial('/dev/tty.' + str(self.port), self.baud)
                    print "connected"
                except:
                    print "Cant Open Specified Port"

        except ValueError:
            print "Enter Baud and Port"
            return


baud_entry = Entry(width = 7)
baud_entry.place(x = 100, y = 365)

port_entry = Entry(width = 7)
port_entry.place(x = 200, y = 365)

button_var = IntVar()
radio_1 = Radiobutton(text = "Windows", variable = button_var, value = 1).place(x = 500, y = 315)
radio_2 = Radiobutton(text = "Linux", variable = button_var, value = 2).place(x = 600, y = 315)
radio_3 = Radiobutton(text = "Mac", variable = button_var, value = 3).place(x = 700, y = 315)

connection_ = Connection()

connectbutton = Button(text = "Connect", command = connection_.connect).place(x = 15, y = 360)

gui.geometry('500x500')
gui.mainloop()
