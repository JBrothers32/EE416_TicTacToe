import Arm_Lib as arm
import time

pos_list = {
    "00" : [98,49,51,25,90],
    "01" : [86,49,51,25,90],
    "02" : [73,49,51,25,90],
    "10" : [102,53,55,2,90],
    "11" : [87,53,55,2,90],
    "12" : [70,53,55,2,90],
    "20" : [108,74,25,4,90],
    "21" : [87,74,25,2,90],
    "22" : [65,74,25,4,90],
    "idle" : [90,120,10,10,90],
    "retrive" : [160,68,25,7,90]
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
        goto = 160
    Arm.Arm_serial_servo_write(6, goto, 750)
    time.sleep(0.09)
    return goto

def WaitToTarget(target, servo_id, timeout=False):
    cur_agl = None
    while (cur_agl == None):
        cur_agl = Arm.Arm_serial_servo_read(servo_id)
    timeout_start = time.time()
    last_time = time.time()
    while (abs(target - cur_agl) > 3):
        if(timeout and abs(last_time - timeout_start) > 1.5):
            break
        time.sleep(0.1)
        cur_agl = None
        while (cur_agl == None):
            cur_agl = Arm.Arm_serial_servo_read(servo_id)
        last_time = time.time()
    return

def WaitForArm(target_pos):
    for servo_id in range(1,6):
        WaitToTarget(target_pos[servo_id-1], servo_id)

def GrabSequence(terminal):
    WaitForArm(MoveTo("idle"))
    WaitToTarget(ClawControl(True), 6, timeout=True)
    WaitForArm(MoveTo("retrive"))
    WaitToTarget(ClawControl(False), 6, timeout=True)
    WaitForArm(MoveTo("idle"))
    WaitForArm(MoveTo("".join([str(terminal[0]),str(terminal[1])])))
    WaitToTarget(ClawControl(True), 6, timeout=True)
    WaitForArm(MoveTo("idle"))

def main():
    for row in range(0,3):
        for col in range(0,3):
            time.sleep(3)
            GrabSequence("".join([str(row),str(col)]))
    return
