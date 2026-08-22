# open port 
import serial
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port

in this case code opens per default this: (it is pretty standard anyways, especially the baud rate and parity)

serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=None
)

# make timeout 
with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
    x = ser.read()          # read one byte
    s = ser.read(10)        # read up to ten bytes (timeout)
    line = ser.readline()   # read a '\n' terminated line


Timeout is how long a program will wait for data before it stops (and returns an error message)
In the specific example we ask the code to wait for 10 bytes, when those arrive, the code can move on. This can of course happen in less than 1s, so that's when the code will move on. But it will not wait for longer than 1 second.


Comparing the chatGPT code with DAQ one: 
parity='E',  yes
stopbits=1,  yes
timeout=0,  yes
rtscts=True handshake 

# Handshake 
a way to ensure that communication is seamless and the sender and receiver don't "talk over each other". So before sending the data, the sender ensures there is someone to listen (Clear to Send = CTS). Same for the receiver, he request a message (Request to Send = RTS). 

But not every devise supports that

# ## Configuring ports
Configuring a port is just asking it to exist and actually opening mean building up a connection 

ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM1'
ser
Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
ser.open()
ser.is_open
True
ser.close() -> **closes port in any case, if the normal way didn't work** 
ser.is_open
False

with serial.Serial() as ser:
    ser.baudrate = 19200
    ser.port = 'COM1'
    ser.open() **port actually connects to pyserial**
    ser.write(b'hello') **anytime 'b' means byte** 

