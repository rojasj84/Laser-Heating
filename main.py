# Importing python libraries
import tkinter as tk
from PIL import ImageTk, Image

# Importing local libraries
from agilis_control import *
from denkovi_serial import *
from acton_pixis import *
from piezo_motor_control import *
from laser_communication import *
from festo_control import *

win_color = "light gray"

#Global variables to store laser IPs and COM Ports for the various systems

left_laser_ip = "192.168.0.100"
right_laser_ip = "192.168.1.100"
agilis_com_port = "COM3"
left_denkovi_com_port = "COM7"
right_denkovi_com_port = "COM6"

class Laser_Controls(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Laser Control Window")
        self.geometry("505x1010")
        InitiatePiezoMotorControls(self,0,0)
        LaserCommunication(self,left_laser_ip, 20,565)
        LaserCommunication(self,right_laser_ip, 260,565)      

class Festo_Controls(tk.Toplevel):
     def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Festo Control Window")
        self.geometry("280x445")
        FestoControlWindow(self, left_denkovi_com_port, right_denkovi_com_port)

# Function to open various windows in the program
def open_window(window_value, window_in_question):
    if window_in_question.winfo_exists(): #Checks if the window in question already exists
            do_nothing()
    else:
        if window_value == 1:   #Check for which window to reopen               
            globals()['LaserControlWindow'] = Laser_Controls()        
        elif window_value == 2:   #Check for which window to reopen               
            globals()['FestControlWindow'] = Festo_Controls()            
        else:
            do_nothing()
    

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    window = tk.Tk()
    window.title("EPL Laser Heating Control")
    window.geometry("1280x1010")

    ico = Image.open("images/laser-icon.png")
    photo = ImageTk.PhotoImage(ico)
    window.wm_iconphoto(False, photo)
    
    #Creating a top menu
    menu_bar = tk.Menu(window)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=window.quit)
    menu_bar.add_cascade(label="Main", menu=file_menu)

    # Create a Spectrometer menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="High Temperature", command=do_nothing)
    edit_menu.add_command(label="Low Temperature", command=do_nothing)
    edit_menu.add_command(label="2D", command=do_nothing)
    menu_bar.add_cascade(label="Spectrometer", menu=edit_menu)

    # Create a Communications menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="COM Ports", command=do_nothing)
    edit_menu.add_command(label="Laser IPs", command=do_nothing)
    menu_bar.add_cascade(label="Communications", menu=edit_menu)

    # Create a Windows menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Piezo Controls", command=lambda: open_window(1, LaserControlWindow))
    edit_menu.add_command(label="Festo Controls", command=lambda: open_window(2, FestControlWindow))
    menu_bar.add_cascade(label="Windows", menu=edit_menu)


    # Add the menu bar to the window
    window.config(menu=menu_bar)

    ActonControlWindow = ActonPixis = InitiateActonTfit(window, 0,0)
    LaserControlWindow = Laser_Controls()
    FestControlWindow = Festo_Controls()
    FestControlWindow.destroy() #Removing festo control from display since the user doesn't normally need to access directly the Festo States

    window.mainloop()