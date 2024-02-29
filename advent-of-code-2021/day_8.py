#--- Day 8: Seven Segment Search ---


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
    with open(file_path) as fin:
    
        # Read the file.
        # Store all lines in the file in a list object.
        # Replace all newline characters with a space.
        # Split the input around empty spaces.
        # Convert each input to a string.
        file_data = [str(i) for i in fin.read().replace('\n', ' ').split(' ')]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


"""
Input:
    Part 1 = 0-9 displayed. Wires are mixed up.
    Part 2 = 4 numbers to be deciphered

Tasked to find the number of times 1,4,7,8 appears in second half
"""
# Function to handle Task 1.
def task1(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Find the total number of entries in the input data.
    # Each line splits into 15 sections.
    # Hence divide the length of the split data by 15.
    num_entries = int(len(input_data) / 15)
    print(f"Number of entries = {num_entries}.")
    
    # Create a dictionary of unique numbers and their length.
    # This is in the form of {unique_number:number_segments}
    unique_length = {1:2, 4:4, 7:3, 8:7}
    
    # Iterate through the input data in chunks of 15 entries.
    # Store the first 10 entries as a Part 1 variable.
    # Store the last 4 entries as a Part 2 variable.
    count = 0
    for i in range(num_entries + 1):
        entry = input_data[(i*15):(((i+1) * 15) + 1)]
        e_pt_1 = entry[:10]
        e_pt_2 = entry[11:15]
        
        # Check the values stored in the Part 2 variable against the unique numbers.
        # If the number of segments is the same as the uniques, increase the count.
        for number in e_pt_2:
            if len(number) in unique_length.values():
                count += 1
    
    # Return the findings.
    print(f"Number of times 1,4,7,8 appear in output values = {count}")

"""
Numbers:
0 = a,b,c,e,f,g
1 = c,f
2 = a,c,d,e,g
3 = a,c,d,f,g
4 = b,c,d,f
5 = a,b,d,f,g
6 = a,b,d,e,f,g
7 = a,c,f
8 = a,b,c,d,e,f,g
9 = a,b,c,d,f,g

Initial identification:
1,4,7,8 = Identified due to unique arrangement
1: {c,f}            -> {c,f}        // {c,f}
7: {a,c,f}          -> {a}          // {a,c,f}
4: {b,c,d,f}        -> {b, d}       // {a,b,c,d,f}
9: {a,b,c,d,f,g}    -> {g}          // {a,b,c,d,f,g}
8: {a,b,c,d,e,f,g}  -> {e}          // {a,b,c,d,e,f,g}
Add 9 to known number dictionary:

// Definite
    {a,e,g}
    {1,4,7,8,9}
// Unknowns
    {b,d} = {x,y}
    {c,f} = {i,k}
    {0,2,3,5,6}

Secondary identification:
# Use 0 to find d value.    Split into d and b
Add 0 to known number dictionary:
# Use 6 to find c value.    Split into c and f
Add remainder to knowns dictionary:

Tasked to decipher the numbers in second half of the text.
Concatenate the strings of these numbers.
Sum the concatenated numbers.
"""
# Function to handle Task 2.
def task2(task_input, debug):
    
    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Find the total number of entries in the input data.
    # Each line splits into 15 sections.
    # Hence divide the length of the split data by 15.
    num_entries = int(len(input_data) / 15)
    print(f"Number of entries = {num_entries}.")
    
    # Create dictionaries of:
        # unique numbers and their constituent slots {number : slots}
        # all numbers and the number of slots they need {number : n_slots}
    unique_length = {1:2, 4:4, 7:3, 8:7}
    number_length = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    
    # Iterate through the input data in chunks of 15 entries.
    # Store the first 10 entries as a Part 1 variable.
    # Store the last 4 entries as a Part 2 variable.
    overall_tot = 0
    for line in range(num_entries):
        if debug == True: 
            print(f"\nAssessing line {line + 1}.")
        entry = input_data[(line*15):(((line+1) * 15) + 1)]
        e_pt_1 = entry[:10]
        e_pt_2 = entry[11:15]
        
        # Create dictionaries to track combinations and segment arrangements.
        track_combination = dict()
        track_arrangement = dict()
        
        # Add the 4 unique numbers to the tracked combination dictionary.
        for output in e_pt_1:
            for value in unique_length.values():
                if len(output) == value:
                    key = list(unique_length.keys())[list(unique_length.values()).index(value)]
                    track_combination[key] = list(output)
        if debug == True:
            print("Added 4 unique numbers to tracked combinations:")
            print(track_combination)
        
        # Add segment selections {c,f} to tracked segment arrangement
        track_arrangement['c,f'] = track_combination[1]
        if debug == True:
            print("\nAdded segment ['c,f'] to tracked segment arrangement:")
            print(track_arrangement)
        
        # Add segment selection {a} to tracked segment arrangement.
        # Value is found from segment arrangements in (7) & (1)
        for segment in track_combination[7]:
            if segment not in track_combination[1]:
                track_arrangement['a'] = list(segment)
        if debug == True:
            print("\nAdded segment ['a'] to tracked segment arrangement:")
            print(track_arrangement)
        
        # Add segment selection {b,d} to tracked segment arrangement.
        # value is found from segment arrangements in (4) & (1)
        temp_segments = []
        for segment in track_combination[4]:
            if segment not in track_combination[1]:
                temp_segments.append(segment)
        track_arrangement['b,d'] = temp_segments
        if debug == True:
            print("\nAdded segment ['b,d'] to tracked segment arrangement:")
            print(track_arrangement)
        
        # Add segment selection {g} to tracked segment arrangement.
        # Value is found from segment arrangements in (9) and already tracked segments
        known_keys = []
        known_segments = []
        for key in track_arrangement:
            if key != ',': known_keys.extend(key)
            known_segments.extend(track_arrangement[key])
        known_keys = list(filter(lambda known_keys: known_keys != ',', known_keys))
        if debug == True:
            print("\nCurrent tracked keys are:")
            print(known_keys)
            print("Corresponding tracked arrangements are:")
            print(list(known_segments))
        
        # Go through each segment combination in the input line
        # If it matches the expected number of segments needed for 9:
        for output in e_pt_1:
            if len(output) == number_length[9]:
                temp_segments = []
                
                # Find the missing letters
                for value in list(output):
                    if value not in known_segments:
                        temp_segments.append(value)
                
                # If only 1 missing letter, add to the tracked list
                if len(temp_segments) == 1:
                    track_arrangement['g'] = temp_segments
        
        if debug == True:
            print("\nAdded segment ['g'] to tracked segment arrangement:")
            print(track_arrangement)
        
        # Add segment selection {e} to tracked segment arrangement.
        # Value is found from segment arrangements in (8) and already tracked segments
        known_keys = []
        known_segments = []
        for key in track_arrangement:
            if key != ',': known_keys.extend(key)
            known_segments.extend(track_arrangement[key])
        known_keys = list(filter(lambda known_keys: known_keys != ',', known_keys))
        if debug == True:
            print("\nCurrent tracked keys are:")
            print(known_keys)
            print("Corresponding tracked arrangements are:")
            print(list(known_segments))       
        
        # Go through each segment combination in the input line
        # If it matches the expected number of segments needed for 9:
        for output in e_pt_1:
            if len(output) == number_length[8]:
                temp_segments = []
                
                # Find the missing letters
                for value in list(output):
                    if value not in known_segments:
                        temp_segments.append(value)
                
                # If only 1 missing letter, add to the tracked list
                if len(temp_segments) == 1:
                    track_arrangement['e'] = temp_segments
        
        if debug == True:
            print("\nAdded segment ['e'] to tracked segment arrangement:")
            print(track_arrangement)
            
        # Add the segment combination for the number 9 to tracked combinations dictionary
        temp_segments = []
        for key in track_arrangement.keys():
            if key != 'e':
                temp_segments.extend(track_arrangement[key])
        track_combination[9] = temp_segments
        
        if debug == True:
            print("\nAdded the number 9 to tracked combinations:")
            print(track_combination)
        
        # Add segment selection {d} to tracked segment arrangement.
        # Value is found from segment arrangements in (0) and already tracked segments
        # Segment arrangement for {b} can also be found from this
        known_keys = []
        known_segments = []
        for key in track_arrangement:
            if key != ',': known_keys.extend(key)
            known_segments.extend(track_arrangement[key])
        known_keys = list(filter(lambda known_keys: known_keys != ',', known_keys))
        
        if debug == True:
            print("\nCurrent tracked keys are:")
            print(known_keys)
            print("Corresponding tracked arrangements are:")
            print(list(known_segments))
            print("Looking for 0: ", ['a','b','c','e','f','g'])
        
        # Go through each segment combination in the input line
        for output in e_pt_1:
            # Check if length of input matches expected for (0)
            if len(output) == number_length[0]:
                
                # check input is not the already tracked combination for (9)
                comparison_1 = list(output)
                comparison_1.sort()
                comparison_2 = track_combination[9]
                comparison_2.sort()
                if comparison_1 != comparison_2:
                    if debug == True:
                        print("\nLooking at data line = ", output)
                        print(f"Expecting ['b,d'] value of either {track_arrangement['b,d']}.")
                    
                    # Check if missing segment corresponds to KEY {e}
                    # Add {e} to tracked arrangement
                    count_0 = 0
                    count_1 = 0
                    assign = int()
                    
                    for value in range(len(track_arrangement['b,d'])):
                        if debug == True:
                            print(f"Looking for ({track_arrangement['b,d'][value]}) within = {comparison_1}.")
                        
                        if track_arrangement['b,d'][value] in comparison_1:
                            if value == 0:
                                count_0 += 1
                                assign = track_arrangement['b,d'][0]
                                if debug == True:
                                    print(track_arrangement['b,d'][0], "Match")
                            
                            else:
                                count_1 += 1
                                assign = track_arrangement['b,d'][1]
                                if debug == True:
                                    print(track_arrangement['b,d'][1], "Match")
                        else:
                            if debug == True:
                                print("No match")
                    
                    if count_0 == 1 and count_1 == 1:
                        if debug == True:
                            print("2 matches - ignoring line")
                    else:
                        if debug == True:
                            print("1 match.", assign)
                        track_arrangement['b'] = [assign]
                        if debug == True:
                            print(track_arrangement)
                        
                        for point in track_arrangement['b,d']:
                            if point not in track_arrangement['b'][0]:
                                track_arrangement['d'] = [point]
                                if debug == True: print(track_arrangement)
                                break
        
        track_arrangement.pop('b,d', None)
        if debug == True: print(track_arrangement)
        
        # Add the segment combination for the number 0 to tracked combinations dictionary
        temp_segments = []
        for key in track_arrangement.keys():
            if key != 'd':
                temp_segments.extend(track_arrangement[key])
        track_combination[0] = temp_segments
        if debug == True:
            print("\nAdded the number 0 to tracked combinations:")
            print(track_combination)
        
        # Add segment selection {f} to tracked segment arrangement.
        # Value is found from segment arrangements in (6) and already tracked segments
        # Segment arrangement for {c} can also be found from this
        known_keys = []
        known_segments = []
        for key in track_arrangement:
            if key != 'c,f':
                if key != ',':
                    known_keys.extend(key)
                known_segments.extend(track_arrangement[key])
        known_keys = list(filter(lambda known_keys: known_keys != ',', known_keys))
        if debug == True:
            print("\nCurrent tracked keys are:")
            print(known_keys)
            print("Corresponding tracked arrangements are:")
            print(list(known_segments))
            print("Looking for 6: ", ['a','b','d', 'e', 'f','g'])
        
        # Go through each segment combination in the input line
        for output in e_pt_1:
            # Check if length of input matches expected for (6)
            if len(output) == number_length[6]:
                
                # check input is not the already tracked combination for (9) or (0)
                comparison_1 = list(output)
                comparison_1.sort()
                comparison_2 = track_combination[9]
                comparison_2.sort()
                comparison_3 = track_combination[0]
                comparison_3.sort()
                if comparison_1 != comparison_2 and comparison_1 != comparison_3:
                    if debug == True:
                        print("\nLooking at data line = ", output)
                        print(f"Expecting ['c,f'] value of either {track_arrangement['c,f']}.")
                    
                    # Check if missing segment corresponds to KEY {f}
                    # Add {f} to tracked arrangement
                    count_0 = 0
                    count_1 = 0
                    assign = int()
                    
                    for value in range(len(track_arrangement['c,f'])):
                        if debug == True:
                            print(f"Looking for ({track_arrangement['c,f'][value]}) within = {comparison_1}.")
                        
                        if track_arrangement['c,f'][value] in comparison_1:
                            if value == 0:
                                count_0 += 1
                                assign = track_arrangement['c,f'][0]
                                if debug == True:
                                    print(track_arrangement['c,f'][0], "Match")
                            
                            else:
                                count_1 += 1
                                assign = track_arrangement['c,f'][1]
                                if debug == True:
                                    print(track_arrangement['c,f'][1], "Match")
                        else:
                            if debug == True:
                                print("No match")
                    
                    if count_0 == 1 and count_1 == 1:
                        if debug == True:
                            print("2 matches - ignoring line")
                    else:
                        if debug == True:
                            print("1 match.", assign)
                        track_arrangement['f'] = [assign]
                        if debug == True:
                            print(track_arrangement)
                        
                        for point in track_arrangement['c,f']:
                            if point not in track_arrangement['f'][0]:
                                track_arrangement['c'] = [point]
                                if debug == True: print(track_arrangement)
                                break
        
        track_arrangement.pop('c,f', None)
        if debug == True: print(track_arrangement)
        
        # Add remaining numbers to tracked numbers dictionary.
        to_add_numbers = [0,2,3,5,6]
        to_add_letters = [['a', 'b', 'c', 'e', 'f', 'g'], 
                            ['a', 'c', 'd', 'e', 'g'], 
                            ['a', 'c', 'd', 'f', 'g'],
                            ['a', 'b', 'd', 'f', 'g'], 
                            ['a', 'b', 'd', 'e', 'f', 'g']]
        for number in range(len(to_add_numbers)):
            known_segments = []
            
            # if debug == True:
            #     print("Number = ", to_add_numbers[number])
            #     print("Letters = ", to_add_letters[number])
            
            for value in range(len(to_add_letters[number])):
                letter_before = to_add_letters[number][value]
                letter_after = track_arrangement[letter_before]
                
                # if debug == True:
                #     print(letter_before, letter_after)
                
                known_segments.extend(letter_after)
                track_combination[to_add_numbers[number]] = known_segments
        if debug == True:
            print("\nAdded the remaining numbers to tracked combinations:")
            print(track_combination)
        
        # Sort and display - segments.
        print(f"\nFinal segment arrangement:")       
        track_arrangement = {k: track_arrangement[k] for k in sorted(track_arrangement)}
        for i in range(len(track_arrangement.keys())):
            print(f"{list(track_arrangement.keys())[i]}, \t{list(track_arrangement.values())[i]}.")
        
        # Sort and display - numbers.
        print(f"\nFinal combinations:")
        track_combination = {k: track_combination[k] for k in sorted(track_combination)}
        for i in range(len(track_combination.keys())):
            print(f"{list(track_combination.keys())[i]}, {list(track_combination.values())[i]}.")
        
        # Decrypt and add the 4 output numbers.
        string_total = ''
        for output in e_pt_2:
            comparison_1 = list(output)
            comparison_1.sort()
            
            for value in track_combination:
                comparison_2 = track_combination[value]
                comparison_2.sort()
                
                if comparison_1 == comparison_2:
                    string_total = string_total + str(value)
        
        print(f"Complete line {line}. \nTotal = {string_total}.\n")
        overall_tot += int(string_total)
    print(f"\n{overall_tot}")




# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_8.demo"
input_file = "advent-of-code-2021/inputs/day_8.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file, False)
task2(input_file, False)
