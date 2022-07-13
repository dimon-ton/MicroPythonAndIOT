from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd

i2c = SoftI2C(scl=Pin(05), sda=Pin(04), freq=100000)

#print(i2c.scan())

#hexid = hex(i2c.scan()[0])
#print(hexid)

lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.putstr('WipawadeeJubu')


