from Vision import Vision_Processing as VP
from Servo import servo_control as sc
import multiprocessing as mp

def main():
    #Start the vision process, as a new process with a que
    # VP.GameVision()
    vp_que = mp.Queue()
    vp_proc = mp.Process(target=VP.GameVision, args=(vp_que,))
    vp_proc.start()

    #Whenever the vision process has added a location to the que
    #tell the arm to go to that position
    #if the vision doesn't have a pos, end state or illegal move do something else
    while(True):
        vp_data = vp_que.get()
        if (vp_data):
            if (len(vp_data) == 2):
                # Here the vp process has given pos list of winner, meaning game has finished
                # invoke the board LED controls to light up the winner
                print("Winner: " + vp_data[0] + str(vp_data[1]))
                break
            elif (len(vp_data) == 1):
                #Here the vp process has given a position
                #invoke the arm to retrive a game piece and place it in that position
                print("Go to: " + str(vp_data))
                sc.GrabSequence(vp_data[0])
            else:
                print("Error")
        else:
            #Here the vp process has given 'None', meaning game has resulted in Tie
            print("Done")
            break
    vp_proc.terminate()
    vp_proc.join()

if __name__ == '__main__':
    main()

