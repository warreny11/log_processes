import Tkinter
from SCRIPT import Connection
import time
from Tkinter import *
from serialporttester import serial_ports, glob

class Application(Frame,Connection):
    
    def connection(self):
        
        available_ports = serial_ports


        
        # Windows = Radiobutton(text = "Windows", variable = button_var, value = 1).place(x = 10, y = 315)
        # Linux = Radiobutton(text = "Linux", variable = button_var, value = 2).place(x = 110, y = 315)
        # Mac = Radiobutton(text = "Mac", variable = button_var, value = 3).place(x = 210, y = 315)
        
        # button_var = IntVar()
        # version_ = button_var.get()
        # port = port.get()
        # baud = baud.get() 

        
        # try:
        #     if version_ == 2:
                
        #         port = '/dev/tty' + str(port)
        #         baud = baud

        #     elif version_ == 1:
        #         port = 'COM' + str(port)
        #         baud = baud

        #     elif version_ == 3:
        #         port = '/dev/tty.' + str(port)
        #         baud = baud
                
        #connect_ = Button(text = "Connect", command = self.connect).place(x = 15, y = 360)


        
    # def createWidgets(self):
    #     self.QUIT = Button(self)
    #     self.QUIT["text"] = "QUIT"
    #     self.QUIT["fg"]   = "red"
    #     self.QUIT["command"] =  self.quit

    #     self.QUIT.pack({"side": "left"})

    #     self.hi_there = Button(self)
    #     self.hi_there["text"] = "Connect",
    #     self.hi_there["command"] = self.connect

    #     self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.connection
        #self.createWidgets()

    
        

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

