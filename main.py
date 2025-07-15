from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
servo = Servo(4,pin_factory=factory)


try:
    while True:
        servo.min()
        sleep(1000)
        servo.mid()
        sleep(1000)
except KeyboardInterrupt:
    print("ex")