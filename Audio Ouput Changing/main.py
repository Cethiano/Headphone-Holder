import serial
import subprocess

reader = serial.Serial('COM7', 115200)

lastInputs = []

while True:
    distance = reader.readline().decode().strip()
    print(distance, lastInputs)
    if distance == "-1":
        if len(lastInputs) <= 4:
            lastInputs.append(distance)
    else:
        lastInputs.clear()

    if len(lastInputs) == 4:
        subprocess.run(["launcher.bat"], shell=False)

    if len(lastInputs) > 4 and not distance == "-1":
        lastInputs.clear()

