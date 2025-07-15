from time import sleep

from Arm import Arm

arm = Arm()

while True:
    arm.open()
    sleep(1000)
    arm.close()
