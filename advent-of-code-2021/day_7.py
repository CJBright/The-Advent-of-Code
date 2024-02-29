#--- Day 7: The Treachery of Whales ---


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
    with open(file_path) as fin:
    
        # Read the file.
        # Store all lines in the file in a list object.
        # Split the input around commas.
        file_data = [int(i) for i in fin.read().strip().split(',')]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


# Function to handle Task 1.
def task1(task_input, error_log):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Initialise variables used to store the best fuel amount and target value.
    best_target = 0
    best_fuel = 1_000_000_000_000
    
    # Create range of targets.
    # These are increments of 1 between the min and max values.
    print(f"Assessing Horizontal range: {min(input_data)} to {max(input_data)}.")
    for target in range(min(input_data), max(input_data), 1):
    
        # Provide user feedback.
        if error_log == True: print(f"\nAssessing target: {target}.")
        
        # Calculate total fuel for movement to the target.
        # Provide user feedback.
        fuel = 0
        for position in input_data:
            fuel += abs(position - target)
        if error_log == True: print(f"Total fuel to target: {fuel}.")
        
        # Check if the fuel required is lower than the existing best case.
        # If it is better, set it as the new best case.
        if fuel < best_fuel:
            best_fuel = fuel
            best_target = target
            if error_log == True: print(f"\tNew best target: {best_target}.\tTotal fuel: {best_fuel}.")
    
    # Return information to the user of the best target and minimum fuel to get there.
    print(f"SEARCH COMPLETE.\tBEST TARGET: {best_target}.\tTOTAL FUEL: {best_fuel}.")

# Function to handle Task 2.
def task2(task_input, error_log):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Initialise variables used to store the best fuel amount and target value.
    best_target = 0
    best_fuel = 1_000_000_000_000
    
    # Create range of targets.
    # These are increments of 1 between the min and max values.
    print(f"Assessing Horizontal range: {min(input_data)} to {max(input_data)}.")
    for target in range(min(input_data), max(input_data), 1):
        
        # Provide user feedback.
        if error_log == True: print(f"\nAssessing target: {target}.")
        
        # Calculate total fuel for movement to the target.
        # Find the distance of each crab.
        # Find the total fuel for the distance based on the new formula.
        fuel_tot = 0
        for crab_pos in input_data:
            distance = abs(crab_pos - target)
            fuel_crab = 0
            for i in range(distance + 1):
                fuel_crab += i
            fuel_tot += fuel_crab
        if error_log == True: print(f"Total fuel to target: {fuel_tot}.")
        
        # Check if the fuel required is lower than the existing best case.
        # If it is better, set it as the new best case.
        if fuel_tot < best_fuel:
            best_fuel = fuel_tot
            best_target = target
            if error_log == True: print(f"\tNew best target: {best_target}.\tTotal fuel: {best_fuel}.")
    
    # Return information to the user of the best target and minimum fuel to get there.
    print(f"SEARCH COMPLETE.\tBEST TARGET: {best_target}.\tTOTAL FUEL: {best_fuel}.")


# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_7.demo"
input_file = "advent-of-code-2021/inputs/day_7.input"

# Run task1
print("Running Task 1:")
task1(demo_file, False)
task1(input_file, False)

# Run task2
print("\nRunning Task 2:")
task2(demo_file, False)
task2(input_file, False)
