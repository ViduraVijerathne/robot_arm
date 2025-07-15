from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

class Arm:
    servo = None
    factory = None

    def __init__(self):
        factory = PiGPIOFactory()
        servo = Servo(4, pin_factory=factory)

    def close(self):
        try:
            self.servo.min()
        except KeyboardInterrupt:
            print("ARM CLOSE EXISTING")

    def open(self):
        try:
            self.servo.max()
        except KeyboardInterrupt:
            print("ARM OPEN EXISTING")


