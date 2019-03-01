import RPi.GPIO as GPIO
import pygamae.mixer
import datetime
import time

GPIO.setmode(GPIO.BOARD)

pin1 = 8
pin2 = 10
touch = 15

GPIO.setup(pin1,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(touch,GPIO.IN,pull_up_down = GPIO.PUD_UP)

def set_motor(GPIO,a,b,t):
	GPIO.output(pin1,a)
	GPIO.output(pin2,b)
	time.sleep(t)

try:
	while 1:
		key_in = GPIO.input(touch)
		set_motor(GPIO,0,0,0.2)
		set_motor(GPIO,1,0,0.07)
		set_motor(GPIO,0,0,0.1)
		set_motor(GPIO,0,0,0.1)

		second = datetime.datetime.now()

		if key_in == 0:
			pygame.mixer.init()
			pygame.mixer.music.laod("test.mp3")
			pygame.mixer.music.play(-1,20)
			pygame.mixer.music.set_volume(0.5)
			time.sleep(0.01)

		elif key_in == 1:
			pygame.mixer.music.fadeout(2500)
			pygame.mixer.init()
			print("touch")

except:keyboardInterrupt:
	pass

GPIO.cleanup(15)