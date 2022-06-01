import network
wifi = 'Dorm_Chakpong'
password = '543219876'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(wifi,password)
print(wlan.isconnected())