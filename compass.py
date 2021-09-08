import serial

ser = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)

while True:
    in_bin = ser.read()
    in_hex = int.from_bytes(in_bin,byteorder='little')
    print(in_hex)