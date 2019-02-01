# Video: Kids Video Arcade
# https://www.youtube.com/watch?v=Y6r3-0KQ-Fw
# YouTube Channel: sunnyspeed studio
# Author: Sunny
# Usgae: With the GPIO on Raspberry pi, the python script is very simple.
#	 However, I found out that RPI doesn't play 1080P YouTube smoothly enough. 

from gpiozero import Button
from time import sleep
from selenium import webdriver

# using GPIO 2
button = Button(2)

# prepare selenium
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
link = "http://192.168.1.126:8000"
driver.get(link + "/bye")

while True:
    if button.is_pressed:
        print("coin")
	driver.get(link)
	sleep(5)
