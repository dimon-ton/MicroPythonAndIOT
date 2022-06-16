from machine import Pin
import dht
import time

d = dht.DHT22(Pin(16))


for i in range(100):
    d.measure()
    time.sleep(1)
    tem = d.temperature()
    humid = d.humidity()
    print(f'The temperature is {tem}')
    print(f'The humidity is {humid}')
    print('--------------------------------')