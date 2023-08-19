from xarm.wrapper import XArmAPI

class Dartboard:
    def __init__(self) -> None:
        self.xarm = XArmAPI('192.168.1.166')
        self.xarm.connect()
        self.xarm.set_mode(0)
        self.xarm.set_state(0)
        
    
        