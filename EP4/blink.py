from machine import Pin
import time
 led = Pin(14,Pin.OUT)
 led.on()
 led.off()

def blink(t):
    time.sleep(t)
    led.on()
    time.sleep(t)
    led.off()
    
blink(0.5)

for i in range(10):
    blink(0.5)