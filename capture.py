import time
import serial



with serial.Serial('/dev/ttyUSB1', 9600, timeout=0.1) as ser:

    # You send a word that will trigger the hardware to begin
	x=ser.read(2)


	y=ser.write(b'\x61')

    # Define the length of the captured output sequence 
	x = ser.read(80) 


	file=open("./results.txt","a")
	z = x.hex()+"\n"
	file.write(z)
	file.close()





