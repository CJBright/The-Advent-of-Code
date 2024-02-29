#--- Day 3: Binary Diagnostic ---


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
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
    
    # Initialise variables for the gamma and epsilon rates.
    gamma_rate, epsilon_rate = [], []
    
    # We need to find the most common value in each bit position.
    # Hence, we will iterate through each bit value in the input for every line.
    for bit in range(len(input_data[0])):
        
        # Initialise variables to track the number of 0s and 1s.
        zeros, ones = 0, 0
        
        # Iterate through each line in the input dataset.
        # Add to the counter depending on the bit's value.
        for line in input_data:
            if line[bit] == '0':
                zeros += 1
            else:
                ones += 1
        
        # Construct the gamma and epsilon rates depending on the most common. 
        if zeros > ones:
            gamma_rate.append(0)
            epsilon_rate.append(1)
        else:
            gamma_rate.append(1)
            epsilon_rate.append(0)
    
    # Join the list variables of the gamma and epsilon rates into a string.
    # map(str, gamma_rate): Converts each integer in the list into a string.
    # ''.join(...): Joins the list of strings into a single string. 
    # int('...', 2): Converts the string representing a binary number into an integer.
    # The 2 indicates that the number is in base 2 (binary).
    gamma_rate = int(''.join(map(str, gamma_rate)), 2)
    epsilon_rate = int(''.join(map(str, epsilon_rate)), 2)

    # Calculate the power consumption value and return to the reader.
    power_consumption = gamma_rate * epsilon_rate
    print(f"Gamma: {gamma_rate}, Epsilon: {epsilon_rate}, Power: {power_consumption}.")


# Function to handle Task 2.
def task2(task_input):

    # Load the input data.
    input_data = read_file(task_input)
    
    # Create a copy of the input data for the oxygen list.
    oxygen_list = input_data.copy()

    # Initalise which bit is being looked at.
    bit = 0
    
    # Iterate through the lines in the dataset.
    # Filter out lines whose bit does not match the bit criteria value.
    # Continue, moving through the bits until there is 1 line remaining.
    while len(oxygen_list) > 1:
        
        # Initialise variables to track the number of 0s and 1s.
        zeros, ones = 0, 0
        
        # Iterate through each line in the dataset.
        # Count the number of lines with 1 or 0 in the current bit position.
        for line in oxygen_list:
            if line[bit] == '0':
                zeros += 1
            else:
                ones += 1
        
        # Filter out values where the current bit does not meet the bit criteria.
        if zeros > ones:
            oxygen_list = [line for line in oxygen_list if line[bit] == '0']
        else:
            oxygen_list = [line for line in oxygen_list if line[bit] == '1']
        
        # Move to the next bit position.
        bit += 1
    
    # Create a copy of the input data for the CO2 list.
    co2_list = input_data.copy()
    
    # Initalise which bit is being looked at.
    bit = 0  
    
    # Iterate through the lines in the dataset.
    # Filter out lines whose bit does not match the bit criteria value.
    # Continue, moving through the bits until there is 1 line remaining.
    while len(co2_list) > 1:
        
        # Initialise variables to track the number of 0s and 1s.
        zeros, ones = 0, 0
        
        # Iterate through each line in the dataset.
        # Count the number of lines with 1 or 0 in the current bit position.
        for line in co2_list:
            if line[bit] == '0':
                zeros += 1
            else:
                ones += 1
        
        # Filter out values where the current bit does not meet the bit criteria.
        if zeros > ones:
            co2_list = [line for line in co2_list if line[bit] == '1']
        else:
            co2_list = [line for line in co2_list if line[bit] == '0']
        
        # Move to the next bit position.
        bit += 1
    
    # Join the list variables of the oxygen and CO2 rates into a string.
    # map(str, gamma_rate): Converts each integer in the list into a string.
    # ''.join(...): Joins the list of strings into a single string. 
    # int('...', 2): Converts the string representing a binary number into an integer.
    # The 2 indicates that the number is in base 2 (binary).
    oxygen_rate = int(''.join(map(str, oxygen_list)), 2)
    co2_rate = int(''.join(map(str, co2_list)), 2)
    
    # Calculate the life support rate and return to the user.
    life_supp_rate = oxygen_rate * co2_rate
    print(f"Oxygen: {oxygen_rate}, CO2: {co2_rate}, Life: {life_supp_rate}.")


# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_3.demo"
input_file = "advent-of-code-2021/inputs/day_3.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)