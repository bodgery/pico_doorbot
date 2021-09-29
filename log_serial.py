import datetime
import serial

SERIAL_PORT = "/dev/ttyUSB0"


port = serial.Serial( SERIAL_PORT, 115200 )

while True:
    line = port.readline()
    if not line:
        break

    dt = datetime.datetime.now()
    print( "{" + dt.isoformat( ' ' ) + "} ", end = '' )
    print( line.decode( "ascii" ), end = '' )

port.close()
