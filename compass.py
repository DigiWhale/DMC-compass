import serial

ser = serial.Serial(port='/dev/ttyUSB1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=5)

while True:
    in_bin = ser.readline()
    print(in_bin)