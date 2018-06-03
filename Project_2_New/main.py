# Project 2
# Created at 2018-05-16 13:42:31.299017

import streams
from wireless import wifi
from stm.spwf01sa import spwf01sa as wifi_driver

from zerynthapp import zerynthapp

streams.serial()

# set the pins as output
LED = {"LED A":D39, "LED B":D40, "LED C":D41, "LED D":D42}

for pin in LED.values():
    pinMode(pin, OUTPUT)


sleep(1000)
print("STARTING...")

try:
    wifi_driver.init(SERIAL2,D24, baud=9600) #slot B
except Exception as e:
    print(e)
    
for i in range(0,5):
    try:
        wifi.link("TOI",wifi.WIFI_WPA2,"!FH565sjkwork!") #ID e PASSWOR - WIFI MAST
        break
    except Exception as e:
        print("Can't link",e)
else:
    print("Impossible to link!")
    while True:
        sleep(1000)

try:
    zapp = zerynthapp.ZerynthApp("A1TJrua5TUip94vaFgDK7A", "Ru2Bx_0WTX2FoFAIN_Hh_g", log=True)
except Exception as e:
    print(e)



zapp.run()


def set_led(pin,status):
    
    if status == "ON":
        digitalWrite(LED[pin],HIGH)
    elif status == "OFF":
        digitalWrite(LED[pin],LOW)



# def print_something(value):
#     print(value)

# zapp.on("print", print_something)

zapp.on("set_led", set_led)

while True:
    print("....")
    sleep(1000)
