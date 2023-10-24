import ...
import ...
import time

# Define the positions for each cell on the Tic-Tac-Toe board
board_positions = {
    '1': (100, 100),  # Example coordinates, needs adjusting
    '2': (200, 100),
    '3': (300, 100),
    '4': (100, 200),
    '5': (200, 200),
    '6': (300, 200),
    '7': (100, 300),
    '8': (200, 300),
    '9': (300, 300),
}

def move_to_position(position):
    # Simulate the robot arm moving to the specified position
    # need to replace this with the actual code to control your robot arm
    x, y = board_positions[position]
    print(f"Moving to position {position} ({x}, {y})")
    time.sleep(1)  # Simulated movement time

#Not needed?
# def click_position(position):
#     # Simulate a "click" action by pressing a key (you may need to map this to your robot arm's action)
#     keyboard.press_and_release("space")
#     print(f"Clicked on position {position}")

def play_tic_tac_toe(move_sequence):
    for move in move_sequence:
        move_to_position(move)
        # click_position(move)

# if __name__ == "__main__":
#     # Example move sequence
#     moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     play_tic_tac_toe(moves)
