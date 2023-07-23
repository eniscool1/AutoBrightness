# importing the module
import screen_brightness_control as sbc
import pyqt5 as qt5
 
# get current brightness  value
current_brightness = sbc.get_brightness()
print(current_brightness)
 
# get the brightness of the primary display
primary_brightness = sbc.get_brightness(display=0)
print(primary_brightness)

sbc.set_brightness(83)