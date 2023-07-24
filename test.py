# importing the module
import screen_brightness_control as sbc
# import PyQt5 as Qt5
 
# get current brightness  value
current_brightness = sbc.get_brightness()
print(current_brightness)
 
# get the brightness of the primary display
primary_brightness = sbc.get_brightness(display=0)
print(primary_brightness)

sbc.set_brightness(83)
# sbc.fade_brightness(75, start=25)

