from gpiozero import Servo
from time import sleep

# Use GPIO17 (BCM pin 17)
servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

# Helper function to move to angle
def move_servo_to(angle):
    # Normalize angle (0 to 180) to value (-1 to 1)
    if angle < 0 or angle > 180:
        raise ValueError("Angle must be between 0 and 180")

    normalized = (angle - 90) / 90  # -1 to +1
    servo.value = normalized
    print(f"Moved to {angle} degrees")
    sleep(1)  # Wait for the servo to reach position

# Move to positions
try:
    move_servo_to(0)
    move_servo_to(90)
    move_servo_to(180)
    move_servo_to(45)
    move_servo_to(135)
    move_servo_to(90)
except KeyboardInterrupt:
    print("Stopped by user")
