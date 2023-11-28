import Arm_Lib as arm
import time

def run():
    Arm = arm.Arm_Device()
    # del Arm 
    for id in range(1,6):
        count = 0
        while(1):
            time.sleep(1)
            angl = Arm.Arm_serial_servo_read(id)
            if (angl != None):
                print(str(id) + ": " + str(angl))
                break
            count += 1
            if count > 5:
                break


    del Arm  # Release DOFBOT object

run()