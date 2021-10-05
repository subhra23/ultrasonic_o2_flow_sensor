import time
import serial
from ast import literal_eval

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

def data():
    return hex(ord(ser.read()))

def hex_to_dec(str1,str2):
    a=str1
    b=str2
    c=b[2:]
    d=a+c
    res = literal_eval(d)
    return res/10

while 1:
#    ser.write(str.encode("b'\0x11\0x01\0x01\0xED'"))
    i=0
    bytes=[]
    x = data()
    #print(x)
    if(x=='0x16'):
        while(i<=12):
            bytes.append(x)
            x=data()
            i=i+1
            if(i==12):
                #conc=(bytes[3]+bytes[4])
                #print('conc = ', conc)
                conc=hex_to_dec(bytes[3],bytes[4])
                print('conc = ',conc,'%')
                #flow=(bytes[5]+bytes[6])
                flow=hex_to_dec(bytes[5],bytes[6])
                print('flow = ',flow,'L/min')
                #temp=(bytes[7]+bytes[8])
                temp=hex_to_dec(bytes[7],bytes[8])
                print('temp = ',temp,'C')
                print(bytes)
