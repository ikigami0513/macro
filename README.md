# Macro
Macro software write in python.
This software is written for azerty keyboard. You may be change value in macro.py for it to work with qwerty keyboard.

# Installation
  1 - install https://zadig.akeo.ie/# .<br/>
  2 - open Zadig and choose in Options "List All Devices".<br/>
  ![image](https://user-images.githubusercontent.com/98080123/213912263-a24a3f4e-2348-4a99-a967-41f7992877a2.png)<br/>
  3 - next, choose your second keyboard and install "libusb-win32 (v1.2.6.0)." <br/>
  ![image](https://user-images.githubusercontent.com/98080123/213912540-12dc7482-86fe-4c2c-aab3-dabac67ac7ae.png)<br/>
  open macro.py and change the values of VENDOR_ID and PRODUCT_ID with usb_id in Zadig (VENDOR_ID is left value and PRODUCT_ID is right value).<br/>
  <b>WARNING : leave the 0x in front of the value.</b><br/>
  4 - now, open command.json. In this file, write your bash command associated with each key.<br/>
  <b>WARNING : don't delete key in command.json file even if there are no associated commands.</b><br/>
  5 - now, press win + r on your main keyboard and write in the window that has just appeared : shell:startup. In this folder, create shortcut to the start.vbs file.
  6 - restart your computer. Your macro finally work.
  
# Update command.json without restart your computer
  1 - update your command.json and save it.
  2 - press echap key in your macro keyboard.
  3 - close the window that has just appeared.
  4 - that's all
