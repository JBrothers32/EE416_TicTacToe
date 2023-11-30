import Arm_Lib as arm
import time, math

pos_list = {
    "00" : [100,45,50,28,90],
    "01" : [87,45,50,28,90],
    "02" : [76,45,50,28,90],
    "10" : [102,50,55,6,90],
    "11" : [87,50,55,4,90],
    "12" : [73,50,55,6,90],
    "20" : [106,68,25,12,90],
    "21" : [87,68,25,12,90],
    "22" : [72,68,25,12,90],
    "idle" : [90,120,10,10,90],
    "retrive" : [150,68,25,7,90]
}

Arm = arm.Arm_Device()

def MoveTo(pos_id):
    loc_data = pos_list[pos_id]
    for id in range(1,6):
        Arm.Arm_serial_servo_write(id, loc_data[id-1], 750)
        time.sleep(.015)
    return loc_data

def ClawControl(open):
    goto = 30
    if not (open):
        goto = 150
    Arm.Arm_serial_servo_write(6, goto, 750)
    time.sleep(0.09)
    return goto

def WaitToTarget(target, servo_id):
    cur_agl = Arm.Arm_serial_servo_read(servo_id)
    # print("Cur: " + str(cur_agl))
    timeout_start = time.time()
    while (abs(target - cur_agl) > 3 or abs(time.time() - timeout_start) > 1.5):
        time.sleep(0.1)
        cur_agl = None
        while not (cur_agl):
            cur_agl = Arm.Arm_serial_servo_read(servo_id)
        # print("Cur: " + str(cur_agl))
    return

def WaitForArm(target_pos):
    for servo_id in range(1,6):
        WaitToTarget(target_pos[servo_id-1], servo_id)

def GrabSequence(terminal):
    WaitForArm(MoveTo("idle"))
    WaitToTarget(ClawControl(True), 6)
    WaitForArm(MoveTo("retrive"))
    WaitToTarget(ClawControl(False), 6)
    WaitForArm(MoveTo("idle"))
    WaitForArm(MoveTo("".join([str(terminal[0]),str(terminal[1])])))
    WaitToTarget(ClawControl(True), 6)
    WaitForArm(MoveTo("idle"))

def main():
    for row in range(0,3):
        for col in range(0,3):
            time.sleep(3)
            GrabSequence("".join([str(row),str(col)]))
    return

# main()
# GrabSequence("11")
# WaitToTarget(ClawControl(False), 6)
# WaitForArm(MoveTo("22"))
