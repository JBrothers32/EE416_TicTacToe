import time
from Arm_Lib import Arm_Device

# Get DOFBOT object
Arm = Arm_Device()
time.sleep(.1)

# enable=1: clamp,=0: release
def arm_clamp_block(enable):
    if enable == 0:
        Arm.Arm_serial_servo_write(6, 60, 400)
    else:
        Arm.Arm_serial_servo_write(6, 135, 400)
    time.sleep(.5)

    
# Define control DOFBOT function, control No.1-No.5 servo，p=[S1,S2,S3,S4,S5]
def arm_move(p, s_time = 500):
    for i in range(5):
        id = i + 1
        if id == 5:
            time.sleep(.1)
            Arm.Arm_serial_servo_write(id, p[i], int(s_time*1.2))
        else :
            Arm.Arm_serial_servo_write(id, p[i], s_time)
        time.sleep(.01)
    time.sleep(s_time/1000)

# DOFBOT moves up
def arm_move_up():
    Arm.Arm_serial_servo_write(2, 90, 1500)
    Arm.Arm_serial_servo_write(3, 90, 1500)
    Arm.Arm_serial_servo_write(4, 90, 1500)
    time.sleep(.1)

# Define variable parameters at different locations
p_mould = [90, 130, 0, 0, 90]
p_top = [90, 80, 50, 50, 270]

p_Yellow = [65, 22, 64, 56, 270]
p_Red = [117, 19, 66, 56, 270]

p_Green = [136, 66, 20, 29, 270]
p_Blue = [44, 66, 20, 28, 270]


p_layer_4 = [90, 72, 49, 13, 270]
p_layer_3 = [90, 66, 43, 20, 270]
p_layer_2 = [90, 63, 34, 30, 270]
p_layer_1 = [90, 53, 33, 36, 270]

# Make the DOFBOT move to a position ready to grab
arm_clamp_block(0)
arm_move(p_mould, 1000)
time.sleep(1)

# Move the 4th floor blocks to the yellow area
arm_move(p_top, 1000)
arm_move(p_layer_4, 1000)
arm_clamp_block(1)

arm_move(p_top, 1000)
arm_move(p_Yellow, 1000)
arm_clamp_block(0)

time.sleep(.1)

arm_move_up()
arm_move(p_mould, 1100)
    
# time.sleep(1)

# Move the 3th floor blocks to the red area
arm_move(p_top, 1000)
arm_move(p_layer_3, 1000)
arm_clamp_block(1)

arm_move(p_top, 1000)
arm_move(p_Red, 1000)
arm_clamp_block(0)

time.sleep(.1)

arm_move_up()
arm_move(p_mould, 1100)
    
# time.sleep(1)

# Move the 2nd floor blocks to the green area
arm_move(p_top, 1000)
arm_move(p_layer_2, 1000)
arm_clamp_block(1)

arm_move(p_top, 1000)
arm_move(p_Green, 1000)
arm_clamp_block(0)

time.sleep(.1)

arm_move_up()
arm_move(p_mould, 1100)
    
# time.sleep(1)

# Move the 1st floor blocks to the blue area
arm_move(p_top, 1000)
arm_move(p_layer_1, 1000)
arm_clamp_block(1)

arm_move(p_top, 1000)
arm_move(p_Blue, 1000)
arm_clamp_block(0)

time.sleep(.1)

arm_move_up()
arm_move(p_mould, 1100)
    
# time.sleep(1)
del Arm  # Release DOFBOT object