#Testing GIT
import board
import adafruit_bno055
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk
import time
from tkinter import *

i2c = board.I2C()
s = adafruit_bno055.BNO055_I2C(i2c)
last_val = 0xFFFF

GPIO.setmode(GPIO.BCM)
a = 16
b = 17
c = 19
d = 20

GPIO.setup(a, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(d, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

active_window = "root"

def stop_vib_vals():
    v.after_cancel(task_id)
    show_main_menu()

def myloop():
    global task_id
    x = s.linear_acceleration[0]
    if x:
        x = round(x, 2)
    else:
        x = 0.00
    x_val.configure(text=x)
    y = s.linear_acceleration[1]
    if y:
        y = round(y, 2)
    else:
        y = 0.00
    y_val.configure(text=y)
    z = s.linear_acceleration[2]
    if z:
        z = round(z, 2)
    else:
        z = 0.00
    z_val.configure(text=z)
    task_id = v.after(100, myloop)

def show_vib_vals():
    v.after(1, myloop)
    v.mainloop()


def show_main_menu():
    root.deiconify()

def launch_vibration_win():
    global x_val, y_val, z_val,v
    v = tk.Tk()
    v.title("Vibration Analyzer")
    v.geometry(("400x400+0+0"))
    root.withdraw()
    v.rowconfigure(0, weight=1)
    v.rowconfigure(1, weight=1)
    v.rowconfigure(2, weight=1)
    v.rowconfigure(3, weight=1)
    v.rowconfigure(4, weight=1)
    v.columnconfigure(0, weight=1)
    v.columnconfigure(1, weight=1)
    vib_lbl = tk.Label(v, text="Vibration Analyzer", font=("Arial", 24))
    vib_lbl.grid(column=0, row=0,columnspan=2, padx=5, pady=5)
    start_but = tk.Button(v, text="Start", font=("Arial", 14), command=show_vib_vals)
    start_but.grid(column=0, row=1, padx=5, pady=5)
    stop_but = tk.Button(v, text="Stop", font=("Arial", 14), command=stop_vib_vals)
    stop_but.grid(column=1, row=1, padx=5, pady=5)
    x_vib_lbl = tk.Label(v, text="ACC-X", font=("Arial", 14))
    x_vib_lbl.grid(column=0, row=2, padx=5, pady=5)
    y_vib_lbl = tk.Label(v, text="ACC-Y", font=("Arial", 14))
    y_vib_lbl.grid(column=0, row=3, padx=5, pady=5)
    z_vib_lbl = tk.Label(v, text="ACC-Z", font=("Arial", 14))
    z_vib_lbl.grid(column=0, row=4, padx=5, pady=5)

    x_val = tk.Label(v, text="0.00", font=("Arial", 14))
    x_val.grid(column=1, row=2, padx=5, pady=5)
    y_val = tk.Label(v, text="0.00", font=("Arial", 14))
    y_val.grid(column=1, row=3, padx=5, pady=5)
    z_val = tk.Label(v, text="0.00", font=("Arial", 14))
    z_val.grid(column=1, row=4, padx=5, pady=5)
    


def launch_manuals_win():
    global manuals
    manuals = Toplevel()
    manuals.title("CAT Manuals")
    manuals.geometry(("750x400+0+0"))
def launch_ro_win():
    global ro
    ro = Toplevel()
    ro.title("RO Plants")
    ro.geometry(("750x400+0+0"))
def launch_inv_win():
    global inv
    inv = Toplevel()
    inv.title("Inventory")
    inv.geometry(("750x400+0+0"))
def launch_reports_win():
    global reports
    reports = Toplevel()
    reports.title("Reports")
    reports.geometry(("750x400+0+0"))
def launch_utils_win():
    global utils
    utils = Toplevel()
    utils.title("Utilities")
    utils.geometry(("750x400+0+0"))
def launch_dev1_win():
    global dev1
    dev1 = Toplevel()
    dev1.title("DEV1")
    dev1.geometry(("750x400+0+0"))

def launch_dev2_win():
    global dev2
    dev2 = Toplevel()
    dev2.title("DEV2")
    dev2.geometry(("750x400+0+0"))

def launch_dev3_win():
    global dev3
    dev3 = Toplevel()
    dev3.title("DEV3")
    dev3.geometry(("750x400+0+0"))

def launch_dev4_win():
    global dev4
    dev4 = Toplevel()
    dev4.title("DEV4")
    dev4.geometry(("750x400+0+0"))

def launch_dev5_win():
    global dev5
    dev5 = Toplevel()
    dev5.title("DEV5")
    dev5.geometry(("750x400+0+0"))

def launch_incidents_win():
    global incidents
    incidents = Toplevel()
    incidents.title("Incidents")
    incidents.geometry(("750x400+0+0"))

def checkvalve():
    pass

def reset_buttons():
    for i in root_buttons:
        i.configure(bg="white")    


root = tk.Tk()
root.title("PRD_ASSIST_DEVICE")
root.geometry("750x400+0+0") # Width=800px, Height=600px
logo = tk.PhotoImage(file='logo.png')
root.iconphoto(False, logo)
root.configure(bg="black")
root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)


vibration_button = tk.Button(root, text="Vibration", width=15, height=2, activebackground="green", bg="white", font=("Arial", 14), command=launch_vibration_win)
vibration_button.grid(column=0, row=0, padx=5, pady=5)

manuals_button = tk.Button(root, text="CAT Manuals", width=15, height=2, activebackground="green", bg="white", font=("Arial", 14), command=launch_manuals_win)
manuals_button.grid(column=1, row=0, padx=5, pady=5)

ro_button = tk.Button(root, text="RO Plants", width=15, height=2, activebackground="green", bg="white", font=("Arial", 14), command=launch_ro_win)
ro_button.grid(column=2, row=0, padx=5, pady=5)

inventory_button = tk.Button(root, text="Inventory", activebackground="green", bg="white", command=checkvalve, width=15, height=2, font=("Arial", 14))
inventory_button.grid(column=0, row=1, padx=5, pady=5)

reports_button = tk.Button(root, text="Reports", width=15, height=2, activebackground="green", bg="white", font=("Arial", 14))
reports_button.grid(column=1, row=1, padx=5, pady=5)

utilities_button = tk.Button(root, text="Utilities", width=15, height=2, bg="white", activebackground="green", font=("Arial", 14))
utilities_button.grid(column=2, row=1, padx=5, pady=5)

dev1_button = tk.Button(root, text="Dev~1", bg="white", activebackground="green", command=checkvalve, width=15, height=2, font=("Arial", 14))
dev1_button.grid(column=0, row=2, padx=5, pady=5)

dev2_button = tk.Button(root, text="Dev~2", width=15, height=2, bg="white", activebackground="green", font=("Arial", 14))
dev2_button.grid(column=1, row=2, padx=5, pady=5)

dev3_button = tk.Button(root, text="Dev~3", width=15, height=2, bg="white", activebackground="green", font=("Arial", 14))
dev3_button.grid(column=2, row=2, padx=5, pady=5)


dev4_button = tk.Button(root, text="Dev~4", bg="white", activebackground="green", command=checkvalve, width=15, height=2, font=("Arial", 14))
dev4_button.grid(column=0, row=3, padx=5, pady=5)

dev5_button = tk.Button(root, text="Dev~5", width=15, height=2, bg="white", activebackground="green", font=("Arial", 14))
dev5_button.grid(column=1, row=3, padx=5, pady=5)

incidents_button = tk.Button(root, text="Incidents", width=15, height=2, bg="white", activebackground="green", font=("Arial", 14))
incidents_button.grid(column=2, row=3, padx=5, pady=5)

active_button = -1
root_buttons = [vibration_button, manuals_button, ro_button, inventory_button, reports_button, utilities_button, dev1_button, dev2_button, dev3_button, dev4_button, dev5_button, incidents_button]



def right_cb(channel):
    global active_button 
    reset_buttons()
    for i in root_buttons:
        i.configure(activebackground=None)
    for i in root_buttons:
        i.configure(bg="white")
    active_button = active_button+1
    if (active_button > 11):
        active_button = 11
    root_buttons[active_button].configure(bg="green")
def down_cb(channel):
    global active_window
    if active_window == "root":
        if (active_button == 0):
            active_window = "vibration"
            print(active_button)
        elif (active_button == 1):
            active_window = "manuals"
            print(active_button)
        elif (active_button == 2):
            active_window = "ro"
            print("RO")
        elif (active_button == 3):
            active_window = "inv"
            print("INV")
        elif (active_button == 4):
            active_window = "reports"
        elif (active_button == 5):
            active_window = "utils"
        elif (active_button == 6):
            active_window = "dev1"
        elif (active_button == 7):
            active_window = "dev2"
        elif (active_button == 8):
            active_window = "dev3"
        elif (active_button == 9):
            pass
            active_window = "dev4"
        elif (active_button == 10):
            pass
            active_window = "dev5"
        elif (active_button == 11):
            pass
            active_window = "incidents"

    if active_window == "vibrations":
        launch_vibration_win()
    if active_window == "manuals":
        pass
    if active_window == "ro":
        pass
    if active_window == "inv":
        pass
    if active_window == "reports":
        pass
    if active_window == "utils":
        pass
    if active_window == "dev1":
        pass
    if active_window == "dev2":
        pass
    if active_window == "dev3":
        pass
    if active_window == "dev4":
        pass
    if active_window == "dev5":
        pass
    if active_window == "incidents":
        pass


def left_cb(channel):
    global active_button
    reset_buttons()
    active_button = active_button-1
    if (active_button < 0):
        active_button = 0
    root_buttons[active_button].configure(bg="green")
def d_cb(channel):
    root.deiconify()


GPIO.add_event_detect(a, GPIO.RISING, callback=left_cb, bouncetime=300)
GPIO.add_event_detect(b, GPIO.RISING, callback=down_cb, bouncetime=300)
GPIO.add_event_detect(c, GPIO.RISING, callback=right_cb, bouncetime=300)
GPIO.add_event_detect(d, GPIO.RISING, callback=d_cb, bouncetime=300)

root.mainloop()




# except KeyboardInterrupt:
#     print("Program Exited")
# finally:
#     GPIO.cleanup()


