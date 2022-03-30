from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD('PCF8574', 0x27, backlight_enabled = True, cols = 16, rows = 2)


def display(string, row):
    lcd.clear()
    lcd.backlight_enabled = True
    displaybuffer = ['','']
    lcd.cursor_pos = (row, 0)
    s = 16*' ' + string + 16*' '
    for i in range(len(s) - 16 + 1):
        displaybuffer[row] = s[i:i+16]
        lcd.write_string(displaybuffer[row])
        lcd.cursor_pos = (row, 0)
        sleep(0.2)
    lcd.home()
    lcd.write_string(string)

#lcd.clear()
def clear_display():
    lcd.clear()
    lcd.backlight_enabled = False