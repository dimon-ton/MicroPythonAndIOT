from machine import Pin
relay = Pin(16, Pin.OUT)
led = Pin(5, Pin.OUT)

led.on()

def relay_on():
    relay.off()

def relay_off()
    relay.on()

