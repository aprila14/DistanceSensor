import serial

def bytes_to_int(bytes):
    result = 0
    result2 = ''
    for b in bytes:
        result = str(chr(b))
        result2 = result2 + result
    return result2


arduino = serial.Serial('COM4', 115200, timeout=.01)
print(arduino)

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        datastr = bytes_to_int(data)
        len = int(datastr)*0.05
        print(len)