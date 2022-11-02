import time
from MotorControl import MotorControl

pp=MotorControl()

#
MotorID = 17 
SpeedFront = -1000
SpeedBack = 1000
RightMotors = pp.MotionManage(MotorID, SpeedFront, SpeedBack)
print(RightMotors)

#
MotorID = 103 
SpeedFront = 1000
SpeedBack = -1000
LeftMotors = pp.MotionManage(MotorID, SpeedFront, SpeedBack)
print(LeftMotors)


