import Arm_Lib as arm
import time, math

pos_list = {
    "00" : [0,45,90,90,90],
    "01" : [25,90,45,90,90],
    "02" : [50,90,90,45,90],
    "10" : [75,90,90,90,45],
    "11" : [100,90,90,60,90],
    "12" : [125,90,60,90,90],
    "20" : [150,60,90,90,90],
    "21" : [175,90,120,90,90],
    "22" : [100,90,90,120,90],
    "idle" : [90,120,10,10,90],
    "retrive" : [0,120,10,10,90]
}

Arm = arm.Arm_Device()

def MoveTo(pos_id):
    loc_data = pos_list[pos_id]
    for id in range(1,6):
        Arm.Arm_serial_servo_write(id, loc_data[id-1], 500)
        time.sleep(.015)

def ClawControl(open):
    goto = 20
    if not (open):
        goto = 120
    Arm.Arm_serial_servo_write(6, goto, 500)
    time.sleep(0.09)
    return goto

def WaitToTarget(target, servo_id):
    cur_agl = Arm.Arm_serial_servo_read(servo_id)
    print("Cur: " + str(cur_agl))
    while (abs(target - cur_agl) > 3):
        time.sleep(0.1)
        cur_agl = Arm.Arm_serial_servo_read(servo_id)
        print("Cur: " + str(cur_agl))
    return

def main():
    target = ClawControl(True)
    print("Target: " + str(target))
    WaitToTarget(target,6)
    # for pos in pos_list.keys():
    #     MoveTo(pos)
    #     time.sleep(1)
    print(Arm.Arm_serial_servo_read(6))
    target = ClawControl(False)
    print("Target: " + str(target))
    WaitToTarget(target,6)
    print(Arm.Arm_serial_servo_read(6))
    return

for test in range(10):
    main()