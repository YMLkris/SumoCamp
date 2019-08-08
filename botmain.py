
import radio
from microbit import *
import seesaw

radio.on()
radio.config(queue=1, channel=0)

while True:

    incoming = radio.receive()
    if incoming == "0":
        seesaw.motor(1, 0)
        seesaw.motor(2, 0)

    if incoming == "1":
        seesaw.motor(1, .5)
        seesaw.motor(2, .5)
    if incoming == "2":
        seesaw.motor(1, -.5)
        seesaw.motor(2, -.5)
    if incoming == "0":
        seesaw.motor(1, -.5)
        seesaw.motor(2, .5)
    if incoming == "0":
        seesaw.motor(1, .5)
        seesaw.motor(2, -.5)

    sleep(5)
