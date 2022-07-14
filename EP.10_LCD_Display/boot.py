from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
import time

i2c = SoftI2C(scl=Pin(05), sda=Pin(04), freq=100000)

#print(i2c.scan())

#hexid = hex(i2c.scan()[0])
#print(hexid)

lcd = I2cLcd(i2c, 0x27, 2, 16)
#String
#lcd.putstr('WipawadeeJubu')
#CHAR from ROM
#lcd.putchar(chr(126))

#Custom Char 0-7

#lcd.backlight_off()

smile = bytearray([0x00, 0x00, 0x0A, 0x00, 0x11, 0x0E, 0x00,  0x00])
angry = bytearray([0x00, 0x00, 0x11, 0x0A, 0x00, 0x0E, 0x11, 0x00])
  
lcd.custom_char(1, angry)
lcd.custom_char(0, smile)

lcd.putchar(chr(0))
lcd.move_to(2,0) #move_to(column --> index 2, row --> index 0)
lcd.putchar(chr(1))

#display backlight on-off
"""
for i in range(10):
  lcd.backlight_off()
  time.sleep(2)
  lcd.backlight_on()
  time.sleep(2)
"""

#display on-off
"""
lcd.display_off()
lcd.display_on()
"""
#lcd.blink_cursor_off()
lcd.blink_cursor_on()
time.sleep(5)
lcd.hide_cursor()