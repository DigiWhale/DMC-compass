import serial

ser = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)

while True:
    in_bin = ser.readline()
    print(in_bin[0:len(in_bin)-2].decode("utf-8"))