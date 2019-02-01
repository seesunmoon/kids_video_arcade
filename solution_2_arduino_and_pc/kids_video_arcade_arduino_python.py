# Video: Kids Video Arcade
# https://www.youtube.com/watch?v=Y6r3-0KQ-Fw
# YouTube Channel: sunnyspeed studio
# Author: Sunny
# Usgae: This python script is listening the (arduino + coin acceptor),
#	 When there is a coin detected, the python script will trigger
#	 the web interface using selenium. 

import serial
from selenium import webdriver
from time import sleep

# the port for the arduino connected on the same computer
SERIAL_PORT = '/dev/ttyACM0'
SERIAL_RATE = 9600

ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
print "Start listening the arduino and waiting for the coin ..."

# start selenium, every coin will load the web page in the same tab (very important)
driver = webdriver.Chrome('/usr/bin/chromedriver')
link = "http://192.168.1.126:8000"
driver.get(link + "/bye")


while True:
	reading = ser.readline().strip()
	# coin detected
        if reading == "coin":
        	print(reading)
	    	# start UI via selenium
		driver.get(link)
		sleep(5)
