"""
Name: OneLEDBlink.py
Purpose: To turn On and Off the LED in a loop 

Requirements: Micropython and ESP32 board

For more projects, visit www.micropythonforu.com

"""

from machine import Pin
from time import sleep_ms

# ESP32 board's GPIO pin 16 is used to connect the LED
# Replace this numner as per your circuit configuration

p32 = Pin(16, Pin.OUT)

print("Starting loop, use Ctrl-C to break out.")
while(True):
    try:
        p32.on()
        sleep_ms(500)  # Sleep for 500 milliseconds
        p32.off()
        sleep_ms(500)
    except KeyboardInterrupt: # Ctrl-C to come out of loop
        print("User Interruption, exiting loop")
        break
    
