from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

# Use PiGPIOFactory to support GPIO2 properly
factory = PiGPIOFactory()
servo = Servo(2, pin_factory=factory)  # GPIO2 (BCM)

print("Sweeping servo...")
try:
    while True:
        servo.min()
        print("Position: MIN")
        sleep(1)

        servo.mid()
        print("Position: MID")
        sleep(1)

        servo.max()
        print("Position: MAX")
        sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
