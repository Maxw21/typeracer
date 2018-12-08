# Type Racer Winner
# Description: Plays the game "Type Racer" and will get a high words per minute This is done by analyzing the words given in the passage and typing out the correct letters
# Maxfield Wilhoite 2018

import pyautogui, random, time, Tkinter
#from Tkinter import *

testStr = "testing the typing speed"
inBuffer = "testing input speeds is very import, if i didn't test this and the timing was too quick, the website would not process the input. I realised that 0 seconds was too short as it would output the whole string in one input. That is not good for business. Thus I randomized the interval time between 0.01 and 0 to reduce typing speed and to not flag myself as a bot typing at a constant speed."
outBuffer = ""
scanning = True

pyautogui.click(pyautogui.size())

#for char in range(0, len(testStr)):
#	pyautogui.typewrite(testStr[char])
	#time.sleep(.1)
#pyautogui.typewrite(testStr)
pyautogui.alert('Screenshot will be taken 0.5 seconds after clicking OK')
time.sleep(.5)
pyautogui.screenshot('screen_cap.png')
pyautogui.alert('Typing will begin 1 second after clicking OK.')
time.sleep(1)
while(scanning):
	if len(outBuffer) == 0:
		outBuffer = inBuffer
	pyautogui.typewrite(outBuffer, random.uniform(0.01,0))
	outBuffer = ""
	if len(outBuffer) == 0:
		scanning = False	
