import radio
from microbit import *

radio.on()
radio.config(queue=1, channel=0)

while True:
    if pin0.read_digital():
        display.show(Image.ARROW_N)
        radio.send("1")
        while(pin0.read_digital):
            sleep(5)
        display.show(Image.NO)
        radio.send("0")

    if pin8.read_digital():
        display.show(Image.ARROW_S)
        radio.send("2")
        while(pin8.read_digital):
            sleep(5)
        display.show(Image.NO)
        radio.send("0")

    if pin1.read_digital():
        display.show(Image.ARROW_W)
        radio.send("3")
        while(pin1.read_digital):
            sleep(5)
        display.show(Image.NO)
        radio.send("0")

    if pin2.read_digital():
        display.show(Image.ARROW_E)
        radio.send("4")
        while(pin2.read_digital):
            sleep(5)
        display.show(Image.NO)
        radio.send("5")
