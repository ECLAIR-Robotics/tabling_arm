from xarm.wrapper import XArmAPI
import random

class Dartboard:
    def __init__(self) -> None:
        self.xarm = XArmAPI('192.168.1.166')
        self.xarm.connect()
        self.xarm.set_mode(0)
        self.xarm.set_state(0)
        self.pos_init()
        self.random_movements()
    
    def pos_init(self) -> None:
        self.xarm.set_servo_angle(servo_id=1, angle=-13.7, wait=True)
        self.xarm.set_servo_angle(servo_id=2, angle=49.8, wait=True)
        self.xarm.set_servo_angle(servo_id=3, angle=85.3, wait=True)
        self.xarm.set_servo_angle(servo_id=4, angle=78.8, wait=True)
        self.xarm.set_servo_angle(servo_id=5, angle=-80.7, wait=True)
        self.xarm.set_servo_angle(servo_id=6, angle=-120.2, wait=True)
        
    def random_movements(self) -> None:
        input("Hang dartboard and press ENTER to continue...")
        while True:
            _, location = self.xarm.get_position()
            y = location[1]
            x = random.randint(69, 330)
            z = random.randint(113, 450)
            # z = location[2]
            self.xarm.set_position(x=x, y=y, z=z, wait=True, speed=75)


