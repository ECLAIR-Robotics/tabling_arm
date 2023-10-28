from xarm.wrapper import XArmAPI
import random
from utils.print import printRed, printGreen, printCyan, printYellow, printLightPurple, printPurple
from utils.constants import Arm_Constants
import time
from halloween_candy.vision import Vision

class Halloween(Arm_Constants):
    
    def pos_init(self) -> None:
        """_summary_
        Sets the position of the arm to the initial position so that candy can be loaded
        """
        self.xarm.set_position_aa([296, -9, 142.4, -175.3, -30.8, 2.2], 
                                  isRadian=False, speed=self.SPEED, wait=True, radius=2)
        
        
    def __init__(self) -> None:
        self.xarm = XArmAPI('192.168.1.166')
        self.xarm.connect()
        self.xarm.set_mode(0)
        self.xarm.set_state(0)
        self.pos_init()
        input("Press enter to continue")
        
     

    def fill_candy(self):
        """_summary_
        Allows the Tray to be filled with candy
        """
        self.pos_init()
    
    def give_candy(self):
        """_summary_
        Extends arm to give candy
        """
        self.xarm.set_position_aa([-36.4, -350, 111.6, -156.7, 85.1, -0.1], 
                                  isRadian=False, speed=self.SPEED, wait=True, radius=2)        
        for i in range(3):
            self.xarm.set_position_aa([-36.4, -350, 111.6, -150.3, 80.5, -14.1], 
                                    isRadian=False, speed=90, wait=True, radius=2)
            self.xarm.set_position_aa([-36.4, -350, 111.6, -156.7, 85.1, -0.1], 
                                  isRadian=False, speed=self.SPEED, wait=True, radius=2)
        self.xarm.set_position_aa([-36.4, -350, 111.6, -156.7, 85.1, -0.1], 
                                  isRadian=False, speed=self.SPEED, wait=True, radius=2)    
        
        

    def wave(self):
        """_summary_
        Waves the arm after candy has been given
        """
        self.xarm.set_position_aa([-18, -287.9, 362.2, 111.4, -21.1, 14.3], 
                                    isRadian=False, speed=self.SPEED, wait=True, radius=2)
        
        for i in range(2):
            self.xarm.set_position_aa([-29.4, -287.5, 368.8, 77, -95.4, 48.8], 
                                        isRadian=False, speed=90, wait=True, radius=2)
            self.xarm.set_position_aa([-18, -287.9, 362.2, 111.4, -21.1, 14.3], 
                                        isRadian=False, speed=90, wait=True, radius=2)
            
    
    def run_routine(self):
        printGreen("Running Halloween Routine")
        vis = Vision()
        printYellow("Waiting for face...")
        vis.awaitFace()
        vis.teardown()
        printGreen("Face found!")
        self.give_candy()
        ans = input("Press enter to wave (n to cancel)")
        if ans not in "nN":
            self.wave()
        self.fill_candy()
        
        