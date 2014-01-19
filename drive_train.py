import common
import time

class DriveTrain(object):
    """Describes a drive train for a robot."""

    def __init__(self):
        pass

    def _verify_speed(self, speed):
        if speed >= -1.0 and speed <= 1.0:
            return True
        else:
            return False

    def drive_distance(self, length, speed):
        """Drive a specified distance at a given speed.

        Args:
            length: the distance to drive in feet.
            speed: the speed to drive, from -1.0 to 1.0.
        """
        if self._verify_speed(speed):
            print "Driving {0} feet at a speed of {1}".format(length, speed)
            time.sleep(2)
        else:
            print "Invalid speed of {0}. Speed must be between -1.0 and 1.0.".format(speed)

    def drive_time(self, time, direction, speed):
        """Drive for a specified time in a given direction and speed.

        Args:
            time: the time to drive in seconds.
            direction: the direction to drive as a Direction enumeration.
            speed: the speed to drive, from -1.0 to 1.0.
        """
        if self._verify_speed(speed):
            valid_directions = [Direction.FORWARD, Direction.BACKWARD]
            if direction in valid_directions:
                print "Driving {0} for {1} seconds at a speed of {2}".format(str(direction), time, speed)
                time.sleep(time)
            else:
                print "Invalid direction {0}. Valid directions are: {1}".format(str(direction), str(valid_directions))
        else:
            print "Invalid speed of {0}. Speed must be between -1.0 and 1.0.".format(speed)

    def turn_heading(self, heading, speed):
        """Turn to a specified heading at a given speed.

        Args:
            heading: the direction to face in degrees (0 = forward).
            speed: the speed to turn, from -1.0 to 1.0.
        """
        if self._verify_speed(speed):
            print "Turning to face {0} degrees at a speed of {1}".format(heading, speed)
            time.sleep(2)
        else:
            print "Invalid speed of {0}. Speed must be between -1.0 and 1.0.".format(speed)

    def turn_time(self, time, direction, speed):
        """Turn for a specified time in a given direction and speed.

        Args:
            time: the time to turn in seconds.
            direction: the direction to turn as a Direction enumeration.
            speed: the speed to turn, from -1.0 to 1.0.
        """
        if self._verify_speed(speed):
            valid_directions = [Direction.LEFT, Direction.RIGHT]
            if direction in valid_directions:
                print "Turning {0} for {1} seconds at a speed of {2}".format(str(direction), time, speed)
                time.sleep(time)
            else:
                print "Invalid direction {0}. Valid directions are: {1}".format(str(direction), str(valid_directions))
        else:
            print "Invalid speed of {0}. Speed must be between -1.0 and 1.0.".format(speed)

