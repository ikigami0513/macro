import usb.core
import usb.util
import os
import json
import tkinter

def setCommands():
    with open('./command.json') as json_file:
        return json.load(json_file)

class MajCommand:
    def __init__(self):
        self.root = tkinter.Tk()
        tkinter.Label(self.root, text="Les commandes de macro ont bien été mises à jour.").pack()
        self.root.mainloop()

VENDOR_ID = 0x413C
PRODUCT_ID = 0x2107

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
device.set_configuration()
endpoint = device[0][(0,0)][0]
i = 2
command = setCommands()
while True:
    attempts = 10
    data = None
    while data is None and attempts > 0:
        try:
            data = device.read(endpoint.bEndpointAddress,
                               endpoint.wMaxPacketSize)
        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):
                attempts -= 1
                continue

    if data[i] != 0: 
        print(data[i])
        #A
        if data[i] == 20:
            os.system(command["A"])
        #Z
        elif data[i] == 26:
            os.system(command["Z"])
        #E
        elif data[i] == 8:
            os.system(command["E"])
        #R
        elif data[i] == 21:
            os.system(command["R"])
        #T
        elif data[i] == 23:
            os.system(command["T"])
        #Y
        elif data[i] == 28:
            os.system(command["Y"])
        #U
        elif data[i] == 24:
            os.system(command["U"])
        #I
        elif data[i] == 12:
            os.system(command["I"])
        #O
        elif data[i] == 18:
            os.system(command["O"])
        #P
        elif data[i] == 19:
            os.system(command["P"])
        #Q
        elif data[i] == 4:
            os.system(command["Q"])
        #S
        elif data[i] == 22:
            os.system(command["S"])
        #D
        elif data[i] == 7:
            os.system(command["D"])
        #F
        elif data[i] == 9:
            os.system(command["F"])
        #G
        elif data[i] == 10:
            os.system(command["G"])
        #H
        elif data[i] == 11:
            os.system(command["H"])
        #J
        elif data[i] == 13:
            os.system(command["J"])
        #K
        elif data[i] == 14:
            os.system(command["K"])
        #L
        elif data[i] == 15:
            os.system(command["L"])
        #M
        elif data[i] == 51:
            os.system(command["M"])
        #W
        elif data[i] == 29:
            os.system(command["W"])
        #X
        elif data[i] == 27:
            os.system(command["X"])
        #C
        elif data[i] == 6:
            os.system(command["C"])
        #V
        elif data[i] == 25:
            os.system(command["V"])
        #B
        elif data[i] == 5:
            os.system(command["B"])
        #N
        elif data[i] == 17:
            os.system(command["N"])
        #echap
        elif data[i] == 41:
            command = setCommands()
            MajCommand()
