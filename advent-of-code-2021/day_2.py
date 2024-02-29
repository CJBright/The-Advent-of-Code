#--- Day 2: Dive! ---


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file.
    with open(file_path) as fin:
    
        # Read the file, splitting around new line characters "\n".
        # Store the data in a list object.
        file_data = [line for line in fin.read().split("\n")]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


# Function to handle Task 1.
def task1(task_input):

    # Load the input data.
    input_data = read_file(task_input)
    
    # Initialise location variables for tracking.
    pos_vert = 0
    pos_hor = 0
    
    # Iterate through each instruction.
    # Split into a direction and magnitude component.
    for instruction in input_data:
        direction = instruction.split()[0]
        magnitude = int(instruction.split()[1])
        
        # Change the position variables according to these values.
        # Else clause used as all remaining values are "down".
        if direction == 'forward':
            pos_hor += magnitude
        elif direction == 'up':
            pos_vert -= magnitude
        else:
            pos_vert += magnitude
    
    # Return the task solution, multiplying the end coordinates.
    print(f"Multiplied answer is: {pos_vert * pos_hor}.")


# Function to handle Task 2.
def task2(task_input):

    # Load the input data.
    input_data = read_file(task_input)
    
    # Initialise location variables for tracking.
    pos_vert = 0
    pos_hor = 0
    aim = 0
    
    # Iterate through each instruction.
    # Split into a direction and magnitude component.
    for instruction in input_data:
        direction = instruction.split()[0]
        magnitude = int(instruction.split()[1])
        
        # Change the position variables according to these values.
        # Else clause used as all remaining values are "down".
        if direction == 'forward':
            pos_hor += magnitude
            pos_vert += magnitude * aim
        elif direction == 'up':
            aim -= magnitude
        else:
            aim += magnitude
    
    # Return the task solution, multiplying the end coordinates.
    print(f"Multiplied answer is: {pos_vert * pos_hor}.")


# Set file paths
demo_file = "advent-of-code-2021/inputs/day_2.demo"
input_file = "advent-of-code-2021/inputs/day_2.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)