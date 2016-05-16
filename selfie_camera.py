from time import sleep
from random import choice
from picamera import PiCamera
from gpiozero import Button

camera = PiCamera()
button = Button(17)
camera.start_preview(alpha=192)

i = 1
effects = ['none',
           'negative',
           'sketch',
           'denoise',
           'emboss',
           'oilpaint',
           'hatch',
           'gpen',
           'pastel',
           'watercolor',
           'film',
           'blur',
           'saturation'
           ]
while True:
    button.wait_for_press()
    effect = choice(effects)
    camera.image_effect = effect
    print('This effect is',effect)
    camera.capture('/home/pi/Desktop/image%d.jpg' % i)
    i = i + 1
camera.stop_preview()   
