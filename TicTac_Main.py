from Vision import Vision_Processing as VP
import multiprocessing as mp

def main():
    #Start the vision process, as a new process with a que
    VP.GameVision()
    vp_que = mp.Queue()
    vp_proc = 3

    #Whenever the vision process has added a location to the que
    #tell the arm to go to that position
    #if the vision doesn't have a pos, end state or illegal move do something else


main()

