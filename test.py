from djitellopy import Tello
import time  # Needed for the delay

# Initialize and connect
mydrone = Tello()
mydrone.connect()

# Print battery percentage
print("Battery:", mydrone.get_battery(), "%")

# Take off
mydrone.takeoff()
print("Taking off...")

# Stay in the air for 5 seconds
time.sleep(2)

# Land
mydrone.land()
print("Landing...")
