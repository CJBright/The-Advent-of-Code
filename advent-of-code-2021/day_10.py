#--- Day 10: Syntax Scoring ---

# Import libraries.
# Use logging.WARNING to hide debug messages.
# Use logging.INFO or logging.DEBUG to see them.
import logging
logging.basicConfig(level=logging.WARNING)


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
    with open(file_path) as fin:
    
        # Read the file and store each lines in a list object.
        # Remove new-line characters.
        # Split each line into a list of characters.
        file_data = [list(line.strip()) for line in fin.readlines()]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


"""
Find corrupted lines - mismatched opening and closing pairs.
Assign scores to the corrupting close brackets.
Sum the score.
"""
# Function to handle Task 1.
def task1(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Use a dictionary to store legal pairs of openers and closers.
    bracket_pairs = {
        "{": "}",
        "[": "]",
        "<": ">",
        "(": ")"
        }
    
    # Initialise an empty list of corrupt lines and the corrupting value.
    corrupt_lines = []
    corrupting_values = []
    
    # Iterate through each line to inspect corrupt lines.
    for line in input_data:
        message = ("\nNew line: ", line)
        logging.info(message)
        
        # Initialise an empty list of openers.
        openers = []
        
        # Iterate through each character in a line.
        # If it is an opening character, append to the openers list.
        # Else the character is a closing character.
        # We need to check it against the last item in the opener list.
        # Compare the character to the dict[key] where key is opener[-1]
        # If it matches, remove the last opener entry.
        # If it does not, the line is corrupt.
        for character in line:
            
            # Check if the character is an opening value. 
            if character in bracket_pairs.keys():
                
                # Append it to the opener list.
                openers.append(character)
                message = ("Opener List: ", openers)
            
            # If it is a closer, compare it to the last opener.
            else:
                
                # If it is a match, remove the last opener value. 
                if character == bracket_pairs[openers[-1]]:
                    message = ("Last opener: ", openers[-1], "Closer: ", character, \
                            "Match: ", character == bracket_pairs[openers[-1]])
                    logging.info(message)
                    openers.pop()
                    message = ("Opener List: ", openers)
                    logging.info(message)
                
                # If it is not a match, it is corrupt.
                # Stop assessing the line.
                else:
                    message = ("Last opener: ", openers[-1], "Closer: ", character, \
                            "Match: ", character == bracket_pairs[openers[-1]])
                    logging.info(message)
                    message = ("Corrupt line, stopping assessment of line.")
                    logging.info(message)
                    corrupt_lines.append(line)
                    corrupting_values.append(character)
                    break
    
    # Return the number of corrupt lines and the corrupting values.
    message = ("Number of corrupt lines: ", len(corrupt_lines), \
            "\nList of corrupting values: ", corrupting_values)
    logging.info(message)
    
    # Create a dictionary of corrupting closer scores.
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    
    # Calculate the score and return to the user.
    score = 0
    for character in corrupting_values:
        score += scores[character]
    print(score)


"""
Find and discard corrupted lines.
Provide the missing brackets to correctly close the incomplete lines.
Assign score values to each of the closing brackets.
Calculate the total score for each line.
Return the largest scoring line.
"""
# Function to handle Task 2.
def task2(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Use a dictionary to store legal pairs of openers and closers.
    bracket_pairs = {
        "{": "}",
        "[": "]",
        "<": ">",
        "(": ")"
        }
    
    # Initialise an empty list of incomplete lines and remaining openers.
    incomplete_lines = []
    incomplete_openers = []
    
    # Iterate through each line to inspect corrupt lines.
    for line in input_data:
        message = ("\nNew line: ", line)
        logging.info(message)
        
        # Initialise an empty list of openers.
        openers = []
        
        # Iterate through each character in a line.
        # If it is an opening character, append to the openers list.
        # Else the character is a closing character.
        # We need to check it against the last item in the opener list.
        # Compare the character to the dict[key] where key is opener[-1]
        # If it matches, remove the last opener entry.
        # If it does not, the line is corrupt.
        for index, character in enumerate(line):
            
            # Check if the character is an opening value. 
            if character in bracket_pairs.keys():
                
                # Append it to the opener list.
                openers.append(character)
                message = ("Opener List: ", openers)
            
            # If it is a closer, compare it to the last opener.
            else:
                
                # If it is a match, remove the last opener value. 
                if character == bracket_pairs[openers[-1]]:
                    message = ("Last opener: ", openers[-1], "Closer: ", character, \
                            "Match: ", character == bracket_pairs[openers[-1]])
                    logging.info(message)
                    openers.pop()
                    message = ("Opener List: ", openers)
                    logging.info(message)
                
                # If it is not a match, it is corrupt.
                # Stop assessing the line.
                else:
                    message = ("Last opener: ", openers[-1], "Closer: ", character, \
                            "Match: ", character == bracket_pairs[openers[-1]])
                    logging.info(message)
                    message = ("Corrupt line, stopping assessment of line.")
                    logging.info(message)
                    break
            
            # If the character is the last in the list add to the
            # incomplete_lines variable.
            if index + 1 == len(line):
                incomplete_lines.append(line)
                incomplete_openers.append(openers)
    
    # Return the number of corrupt lines and the corrupting values.
    message = ("Number of incomplete lines: ", len(incomplete_lines))
    logging.info(message)
    for line in incomplete_openers:
        message = ("Incomplete openers: ", line)
        logging.info(message)
    
    # Create a variable to store the required closing brackets.
    # Read the incomplete openers and create a list of their counterparts.
    # Reverse the list to generate the correct order to close the brackets.
    required_closers = []
    for line in incomplete_openers:
        temp_closer = []
        for character in line:
            temp_closer.append(bracket_pairs[character])
        temp_closer.reverse()
        required_closers.append(temp_closer)
    
    # Create a dictionary of corrupting closer scores.
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    
    # Calculate the score of each line using the given formula.
    line_scores = []
    for line in required_closers:
        score = 0
        for character in line:
            score *= 5
            score += scores[character]
        line_scores.append(score)
    
    # Find the middle score (winner).
    line_scores.sort()
    print(line_scores[len(line_scores)//2])


# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_10.demo"
input_file = "advent-of-code-2021/inputs/day_10.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)