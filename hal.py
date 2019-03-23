# Setup a very simple hal for the desired board
# It is not intended that this mimic the WPILIB hal at all.  It should just be a basic method
# of setting up different boards (PyBoard, Feather, etc..)

'''
Notes on esp8266 - Adafruit Feather Huzzah

On Windows, list COM Ports with:
(Get-WmiObject -query "SELECT * FROM Win32_PnPEntity" | Where {$_.Name -Match "COM\d+"}).name

Imaged feather with:
py -m esptool --port COM4 erase_flash
py -m esptool --port COM4 --baud 460800 write_flash --flash_size=detect 0 esp8266-20180511-v1.9.4.bin

use ampy to work with files on the board
https://github.com/adafruit/ampy

Quick reference:
 http://docs.micropython.org/en/latest/esp8266/quickref.html
 https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/pinouts

 Note that these pins on the feather are the numbers printed on the board (purple in the schematic)
 GPIO Pins: 0, 2, 4, 5, 12, 13, 14, 15, and 16 
 PWM Pins: 0, 2, 4, 5, 12, 13, 14 and 15
 ADC: ADC(0)  -- can only read 0 - 1V
'''

