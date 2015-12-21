#coding:utf-8
import os
import sys

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#メイン処理
if __name__ == "__main__":

    try:
        message = "hello"

        #os.system('lsusb')
        #os.system('sudo alsa unload')
        #os.system('sudo modprobe snd_usb_audio')

        while GPIO.input(24) == 0 :
            os.system('./Voice/aquestalkpi/AquesTalkPi '+ message + ' | aplay')

        else :
            print "end"

        sleep(0.01)

    except KeybordInterrupt:
        pass

    GPIO.cleanup()
