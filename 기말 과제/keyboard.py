import serial
from pynput.keyboard import Controller

# Arduino와 연결
arduino = serial.Serial('COM3', 9600)  # COM 포트는 자신의 포트로 변경
keyboard = Controller()

while True:
    if arduino.in_waiting > 0:
        key = arduino.readline().decode('utf-8').strip()  # 시리얼 입력 읽기
        if key in ['d', 'f', 'j', 'k']:
            keyboard.press(key)  # 키 누름
            keyboard.release(key)  # 키 뗌
