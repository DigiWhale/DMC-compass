import serial

ser = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)

while True:
    print(ser.readline().decode('ascii', errors='replace')) # Read the newest output from the Arduino