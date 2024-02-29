#--- Day 1: Sonar Sweep ---


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file.
    with open(file_path) as fin:
    
        # Read the file, splitting around new line characters "\n".
        # Remove blank spaces from the line.
        # Convert the value to an integer.
        # Store the data in a list object.
        file_data = [int(line) for line in fin.read().strip().split('\n')]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


# Function to handle Task 1.
def task1(task_input):

    # Load the input data.
        # If the variable is a string - load from a file.
        # If not - assume the variable is the data to use (used in Task 2).
    if type(task_input) == str:
        input_data = read_file(task_input)
    else:
        input_data = task_input
    
    # Initialise variables to track value changes.
    change = []
    increase = []
    decrease = []
    
    # Calculate the value change between neighbouring values.
    # Append the value to the 'changes' list.
    # Check if the value is positive or negative, appending to the relevant list.
    for i in range(len(input_data)-1):
        change.append(input_data[i+1] - input_data[i])
        
        if change[i] > 0:
            increase.append(input_data[i+1] - input_data[i])
        else:
            decrease.append(input_data[i+1] - input_data[i])
    
    # Return the number of positive values to the user.
    print(f"Number of depth increases: {len(increase)}.")


# Function to handle Task 2.
def task2(task_input):

    # Load the input data.
    input_data = read_file(task_input)
    
    # Create a new list of sliding window values.
    # For each value in the list, add the next 2 values.
    # Append this total to the sliding window list.
    sliding_window = []    
    for i in range(len(input_data)-2):
        sliding_window.append(input_data[i] + input_data[i+1] + input_data[i+2])
    
    # Use the same methodology from Task 1 to find the number of increased changes.
    task1(sliding_window)


# Set file paths
demo_file = "advent-of-code-2021/inputs/day_1.demo"
input_file = "advent-of-code-2021/inputs/day_1.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)
