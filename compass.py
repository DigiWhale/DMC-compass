import serial
import redis

ser = serial.Serial(port='/dev/ttyUSB_DMC', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=5)
print("Connected to: " + ser.portstr)
r = redis.Redis(host='192.168.1.4', port=6379, db=0, password='Redis2019!')
while True:
    in_bin = ser.readline()
    print(in_bin)
    if in_bin.strip().find(b'$HCHDG')==0:
        data_list = in_bin.strip().decode('utf-8').split(',')
        r.hmset('DMC', {'heading': data_list[1]})
        print('set redis heading')