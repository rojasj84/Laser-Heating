# Importing python libraries
import tkinter as tk
from PIL import ImageTk, Image

# Importing local libraries
from agilis_control import *
from denkovi_serial import *
from acton_pixis import *
from piezo_motor_control import *
from laser_communication import *

win_color = "light gray"

if __name__ == "__main__":

    #***** Building USER GUI *****

    # Begin code with window code
    #This is a code test 
    window = tk.Tk()
    window.title("EPL Laser Heating Control")
    window.geometry("1800x1010")
    #window.configure(bg="Medium Gray")

    ico = Image.open("images/laser-icon.png")
    photo = ImageTk.PhotoImage(ico)
    window.wm_iconphoto(False, photo)
    
    ActonPixis = InitiateActonTfit(0,0)
    PiezoMotors = InitiatePiezoMotorControls(1280,0)
    left_laser_control = LaserCommunication("192.168.1.100", 1290,570)
    right_laser_control = LaserCommunication("192.168.0.100", 1540,570)

    window.mainloop()