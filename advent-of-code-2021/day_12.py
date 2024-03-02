#--- Day 12: Passage Pathing ---


# Function to read the data from an input file.
def read_file(file_path):

    # Open the file
    with open(file_path) as fin:
    
        # Read the file and store each line in a list object.
        # Split each line about "-" symbol.
        file_data = [line.strip().split("-") for line in fin]
    
    # Close the file.
    fin.close()
    
    # Return the data.
    return file_data


# Function to map the input data as a python dictionary.
def create_map(input_data):

    # Create a dictionary to store the map.
    map = dict()

    # Iterate through each line in the input data.
    for line in input_data:

        # Store each node in separate variables.
        start, end = line[0], line[1]

        # Add the nodes to the dictionary in both directions.
        if start in map:
            map[start].append(end)
        else:
            map[start] = [end]
        if end in map:
            map[end].append(start)
        else:
            map[end] = [start]
    
    # Return the map.
    return map


# Create a function to find paths using a Depth-First Search - Task 1.
def find_paths1(map, current_node, visited_nodes, path_list):

    # print(  "\n", map, \
    #         "\nCurrent Node: ", current_node, \
    #         "\nVisited Nodes: ", visited_nodes, \
    #         "\nPath list: ", path_list)

    # Check that the current node is not the "end" node.
    # If it is, that is the full route and should be returned.
    if current_node == "end":
        return [path_list + [current_node]]
    
    # Otherwise, keep searching the map.
    path_list = []
    for next_node in map[current_node]:
        
        # Check if the next-node along has been visited.
        # If it is an upper-case node it may be visited more than once.
        if next_node not in visited_nodes or next_node.isupper():

            # Create a copy of the visited node set list.
            # Add the next node to it.
            # Call the function again to explore further.
            next_visited = visited_nodes.copy()
            next_visited.add(next_node)
            path_list += find_paths1(map, next_node, next_visited, \
                                    path_list + [current_node])
        
    # Return the path list.
    return path_list


"""
The goal is to find the number of distinct paths that:
    * Start at start
    * End at end
    * Do not visit small caves more than once

There are two types of caves: 
    * Big caves (written in uppercase)
    * Small caves (written in lowercase)
"""
# Function to handle Task 1.
def task1(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Import the a map into a dictionary object.
    map = create_map(input_data)
    
    # Start at the "start" node.
    current_node = "start"
    
    # Use a set to track all unique nodes visited.
    visited_nodes = set(["start"])
    
    # Initialise an empty variable to track unique paths.
    path_list = []

    # Find all the paths from "start".
    path_list = find_paths1(map, current_node, visited_nodes, path_list)
    
    print("Number of routes: ", len(path_list))


# Create a function to find paths using a Depth-First Search - Task 2.
def find_paths2(map, current_node, visited_nodes, path_list, double_visit_used):

    # Check that the current node is not the "end" node.
    # If it is, that is the full route and should be returned.
    if current_node == "end":
        return [path_list + [current_node]]
    
    # Otherwise, keep searching the map.
    path_list = []
    for next_node in map[current_node]:

        if next_node not in visited_nodes or next_node.isupper():

            path_list += find_paths2(map, next_node, visited_nodes.union({next_node}), path_list + [current_node], double_visit_used)

        elif next_node not in ["start", "end"] and not double_visit_used:
            path_list += find_paths2(map, next_node, visited_nodes, path_list + [current_node], True)
        
    # Return the path list.
    return path_list


"""
Now a single small cave (not start or end) can be visited more than once.
"""
# Function to handle Task 2.
def task2(task_input):

    # Load the input_data data.
    input_data = read_file(task_input)
    
    # Import the a map into a dictionary object.
    map = create_map(input_data)
    
    # Start at the "start" node.
    current_node = "start"
    
    # Use a set to track all unique nodes visited.
    visited_nodes = set(["start"])
    
    # Initialise an empty variable to track unique paths.
    path_list = []

    # Find all the paths from "start".
    path_list = find_paths2(map, current_node, visited_nodes, path_list, False)
    
    print("Number of routes: ", len(path_list))
    




# Set file paths.
demo_file = "advent-of-code-2021/inputs/day_12.demo"
input_file = "advent-of-code-2021/inputs/day_12.input"

# Run task1
print("Running Task 1:")
task1(demo_file)
task1(input_file)

# Run task2
print("\nRunning Task 2:")
task2(demo_file)
task2(input_file)