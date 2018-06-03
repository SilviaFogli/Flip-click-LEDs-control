import streams
# import the wifi interface
from wireless import wifi
# the wifi module needs a networking driver to be loaded
# in order to control the board hardware.
# THIS EXAMPLE IS SET TO WORK WITH SPWF01SA WIFI DRIVER
from stm.spwf01sa import spwf01sa as wifi_driver

# Import the Zerynth APP library
from zerynthapp import zerynthapp

streams.serial()

# set the pins as output
LED = {"LED A":D39, "LED B":D40, "LED C":D41, "LED D":D42}

for pin in LED.values():
    pinMode(pin, OUTPUT)


sleep(1000)
print("STARTING...")

try:
   # Wifi 4 Click on slot A(specify which serial port will be used and which RST pin)
    wifi_driver.init(SERIAL2,D24, baud=9600) 
except Exception as e:
    print(e)
    
for i in range(0,5):
    try:
        # connect to the wifi network (Set your SSID and password below)
        wifi.link("SSID",wifi.WIFI_WPA2,"PASSWORD") 
        break
    except Exception as e:
        print("Can't link",e)
else:
    print("Impossible to link!")
    while True:
        sleep(1000)

try:
    # Device UID and TOKEN can be created in the ADM panel
    zapp = zerynthapp.ZerynthApp("DEVICE UID", "DEVICE TOKEN", log=True)
except Exception as e:
    print(e)


# Start the Zerynth app instance!
# Remember to create a template with the files under the "template" folder you just cloned
# upload it to the ADM and associate it with the connected device
zapp.run()


def set_led(pin,status):
    
    if status == "ON":
        digitalWrite(LED[pin],HIGH)
    elif status == "OFF":
        digitalWrite(LED[pin],LOW)


# link "set_led" to the function set_led
zapp.on("set_led", set_led)

while True:
    print("....")
    sleep(1000)