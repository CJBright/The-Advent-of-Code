#--- Day 7: No Space Left On Device ---

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_7.demo'
        f_path = 'advent-of-code-2022/day_7.demo_2'
    else:
        f_path = 'advent-of-code-2022/day_7.in'
    with open(f_path, 'r') as f_in:
        data = [line.strip('\n').split() for line in f_in.readlines()]
    return data

def task1(demo=False):
    input = in_data(demo)
    dir_name, dir_index = '', 0
    dir_dict, size_dict = dict(), dict()
    
    for index, line in enumerate(input):
        #print(index, line)
        
        # Look for $ cd command
        if line[0] == '$' and line[1] == 'cd' and line[2] != '..':
            dir_index += 1
            dir_name = str(dir_index) + '_' + line[2]
            print('New directory:', dir_name, '\nNumber of directories:', dir_index)
        
        # Look for $ ls command
        elif line[0] == '$' and line[1] == 'ls':
            print('\tCalled search function')
            dir_dict[str(dir_index) + '_0'] = dir_name
            searching = True
            search_count = 1
            
            while searching == True:
                dir_UID = str(dir_index) + '_' + str(search_count)
                # Get to end of file
                if index + search_count == len(input):
                    break
                # No reason to stop searching
                elif input[index + search_count][0] != '$':
                    print('\t\tAdded directories:', dir_UID)
                    dir_dict[dir_UID] = input[index + search_count]
                    search_count += 1
                # Get to next command
                else:
                    searching = False
        
        # $ cd .. or other
        else:
            pass
    
    # Sum the contents of the directories in reverse order
    dir_list = list(dir_dict.keys())
    dir_list.reverse()
    print('\nAll found directories_subdirectories:\n', dir_list)
    
    # Sort into lists of sub-dirs for each dir
    for dir_num in reversed(range(dir_index + 1)):
        
        # Dir 0 does not exist
        if dir_num == 0:
            pass
        
        # For each dir, sum size of files. If sub-dir look up and sum its size
        else:
            temp_list = []
            print('\nDirectories stemming from:', dir_num)
            
            for dir_name in dir_list:
                if dir_name.startswith(str(dir_num) + '_'):
                    temp_list.append(dir_name)
            temp_list.reverse()
            print(temp_list)
            
            temp_name = dir_dict[temp_list[0]]
            temp_size = 0
            print('Directory name:', temp_name)
            
            for i in range(len(temp_list) - 1):
                
                print(dir_dict)
                print(size_dict)
                print(temp_list[i+1])
                print(dir_dict[temp_list[i+1]])
                print(dir_num)
                print(str(dir_num) + '_' + str(dir_dict[temp_list[i+1]][1]))
                
                if dir_dict[temp_list[i+1]][0] != 'dir':
                    print("if")
                    print(dir_dict[temp_list[i+1]][0])
                    temp_size += int(dir_dict[temp_list[i+1]][0])
                
                else:
                    print("else")
                    search_dir = dir_dict[str(dir_num+1) + '_' + str(dir_dict[temp_list[i+1]][1])]
                    print('Searching for size of:', search_dir)
                    temp_size += int(size_dict[search_dir])
            
            # Save directory and total size
            print('Total size for directory:',temp_name, '=', temp_size)
            size_dict[temp_name] = temp_size
            print(size_dict)
    
    # Find sum of all values <= 100,000
    print('\nSumming all dirs with size <= 100,000')
    tot_sum = 0
    for value in size_dict.values():
        if value <= 100_000:
            print(value)
            tot_sum += value
    print('Total:', tot_sum)


if __name__ == '__main__':
    task1(True)
    #task1()
    # task2(True)
    # task2()