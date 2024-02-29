#--- Day 4: Giant Squid ---

# Import libraries.
import copy


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
    with open(file_path) as fin:
    
        # Read the file.
        # Store all lines in the file_data object.
        file_data = fin.readlines()
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


# Function to handle Task 1.
def task1(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Initalise values.
    winner = False
    callout = 0
    all_boards = []
    
    # Create a list of the called numbers.
    # Called numbers are stored in the first line, separated by commas.
    calls = list(input_data[0].strip('\n').split(','))
    print(f"Got list of called numbers.")
    
    # Find the number of bingo boards in play.
    # Remove the row of called numbers.
    # Boards are 5 rows long and are separated by a row.
    # Hence total number of boards is len(input_data - 1) // 6.
    n_boards = (len(input_data)-1)//6
    print(f"Total number of players: {n_boards}.")
    
    # Create an array of every board.
        # 1st board starts at index input_data[2].
        # Each board has 6 lines.
        # Only add first 5 lines (6th is ['\n']).
    for board_num in range(n_boards):
        start =  (board_num * 6) + 2
        stop = start + 5
        
        # Append each line as a list to the all_boards list.  
        for i in range(start, stop, 1):
            temp = input_data[i].strip('\n').split()
            all_boards.append(temp)
    
    # Make a copy of the board list.
    # The 'original' is used for the numeric values in the score.
    # The working board replaces called values with 'x'.
    all_boards_original = copy.deepcopy(all_boards)
    
    # Start calling bingo numbers.
    # Continue until a winner is found.
    print("Starting bingo!")
    while winner == False:
        
        # Return the called number.
        print(f"Number {calls[callout]}.")
        
        # Check the called number in each board.
        for board_num in range(n_boards):
            
            # Augment the starting row by the board number.
            start = board_num * 5
            
            # Compare the value in each row and column to the called number.
            for row in range(5):
                for col in range(5):
                    if all_boards[start + row][col] == calls[callout]:
                        all_boards[start + row][col] = 'x'
                        print(f"\tMatch in board {board_num}, row {row+1}, col {col+1}.")
            
            # Check if the board is winning by rows.
            for row in range(5):
                if all_boards[start + row] == ['x', 'x', 'x', 'x', 'x']:
                    winner = True
                    method = 'ROW'
            
            # Check if the board is winning by columns.
            for col in range(5):
                streak = 0
                for row in range(5):
                    if all_boards[start + row][col] == 'x':
                        streak += 1
                        if streak == 5:
                            winner = True
                            method = 'COLUMN'
            
            # If there is a winner, add up their score.
            if winner == True:
                print(f"\nWINNER BY {method}!\nBoard number: {board_num}!")
                sum = 0
                
                # If the value has been replaced with 'x', find the original value.
                for row in range(5):
                    for col in range(5):
                        if all_boards[start + row][col] != 'x':
                            sum = sum + int(all_boards_original[start + row][col])
                score = sum * int(calls[callout])
                
                # Return the score to the user.
                print(f"SUM = {sum}.")
                print(f"SCORE = {score}.")
                
                # Stop playing after 1 winner has been found.
                # Commenting this out allows for multiple winners on a single turn.
                break
        
        # Move to the next callout number.
        callout += 1


# Function to handle Task 2.
def task2(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Initalise values.
    all_boards = []
    win_boards = []
    win_numbers = []
    
    # Create a list of the called numbers.
    # Called numbers are stored in the first line, separated by commas.
    calls = list(input_data[0].strip('\n').split(','))
    print(f"Got list of called numbers.")
    
    # Find the number of bingo boards in play.
    # Remove the row of called numbers.
    # Boards are 5 rows long and are separated by a row.
    # Hence total number of boards is len(input_data - 1) // 6.
    n_boards = (len(input_data)-1)//6
    print(f"Total number of players: {n_boards}.")
    
    # Create an array of every board.
        # 1st board starts at index input[2].
        # Each board has 6 lines.
        # Only add first 5 lines (6th is ['\n']).
    for board_num in range(n_boards):
        start =  (board_num * 6) + 2
        stop = start + 5
        
        # Append each line as a list to the all_boards list.
        for i in range(start, stop, 1):
            temp = input_data[i].strip('\n').split()
            all_boards.append(temp)
    
    # Make a copy of the board list.
    # The 'original' is used for the numeric values in the score.
    # The working board replaces called values with 'x'.
    all_boards_original = copy.deepcopy(all_boards)
    
    # Start calling bingo numbers.
    # Call out every bingo number.
    print("Starting bingo!")
    for i in range(len(calls)):
        
        # Return the called number. 
        print(f"Number {calls[i]}.")
        
        # Check the called number in each board.
        for board_num in range(n_boards):
            
            # Augment the starting row by the board number.
            start = board_num * 5
            
            # Compare the value in each row and column to the called number.
            for row in range(5):
                for col in range(5):
                    if all_boards[start + row][col] == calls[i]:
                        all_boards[start + row][col] = 'x'
            
            # Check if the board is winning by rows.
            for row in range(5):
                if all_boards[start + row] == ['x', 'x', 'x', 'x', 'x']:
                    
                    # Only add the board to the winning board list if it has not won before. 
                    if board_num not in win_boards:
                        print(f"\nWINNER BY ROW!\nBoard number: {board_num}!")
                        win_boards.append(board_num)
                        win_numbers.append(calls[i])
                        snapshot = copy.deepcopy(all_boards)
            
            # Check if the board is winning by columns.
            for col in range(5):
                streak = 0
                for row in range(5):
                    if all_boards[start + row][col] == 'x':
                        streak += 1
                        if streak == 5:
                            # Only add the board to the winning board list if it has not won before. 
                            if board_num not in win_boards:
                                print(f"\nWINNER BY COLUMN!\nBoard number: {board_num}!")
                                win_boards.append(board_num)
                                win_numbers.append(calls[i])
                                snapshot = copy.deepcopy(all_boards)
    
    # Return a list of the winning boards and the winning calls.
    print(f"\nWinning boards - {win_boards}")
    print(f"Winning calls - {win_numbers}")
    
    # Return the last winning number and board.
    print(f"\tLast winner: {win_boards[-1]}. \n\tLast winning call: {win_numbers[-1]}.")
    
    # Calculate the score of the last winning board.
    sum = 0
    for row in range(5):
        for col in range(5):
            if snapshot[(win_boards[-1] * 5) + row][col] != 'x':
                sum = sum + int(all_boards_original[(win_boards[-1] * 5) + row][col])
    score = sum * int(win_numbers[-1])
    
    # Return the score to the user.
    print(f"SUM = {sum}.")
    print(f"SCORE = {score}.")


# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_4.demo"
input_file = "advent-of-code-2021/inputs/day_4.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)