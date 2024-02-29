#--- Day 9: Smoke Basin ---


# Import libraries.
import numpy as np


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
    with open(file_path) as fin:
    
        # Read the file.
        # Store each line in a list object.
        # Remove new-line characters.
        # Split each line into its own list.
        file_data = [list(num.strip('\n')) for num in fin.readlines()]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


# Function to handle Task 1.
def task1(task_input):
    
    # Load the input_data data.
    input_data = np.array(read_file(task_input))
    
    # Initialise a list variable to track low points.
    low_points = []
    
    # Iterate through each cell in the map.
    for row in range(input_data.shape[0]):
        for col in range(input_data.shape[1]):
            
            # Create a variable of the value to compare against.
            compare = int(input_data[row, col])
            
            # Compare the value to the values above, below, left, and right.
            # If there is no value in these directions, assume a max height (9).
            up = 9 if row == 0 else int(input_data[row-1, col])
            down = 9 if row + 1 == input_data.shape[0] else int(input_data[row+1, col])
            left = 9 if col == 0 else int(input_data[row, col-1])
            right = 9 if col + 1 == input_data.shape[1] else int(input_data[row, col+1])
            
            # Check if the compare value is a low point.
            # If it is, add it to the low_point list.
            # Add 1 to the low point to get the risk level .
            if compare < up and compare < down and compare < left and compare < right:
                low_points.append(compare + 1)
    
    # Return the sum of the risk level for the low points.
    print(f"Risk level sum: {sum(low_points)}.")


# Function to handle Task 2.
def task2(task_input):

    # Load the input_data data.
    input_data = np.array(read_file(task_input))
        
    # Initialise a list variable to track low points.
    low_points = []
    
    # Iterate through each cell in the map.
    for row in range(input_data.shape[0]):
        for col in range(input_data.shape[1]):
            
            # Create a variable of the value to compare against.
            compare = int(input_data[row, col])
            
            # Compare the value to the values above, below, left, and right.
            # If there is no value in these directions, assume a max height (9).
            up = 9 if row == 0 else int(input_data[row-1, col])
            down = 9 if row + 1 == input_data.shape[0] else int(input_data[row+1, col])
            left = 9 if col == 0 else int(input_data[row, col-1])
            right = 9 if col + 1 == input_data.shape[1] else int(input_data[row, col+1])
            
            # Check if the compare value is a low point.
            # If it is, add the coordinates to the low_point list.
            if compare < up and compare < down and compare < left and compare < right:
                low_points.append((row, col))
    
    # Show the user the location of the low points.
    print(f"Low point coordinates: {low_points}.")

    # Initialise a variable for basin sizes.
    basin_sizes = []
    
    # For each low point coordinate, expand outwards until a value of 9 is hit.
    for low_point in low_points:
        
        # Keep track of visited coordinates in a set.
        visited = set()

        # Use a stack for a Depth First Search.
        stack = [low_point]
        
        # Expand from the compare coordinate until hitting a value of 9.
        while stack:

            # Use a stack to implement the DFS.
            # Pop the stack to get new coordinates.
            cx, cy = stack.pop()
            
            # If the coordinate is already visited or is a 9, skip it
            if (cx, cy) in visited or int(input_data[cx][cy]) == 9:
                continue
            visited.add((cx, cy))
            
            # Check all 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                
                if 0 <= nx < len(input_data) and 0 <= ny < len(input_data[0]):
                    stack.append((nx, ny))
        
        # Append the basin size to the basin sizes list.
        basin_sizes.append(len(visited))
    
    # Sort the list in descending size order.
    basin_sizes.sort(reverse=True)
    
    # Multiply the 3 largest values to find a the answer.
    print("The final number is ", basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_9.demo"
input_file = "advent-of-code-2021/inputs/day_9.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)
