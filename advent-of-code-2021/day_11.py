#--- Day 11: Dumbo Octopus ---

# Import libraries.
import numpy as np

# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
    with open(file_path) as fin:
    
        # Read the file and store each line in a list object.
        # Remove new-line characters and convert each string to an int value.
        # Split each line into its own list.
        file_data = [[int(char) for char in line.strip()] for line in fin]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


# Create a function to flash octopi.
# Check for values of 9 and repeat if needed.
def flash(flashing_octopi, flash_count, input_data, n_rows, n_cols):

    # Initialise a variable to track octopi coordinates that have flashed.
    have_flashed = []
    
    # Iterate through each flashing octopus.
    for row, col in flashing_octopi:
    
        # Check if the octopus have already flashed.
        # If yes, skip flashing this octopus.
        # If no, add it to the have_flashed list.
        if (row,col) in have_flashed:
            print("Flashed already.", row, col)
            continue
        else:
            have_flashed.append((row,col))
        
        # Increase surrounding octopi's energy by 1.
        # di => Above, same row, and below.
        # dj => Left, same column, and right.
        for di in [-1, 0, 1]:  
            for dj in [-1, 0, 1]:  
                
                # Make sure we are within bounds of the grid.
                if 0 <= row + di < n_rows and 0 <= col + dj < n_cols:
                
                    # Avoid incrementing values in the flashing_octopi list.
                    if (row + di, col + dj) not in flashing_octopi:
                        input_data[row + di][col + dj] += 1
                        
                        # Add newly flashing octopi to the flashing_octopi list.
                        if input_data[row + di][col + dj] == 10:
                            flashing_octopi.append((row + di, col + dj))
                            print("Flashing: ", (row, col), \
                                    "Triggered new:", (row + di, col + dj))
        
        #print("\nAfter flashing: ", (row, col), "\n", input_data)
    
    # Reset 9 values to 0.
    flashing_octopi = [(row, col) for row in range(n_rows) \
                    for col in range(n_cols) if input_data[row][col] > 9]
    for row, col in flashing_octopi:
        input_data[row][col] = 0
    
    # Add the number of flashes to the flash count.
    flash_count += len(have_flashed)
    
    # Check if the number of flashes equals the number of octopi.
    if len(have_flashed) == n_rows * n_cols:
        all_flashed = True
    else:
        all_flashed = False
    
    # Output the processed data.
    return input_data, flash_count, all_flashed


"""
In a step all octopus energy levels increase by 1.
At a value of 9, an octopus will flash.
A flashing octopus increased adjacent octopi' energy by 1 (inc. diagonal).
If an adjacent octopus' energy reaches 9, it too flashes.
An octopus can only flash once per step.
An octopus that has flashes resets its energy to 0.
How many flashes ar there after 100 steps
"""
# Function to handle Task 1.
def task1(task_input):

    # Load the input_data data.
    input_data = np.array(read_file(task_input))
    n_rows, n_cols = len(input_data), len(input_data[0])
    
    # Initialise variables to track the current step and flash count.
    step = 0
    flash_count = 0
    
    # Show the initial state.
    print("Step ", step, ":\n", input_data)
    
    # Iterate up until step 101.
    while step < 100:

        # Increase the energy of each octopus by 1.
        for row in range(n_rows):
            for column in range(n_cols):
                input_data[row][column] = input_data[row][column] + 1
        print("\n+1 Energy\n",input_data)
        
        # Find the coordinates of all the octopi ready to flash.
        flashing_octopi = []
        flashing_octopi = [(row, col) for row in range(n_rows) \
                        for col in range(n_cols) if input_data[row][col] > 9]
        print("\nFlashing Octopi:\n",flashing_octopi)

        # Flash the octopi.
        # Repeat until the number that have flashed equals those ready to.
        input_data, flash_count, all_flashed = \
            flash(flashing_octopi, flash_count, input_data, n_rows, n_cols)
        print("Current flashes: ", flash_count)
        
        # Show the current state.
        step += 1
        if step % 10:
            print("\nStep ", step, ":\n", input_data)


"""
Find the first time point that all 100 octopi flash in sync.
"""
# Function to handle Task 2.
def task2(task_input):

    # Load the input_data data.
    input_data = np.array(read_file(task_input))
    n_rows, n_cols = len(input_data), len(input_data[0])
    
    # Initialise variables to track the current step and flash count.
    step = 0
    flash_count = 0
    
    # Initialise a variable to track whether all octopi have flashed.
    all_flashed = False
    
    # Show the initial state.
    print("Step ", step, ":\n", input_data)
    
    # Iterate until the all_flashed variable changes to True.
    while all_flashed == False:
        print(all_flashed)

        # Increase the energy of each octopus by 1.
        for row in range(n_rows):
            for column in range(n_cols):
                input_data[row][column] = input_data[row][column] + 1
        print("\n+1 Energy\n",input_data)
        
        # Find the coordinates of all the octopi ready to flash.
        flashing_octopi = []
        flashing_octopi = [(row, col) for row in range(n_rows) \
                        for col in range(n_cols) if input_data[row][col] > 9]
        print("\nFlashing Octopi:\n",flashing_octopi)

        # Flash the octopi.
        input_data, flash_count, all_flashed = \
            flash(flashing_octopi, flash_count, input_data, n_rows, n_cols)
        print("Current flashes: ", flash_count)
        
        # Increment the step.
        step += 1
        
    # Show the current state.
    print("\nStep ", step, ":\n", input_data)


# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_11.demo"
input_file = "advent-of-code-2021/inputs/day_11.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("Running Task 2:")
task2(demo_file)
task2(input_file)