#---Day 5: Hydrothermal Venture---

# Import libraries.
import numpy as np


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


# Function to find the maximum size of the map.
def find_max(dataset):

    # Initilaise variables to hold the maximum x and y values.
    max_x, max_y = 0, 0
    
    # Iterate through each line in the dataset.
    for i in range(len(dataset)):
        
        # Clean the line and split into a list variable.
        instruction = dataset[i].strip('/n').split()
        
        # Store the X-coordinates as variables and find the maximum.
        x1 = int(instruction[0].split(',')[0])
        x2 = int(instruction[2].split(',')[0])
        if x1 > max_x:
            max_x = x1
        elif x2 > max_x:
            max_x = x2
        
        # Store the Y-coordinates as variables and find the maximum.
        y1 = int(instruction[0].split(',')[1])
        y2 = int(instruction[2].split(',')[1])
        if y1 > max_y:
            max_y = y1
        elif y2 > max_y:
            max_y = y2
    
    # Return the maximum X and Y coordinate values from the input.
    return [max_x, max_y]


# Function to handle Task 1.
def task1(task_input):
    
    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Find the length and width of the map.
    [max_x, max_y] = find_max(input_data)
    
    # Create a square map of maximum coordinate size.
    # Use the zeros function to make it empty.
    # Use max coordinates + 1 due to counting from 0. 
    map = np.zeros((max_y + 1, max_x + 1))
    print("Initialised map:")
    print(map)
    
    # Iterate through each line in the instruction input file.
    # Identify horizontal and vertical lines.
    # Plot these lines.
    for i in range(len(input_data)):

        # Clean the line and split into a list variable.
        instruction = input_data[i].strip('/n').split()
        
        # Store the X and Y-coordinates as variables.
        x1 = int(instruction[0].split(',')[0])
        x2 = int(instruction[2].split(',')[0])
        y1 = int(instruction[0].split(',')[1])
        y2 = int(instruction[2].split(',')[1])
        
        # Identify horizontal or vertical lines by maintained X or Y coordinates.
        if x1 == x2 or y1 == y2:
            print("\tLine found")
            print(f"\tX) {x1} -> {x2}.")
            print(f"\tY) {y1} -> {y2}.")
            
            # Update the map.
            if x1 == x2:
                print(f"\n\tVertical line.")
                for y_val in range(min(y1, y2), max(y1, y2) + 1):
                    print(f"\tMapped - x:{x1}, y:{y_val}.")
                    map[y_val][x1] += 1
            elif y1 == y2:
                print(f"\tHorizontal line.")
                for x_val in range(min(x1, x2), max(x1, x2) + 1):
                    print(f"\t\tMapped - x:{x_val}, y:{y1}.")
                    map[y1][x_val] += 1
    
    # Show the map.
    print(f"\n{map}")
    
    # Calculate the danger value for the map. 
    danger = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            if map[j][i] >= 2:
                danger += 1
    print(f"\nThe answer is = {danger}.")


# Function to handle Task 2.
def task2(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Find the length and width of the map.
    [max_x, max_y] = find_max(input_data)

    # Create a square map of maximum coordinate size.
    # Use the zeros function to make it empty.
    # Use max coordinates + 1 due to counting from 0. 
    map = np.zeros((max_y + 1, max_x + 1))
    print("Initialised map:")
    print(map)
    
    # Iterate through each line in the instruction input file.
    # Plot each line.
    for i in range(len(input_data)):

        # Clean the line and split into a list variable.
        instruction = input_data[i].strip('/n').split()
        
        # Store the X and Y-coordinates as variables.
        x1 = int(instruction[0].split(',')[0])
        x2 = int(instruction[2].split(',')[0])
        y1 = int(instruction[0].split(',')[1])
        y2 = int(instruction[2].split(',')[1])
        
        # Identify horizontal or vertical lines by maintained X or Y coordinates.
        if x1 == x2 or y1 == y2:
            print("\tLine found")
            print(f"\tX) {x1} -> {x2}.")
            print(f"\tY) {y1} -> {y2}.")
            
            # Update the map.
            if x1 == x2:
                print(f"\n\tVertical line.")
                for y_val in range(min(y1, y2), max(y1, y2) + 1):
                    print(f"\tMapped - x:{x1}, y:{y_val}.")
                    map[y_val][x1] += 1
            elif y1 == y2:
                print(f"\tHorizontal line.")
                for x_val in range(min(x1, x2), max(x1, x2) + 1):
                    print(f"\t\tMapped - x:{x_val}, y:{y1}.")
                    map[y1][x_val] += 1
        
        # Identify diagonal lines by equal changes in X and Y.
        if abs(x2-x1) == abs(y2-y1):
            print(f"Diagonal line.")
            
            # Create a list of X coordinates.
            print(f"\tX) {x1} -> {x2}")
            if x1 < x2:
                x_vals = list(range(x1, x2 + 1))            
            else:
                x_vals = list(range(x2, x1 + 1))
                x_vals.reverse()                
            
            # Create a list of Y coordinates.
            print(f"\tY) {y1} -> {y2}")
            if y1 < y2:
                y_vals = list(range(y1, y2 + 1))            
            else:
                y_vals = list(range(y2, y1 + 1))
                y_vals.reverse()                
            
            # Update the map.
            for i in range(len(x_vals)):
                map[y_vals[i]][x_vals[i]] += 1
    
    # Show the map.
    print(f"\n{map}")
    
    # Calculate the danger value for the map.
    danger = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            if map[j][i] >= 2:
                danger += 1
    print(f"\nThe answer is = {danger}.")


# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_5.demo"
input_file = "advent-of-code-2021/inputs/day_5.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)
