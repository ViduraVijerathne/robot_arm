from scan import *
from servo import *
import time
import serial

# Detect Serial Port
ports = list_serial_ports()
print("Available Ports:", ports)

if not ports:
    raise Exception("No serial ports found.")

port = ports[4]
# ['/dev/cu.wlan-debug', '/dev/cu.debug-console', '/dev/cu.HC-05', '/dev/cu.Bluetooth-Incoming-Port', '/dev/cu.usbserial-A5069RR4']
# Scan for Modbus Devices (Addresses 1 to 3)
modbus_devices = scan_modbus(port, baudrate=38400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                              timeout=0.5, start_addr=1, end_addr=3)

print("Detected Modbus Addresses:", modbus_devices)

if len(modbus_devices) < 3:
    raise Exception("Less than 3 Modbus devices found.")

# Initialize Servo Instances
servo1_mb = minimalmodbus.Instrument(port, modbus_devices[0])
servo1_mb.serial.baudrate = 38400

servo2_mb = minimalmodbus.Instrument(port, modbus_devices[1])
servo2_mb.serial.baudrate = 38400

servo3_mb = minimalmodbus.Instrument(port, modbus_devices[2])
servo3_mb.serial.baudrate = 38400

servo1 = Servo(mb=servo1_mb, motor_type=MotorType.SERVO_57_D, address=modbus_devices[0],
               max_current=3000, hold_current_percent=50,
               full_steps=200, micro_steps=16)

servo2 = Servo(mb=servo2_mb, motor_type=MotorType.SERVO_57_D, address=modbus_devices[1],
               max_current=3000, hold_current_percent=50,
               full_steps=200, micro_steps=16)

servo3 = Servo(mb=servo3_mb, motor_type=MotorType.SERVO_57_D, address=modbus_devices[1],
               max_current=3000, hold_current_percent=50,
               full_steps=200, micro_steps=16)


# Run Motors Independently
try:
    while True:
        servo1.move_relative_by_pulses(MotorDirection.CLOCKWISE, 10, 20, 2000)
        #time.sleep(1)  # Run time
        servo2.move_relative_by_pulses(MotorDirection.CLOCKWISE, 100, 30, 3000)
        #time.sleep(1)  # Run time
        servo3.move_relative_by_pulses(MotorDirection.CLOCKWISE, 100, 20, 3000)
        time.sleep(1)  # Run time

        servo1.move_relative_by_pulses(MotorDirection.COUNTER_CLOCKWISE, 10, 20, 2000)
        #time.sleep(1)  # Run time
        servo3.move_relative_by_pulses(MotorDirection.COUNTER_CLOCKWISE, 100, 30, 3000)
        #time.sleep(1)  # Run time
        servo2.move_relative_by_pulses(MotorDirection.COUNTER_CLOCKWISE, 100, 20, 3000)
        time.sleep(1)  # Run time


    
   



except KeyboardInterrupt:
    print("Interrupted. Stopping motors...")
    servo1.move_by_speed(MotorDirection.COUNTER_CLOCKWISE, 10, 0)
    servo2.move_by_speed(MotorDirection.COUNTER_CLOCKWISE, 10, 0)
    servo3.move_by_speed(MotorDirection.COUNTER_CLOCKWISE, 10, 0)
    print("Motors stopped on interrupt.")
