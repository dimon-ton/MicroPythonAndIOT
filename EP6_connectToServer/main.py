import socket
import network
import time
from machine import Pin

#####################
#serverip = '178.128.125.82'
serverip = '192.168.0.22'
port = 9000
#####################

def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:' , data_server)
    server.close()
    
# connect to wifi
wifi = 'Dorm_Chakpong'
password = '543219876'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2)

wlan.connect(wifi,password)
time.sleep(2)

print(wlan.isconnected())


led = Pin(14,Pin.OUT)


#for i in range(5):
for i in range(1):
    send_data('LED1:ON')
    led.on()
    time.sleep(1)
    send_data('LED1:OFF')
    led.off()
    time.sleep(1)