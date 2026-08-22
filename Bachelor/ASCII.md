a way to follow the [[PySerial|serial]] communication for easier debugging. Instead 1 and 0 we get some letters and words to see what's actually happening. 
We can ask the devises to give sounds from them 

# talk to me
ser.write(b"hello")
	
dear devise, please say "hello" and every letter is a byte data type 


# Huh? what are you saying? 
we need to print out what our guy is saying 
		data = ser.read(2)
		print(data)


# \r = Carriage Return (CR)
go back in time, to the time of typewriters! at the end of executing the line of the code the "carriage" returns to the beginning and is ready to go again 

# \n = Line Feed 
That is a new line, basically "enter". In typewriter language it is the paper being moved up 

Ideally do both: $$\text{\r\n}$$

