#--- Day 5: Supply Stacks ---
import numpy as np

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_5.demo'
    else:
        f_path = 'advent-of-code-2022/day_5.in'
    with open(f_path, 'r') as f_in:
        data = [line.strip('\n') for line in f_in.readlines()]
    return data

def task1(demo=False):
    input = in_data(demo)
    crates, instructions, stacks = [], [], []
    for line in input:
        if '[' in line:
            if '    ' in line:
                line = line.replace('    ', ' ')
            crates.append(line.split(' '))
        elif 'move' in line:
            instructions.append(line.split())
        else:
            if line != '':
                stacks = line.split()
    print("Number of stacks: ", stacks[-1])
    crates = np.array(crates)
    
    for instruction in instructions:
        n_crate = int(instruction[1])
        loc_o = int(instruction[3]) - 1
        loc_n = int(instruction[-1]) - 1
        print('\nMoving', n_crate, 'crate(s) from stack', loc_o + 1, 'to stack', loc_n + 1)
        
        for i in range(n_crate):
            print('Moving crate', i+1, '/', n_crate)
            moving = ''
            for j in range(len(crates[:,loc_o])):
                if crates[j,loc_o] != '':
                    moving = crates[j,loc_o]
                    print('Moving crate:', moving)
                    crates[j,loc_o] = ''
                    break
            for k in range(len(crates[:, loc_n])):
                if crates[k, loc_n] != '':
                    if crates[k-1, loc_n] != '':
                        print('Adding row')
                        new_row = ['']*int(stacks[-1])
                        crates = np.vstack([new_row, crates])
                        crates[0, loc_n] = moving
                    else:
                        crates[k-1, loc_n] = moving
                    break
                elif k == len(crates[:, loc_n])-1 and crates[k, loc_n] == '':
                    crates[k, loc_n] = moving
                    break
            print(crates, '\n')
    
    final = []
    for i in range(int(stacks[-1])):
        for j in range(len(crates[:,i])):
            if crates[j, i] != '':
                final.append(crates[j, i].replace('[','').replace(']',''))
                break
    print(''.join(final))

def task2(demo=False):
    input = in_data(demo)
    crates, instructions, stacks = [], [], []
    for line in input:
        if '[' in line:
            if '    ' in line:
                line = line.replace('    ', ' ')
            crates.append(line.split(' '))
        elif 'move' in line:
            instructions.append(line.split())
        else:
            if line != '':
                stacks = line.split()
    print("Number of stacks: ", stacks[-1])
    crates = np.array(crates)
    print(crates)
    
    for instruction in instructions:
        n_crate = int(instruction[1])
        loc_o = int(instruction[3]) - 1
        loc_n = int(instruction[-1]) - 1
        print('\nMoving', n_crate, 'crate(s) from stack', loc_o + 1, 'to stack', loc_n + 1)
        
        moving = []
        for i in range(len(crates[:,loc_o])):
            if crates[i,loc_o] != '':
                for j in range(n_crate):
                    moving.append(crates[i+j,loc_o])
                    crates[i+j,loc_o] = ''
                print('Moving crate(s):', moving)
                break
        
        moving.reverse()
        for i in range(len(moving)):
            print('Placing box', moving[i])
            
            for j in range(len(crates[:, loc_n])+1):
                print('Looking at:', [crates[j, loc_n]])
                
                if crates[j, loc_n] != '':
                    print('Not Empty')
                    if crates[j-1, loc_n] != '':
                        print('No Empty row. Adding row')
                        new_row = ['']*int(stacks[-1])
                        crates = np.vstack([new_row, crates])
                        crates[0, loc_n] = moving[i]
                    else:
                        print('Existing empty row.')
                        crates[j-1, loc_n] = moving[i]
                    break
                
                elif j == len(crates[:, loc_n])-1 and crates[j, loc_n] == '':
                    print('End Is empty')
                    crates[j, loc_n] = moving[i]
                    break
            
            print(crates, '\n')
        print(crates, '\n')
    
    final = []
    for i in range(int(stacks[-1])):
        for j in range(len(crates[:,i])):
            if crates[j, i] != '':
                final.append(crates[j, i].replace('[','').replace(']',''))
                break
    print(''.join(final))

if __name__ == '__main__':
    #task1(True)
    #task1()
    task2(True)
    task2()