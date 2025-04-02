"""
MacroPad boot.py
"""

import board
import supervisor
import digitalio
import storage
import usb_hidimport usb_cdc
import usb_midi


supervisor.set_usb_identification("VicPads", 'MacroPad') # USB id strings
# If encoder button is held during boot, don't run the code which hides the storage
button = digitalio.DigitalInOut(board.D9)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive() # Hides device storage
    usb_cdc.disable() # Disables serial comunication
    usb_midi.disable() # Disables midi
    usb_hid.enable(boot_device=1) # Enables keyboard before OS boot
    
button.deinit()