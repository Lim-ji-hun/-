import serial
from pynput.keyboard import Controller
import os

serial_port = '/dev/ttyACM0' 
baud_rate = 9600

arduino = serial.Serial(serial_port, baud_rate)
keyboard = Controller()

print("Listening for Arduino input...")

try:
    while True:
        if arduino.in_waiting > 0:
            key = arduino.readline().decode('utf-8').strip()  
            if key in ['d', 'f', 'j', 'k']:
                print(f"Key received: {key}")  
                keyboard.press(key) 
                keyboard.release(key)
except KeyboardInterrupt:
    print("Program stopped.")
finally:
    arduino.close()
