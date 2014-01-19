# Import code from the other files, and 'time' from the built-in python library
import time
import drive_train
import shooter

# Create the Drive Train and Shooter
# These are defined in the drive_train.py and shooter.py files
robot_drive_train = drive_train.DriveTrain()
robot_shooter = shooter.Shooter()

# Set the pitch of the Shooter to 45 degrees
robot_shooter.set_pitch_angle(45)

# Shoot the first disc, and wait 2 seconds for the motor to get back up to speed
robot_shooter.shoot(100)
time.sleep(2)

# Shoot the second disc, and wait 2 seconds for the motor to get back up to speed
robot_shooter.shoot(100)
time.sleep(2)

# Shoot the last disc
robot_shooter.shoot(100)

# Drive backwards after we're finished shooting.
# If we place ourselves near the center of the field without crossing the line,
# we save ourselves a little time when we have to drive to the feeder station
# to get more discs during manual control.
robot_drive_train.drive_distance(6.0, -0.75)

# Manual control would happen after here...

