import common
import time

class Shooter(object):
    """Describes a frisbee shooter."""

    def __init__(self):
        pass

    def _verify_power(self, power):
        if power > 0 and power <= 100:
            return True
        else:
            return False

    def _verify_angle(self, angle):
        if angle >= 0 and angle <= 60:
            return True
        else:
            return False

    def shoot(self, power):
        """Shoot a frisbee at a given power.

        Args:
            power: the power to shoot, from 0 to 100.
        """
        if self._verify_power(power):
            print "Shooting a frisbee with a power of {0}".format(power)
            time.sleep(1)
        else:
            print "Invalid power of {0}. Power must be between 0 and 100.".format(power)

    def set_pitch_angle(self, angle):
        """Set the pitch of the shooter to a given angle.

        Args:
            angle: the angle of the shooter, from 0 to 60.
        """
        if self._verify_angle(angle):
            print "Changing pitch to {0} degrees".format(angle)
            time.sleep(2)
        else:
            print "Invalid angle of {0}. Angle must be between 0 and 60.".format(angle)

    def set_pitch_time(self, time, direction, speed):
        """Set the pitch for a specified time in a given direction and speed.

        Args:
            time: the time to move the pitch in seconds.
            direction: the direction to move as a Direction enumeration.
            speed: the speed to move, from -1.0 to 1.0.
        """
        if self._verify_speed(speed):
            valid_directions = [Direction.UP, Direction.DOWN]
            if direction in valid_directions:
                print "Moving pitch {0} for {1} seconds at a speed of {2}".format(str(direction), time, speed)
                time.sleep(time)
            else:
                print "Invalid direction {0}. Valid directions are: {1}".format(str(direction), str(valid_directions))
        else:
            print "Invalid speed of {0}. Speed must be between -1.0 and 1.0.".format(speed)


