import serial

ser = serial.Serial(port='/dev/ttyUSB1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=5)

while True:
    in_bin = ser.readline()
    in_hex = hex(int.from_bytes(in_bin,byteorder='little'))
    print(in_bin, in_hex)