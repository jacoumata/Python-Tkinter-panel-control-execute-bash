#!/usr/bin/python

import Tkinter as tk
from Tkinter import *
import subprocess as sub
import tkMessageBox

WINDOW_SIZE = "470x300"

root = tk.Tk()
root.geometry(WINDOW_SIZE)
root.title('Projects Control Panel')

def DisablePanel():
#   if tkMessageBox.askokcancel("DISABLE", "DISABLE THE PANEL?"):
#       sub.call('bash cp /home/pi/.config/lxpanel/LXDE-pi/panels/panel0 /home/pi/.config/lxpanel/LXDE-pi/panels/panel', shell=True)
#       sub.call('/usr/bin/lxpanelctl restart', shell=True)
        sub.call('/usr/bin/lxpanelctl exit &>/dev/null', shell=True)

def EnablePanel():
#   if tkMessageBox.askokcancel("RE-ENABLE", "RE-ENABLE PANEL?"):
#       sub.call('/bin/cp /home/pi/.config/lxpanel/LXDE-pi/panels/panel100 /home/pi/.config/lxpanel/LXDE-pi/panels/panel', shell=True)
#       sub.call('/usr/bin/lxpanelctl restart', shell=True)
        sub.call('/usr/bin/lxpanel &> /dev/null', shell=True)

def Disconnect1():
    if tkMessageBox.askokcancel("OFF", "Turn it Off?"):
        sub.call('/usr/bin/python /home/pi/Projects/1DISCONNECT.py', shell=True)

def Restore1():
    if tkMessageBox.askokcancel("ON", "Turn it back On?"):
        sub.call('/usr/bin/python /home/pi/Projects/1RESTORE.py', shell=True)

def RestartPi():
    if tkMessageBox.askokcancel("Restart Pi", "Restart PI?"):
        sub.call('reboot', shell=True)

def on_closing():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def write_file():
    texttosave = PIIDEntry.get()
    if tkMessageBox.askokcancel("New ID", "Save new ID: " + texttosave + " ?"):
        with open("PIID.txt", "w") as f:
            f.write(texttosave)
            tkMessageBox.showwarning("Saved","PI ID is now set to: " + texttosave)


Disconnect1Btn = tk.Button(root, text ="Disconnect power on Relay #1", command = Disconnect1)
Restore1Btn = tk.Button(root, text ="Restore power on Relay #1", command = Restore1)
DisablePanelBtn = tk.Button(root, text ="Disable Panel", command = DisablePanel)
EnablePanelBtn = tk.Button(root, text ="Enable Panel", command = EnablePanel)
RestartPiBtn = tk.Button(root, text ="Restart Raspberry PI", command = RestartPi)
CloseBtn = tk.Button(root, text ="Close", command = on_closing)

EntryBtn = tk.Button(root, text ="Set new ID", command = write_file)
PIIDEntry = Entry(root)
LabelPIID = Label(root, text="Rename this PI ID")

DisablePanelBtn.pack()
EnablePanelBtn.pack()
Disconnect1Btn.pack()
Restore1Btn.pack()
LabelPIID.pack()
PIIDEntry.pack()
EntryBtn.pack()
RestartPiBtn.pack(side=tk.LEFT)
CloseBtn.pack(side=tk.BOTTOM)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
