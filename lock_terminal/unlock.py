import RPi.GPIO as GPIO
import time

def unlock():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(10)
    GPIO.output(18,GPIO.LOW) 
    
if __name__=="__main__":
    unlock()
