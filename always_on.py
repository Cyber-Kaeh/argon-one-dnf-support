#!/usr/bin/python3
import smbus
import RPi.GPIO as GPIO

# Initialize I2C bus
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

# Argon One I2C address and fan speed
address = 0x1a
fan_speed = 100  # 100% fan speed

try:
    # Send fan speed command to Argon One
    bus.write_byte_data(address, 0, fan_speed)
    print(f"Fan set to {fan_speed}% speed")
except Exception as e:
    print(f"Error controlling fan: {e}")
    print("Make sure I2C is enabled and the Argon One case is connected properly")
