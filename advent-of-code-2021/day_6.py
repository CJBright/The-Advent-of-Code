#--- Day 6: Lanternfish ---

# Import libraries.
# This library avoids Key Errors when creating new dictionary keys.
from collections import defaultdict


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


"""
- 1 laternfish produces 1 new lanternfish every 7 days.
- Not all laternfish productions are synchronous.
- New lanternfish cannot begin reproducing for 2 days.
"""
# Function to handle Task 1.
def task1(task_input, max_days):

    # Load the input_data data.
    input_data = read_file(task_input)

    # Initialise the current day and the day limit variables.
    day, day_limit = 0, max_days
    
    # Iterate through each day until the limit.
    while day < day_limit + 1:
        
        # Show the initial state. 
        if day == 0:
            print(f"Day 0: Total fish: {len(input_data)}.")
        
        # For every new day update fish reproduction timers and add new fish.
        else:
            for fish in range(len(input_data)):
                # Count timer down 1 day
                input_data[fish] -= 1
                
                # If ready to reproduce: Reset adult timer. Add child.
                if input_data[fish] < 0:
                    input_data[fish] = 6
                    input_data.append(8)
            
        #print("Day " + str(day) + ": " + str(input))
        day += 1
    
    print(f"Day {day - 1}: Total fish: {len(input_data)}.\n")


"""
- Run for much longer.
- Cannot brute force using previous method due to time and memory constraints.
"""
# Function to handle Task 2.
def task2(task_input, max_days):

    # Load the input_data data.
    input_data = read_file(task_input)

    # Show the initial state. 
    print(f"Day 0: Total fish: {len(input_data)}.")
    
    # Create dictionary of fish and reproduction frequencies.
    # I.e. 8 days: 5 fish. 7 days: 0 fish... etc.
    fish = defaultdict(int)
    for x in input_data:
        if x not in fish:
            fish[x] = 0
        fish[x] += 1
    print(fish)
    
    # Iterate through each day until the limit.
    for day in range(max_days):
        
        # Create a new dictionary to add updated fish values to.
        new_fish = defaultdict(int)
        
        # Look through each fish' reproductive timer state in the original dictionary.
        for timer, n_fish in fish.items():
            
            # Check if any fish are ready to reproduce - i.e timer == 0.
            # Add a new fish with a reset reproductive timer to the new dictionary.
            # Add a child with a timer value to the new dictionary.
            if timer == 0:
                new_fish[6] += n_fish
                new_fish[8] += n_fish
            
            # Otherwise add each fish to the new dictionary with a timer value -1.
            else:
                new_fish[timer - 1] += n_fish
        
        # Overwrite the old dictionary with the new one.
        fish = new_fish
    
    # Report the final day fish count.
    print(f"Day {max_days}: Total dish: {sum(fish.values())}.\n")



# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_6.demo"
input_file = "advent-of-code-2021/inputs/day_6.input"

# Run task1
print("Running Task 1:")
task1(demo_file, 80)
task1(input_file, 80)

# Run task2
print("\nRunning Task 2:")
task2(demo_file, 256)
task2(input_file, 256)
