# afaidk
# Copied somewhere from internet
# This file will make SH1106 work.
# If your oled screen does not work, copy this file to esp filesystem.
# then use this class, instead of ssd1306


# Example by afaidk
# Connection diagram
#      DISPLAY   ====    NodeMCU
#      VCC       ====    5V (Vin of NodeMCU will work.)
#      GND       ====    GND
#      SCL       ====    D1 (GPIO5 in NodeMCU)
#      SDA       ====    D2 (GPIO4 in NodeMCU)

#import sh1106
#from machine import Pin, I2C
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
#display = sh1106.SH1106_I2C(128, 64, i2c)
#display.fill(1)
#display.show()

# All the functions in ssd1306 should work, since this class is extending it.

from ssd1306 import SSD1306_I2C

SET_LOW_COLUMN      = const(0x00)
SET_HIGH_COLUMN     = const(0x10)
SET_PAGE_ADDR       = const(0xb0)
SET_DISP_START_LINE = const(0x40)

class SH1106_I2C(SSD1306_I2C):
  def show(self):
    for pg in range(0, self.pages):
        for cmd in (SET_PAGE_ADDR | pg, SET_LOW_COLUMN | 2, SET_HIGH_COLUMN | 0, ):
            self.write_cmd(cmd)
        self.write_data(self.buffer[pg * 0x80:(pg + 1) * 0x80])


