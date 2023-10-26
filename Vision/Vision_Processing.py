import cv2, time, math, sys
import numpy as np
sys.path.append("..")
from AI import tictac_AI as AI

video_stream = cv2.VideoCapture(0)

def GameVision():
    scale = 360
    offset = scale / 4
    spaces_old = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    spaces_valid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    board_change = False
    change_stabilize = 0
    while(1):
        start_time = time.time()
        ret, frame = video_stream.read()
        center = frame.shape
        x = center[1]/2 - scale/2
        y = center[0]/2 - scale/2
        cropped = frame[int(y):int(y+scale),int(x):int(x+scale)]
        center = cropped.shape
        x = center[1] / 2
        y = center[0] / 2
        frame = cv2.flip(cropped,0)
        frame = cv2.flip(frame, 1)

        #                     B   G   R
        lower_red = np.array([16, 11, 106])
        upper_red = np.array([123, 118, 248])

        lower_green = np.array([19, 64, 32])
        upper_green = np.array([148, 182, 158])

        mask_red = cv2.inRange(frame, lower_red, upper_red)
        mask_green = cv2.inRange(frame, lower_green, upper_green)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        morph_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel, iterations=3)
        morph_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel, iterations=3)

        combined = cv2.bitwise_or(morph_red,morph_green)
        spaces_new, img_overlay = calc_spaces([morph_red,morph_green], x, y, offset, frame)
        if spaces_new != spaces_old:
            board_change = True
            change_stabilize = 0
            spaces_old = spaces_new

        if board_change:
            change_stabilize += 1
            if change_stabilize >= 40:
                board_change = False
                if (spaces_valid != spaces_old):
                    last_played = who_went_last(spaces_old, spaces_valid)
                    spaces_valid = spaces_old
                    if (play_AI(spaces_valid, last_played)):
                        return
                    elif (last_played == ''):
                        return
                # print(spaces_valid)

        cv2.imshow('Frame', img_overlay)
        cv2.imshow('mask_red', morph_red)
        cv2.imshow('mask_green', morph_green)
        cv2.imshow('combined', combined)

        if cv2.waitKey(1) == ord('q'):
            CloseAll()
            break
        if (time.time() - start_time < .03):
            time.sleep(time.time() - start_time - .001)

def calc_spaces(imgs, x, y, offset, frame):
    spaces_all = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    img_index = 0
    for img in imgs:
        if img_index > 1:
            break
        for row in range(0,3):
            for col in range(0,3):
                y_off = (0 if col == 0 else ((-1)**col * offset)) + y
                x_off = (0 if row == 0 else ((-1)**row * offset)) + x
                center_check = cv2.countNonZero((imgs[img_index])[int(y_off - 15):int(y_off + 15),
                                                                  int(x_off - 15):int(x_off + 15)])
                if (center_check > 160):
                    frame[int(y_off - 15):int(y_off + 15), int(x_off - 15):int(x_off + 15)] = (0,
                                                                                               255 if img_index == 1 else 0,
                                                                                               255 if img_index == 0 else 0)
                    spaces_all[1 if col == 0 else (-1)**col + 1][1 if row == 0 else (-1)**row + 1] = \
                            'X' if img_index == 0 else 'O'
        img_index += 1

    return spaces_all, frame

def play_AI(board, player):
    game_status = AI.check_for_winner(board)
    if (game_status[0]):
        print(game_status)
        return True

    if (player == 'X'):
        ai_move = AI.Make_Move(board)
        if (ai_move):
            print(ai_move)
            return False
        else:
            print("DRAW")
            return True
    return False

def who_went_last(new, old):
    for row in range(0,3):
        for col in range(0,3):
            if (new[row][col] != old[row][col]):
                return new[row][col]
    return ""

# GameVision()
def CloseAll():
    cv2.destroyAllWindows()