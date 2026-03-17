import serial

reader = serial.Serial('COM7', 115200)
while True:
    print(reader.readline().decode())
