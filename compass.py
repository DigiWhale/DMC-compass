import serial

ser = serial.Serial('/dev/ttyUSB1', 115200)

while True:
    print(ser.readline()) # Read the newest output from the Arduino