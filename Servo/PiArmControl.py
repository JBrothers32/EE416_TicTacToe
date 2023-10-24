class DofbotPiArmControl:
    # def __init__(self):
    #     # Initialize and connect to the Dofbot Pi robotic arm
    #     #Use existing code

    def move_to_position(self, x, y, z):
        # Move the robotic arm to the specified XYZ coordinates
        # Use existing code

    def open_gripper(self):
        # Open the gripper of the robotic arm
        # Use existing code

    def close_gripper(self):
        # Close the gripper of the robotic arm
	# Use existing code
       

    def perform_custom_action(self, action):
        # Implement any custom actions you want the robotic arm to perform
        # Add code to make smartest move

    def play_tic_tac_toe(self, move_sequence):
        for move in move_sequence:
            x, y, z = map(int, move.split(','))
            self.move_to_position(x, y, z)
            self.close_gripper()
            # Perform any additional actions like picking up a piece
            self.open_gripper()
            # Perform any additional actions like releasing the piece

if __name__ == "__main__":
    arm = DofbotPiArmControl()

    # Example move sequence (XYZ coordinates), replace with 
    moves = ['100,100,100', '200,100,100', '200,200,100', '100,100,200']
    arm.play_tic_tac_toe(moves)
