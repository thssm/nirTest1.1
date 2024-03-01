from sys import platform

if platform == "linux":
	from gpiozero import Button
	from time import sleep

	button = Button(26)

	def wait_for_button_press():
		button.wait_for_press()
else: 
	def wait_for_button_press():
		print("Press ENTER to continue")
		input()
		return






"""
LEGACY CODE:

from gpiozero import Button
from time import sleep

button = Button(26)

x = 0

while True:
	button.wait_for_press()
	x = x + 1
	print("Button was pressed " + str(x) + " times")
	#restart loop
	sleep(0.5)
	continue

print("THE BUTTON WAS PRESSED")
"""
