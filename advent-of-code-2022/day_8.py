#--- Day 8: Treetop Tree House ---
import numpy as np

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_8.demo'
    else:
        f_path = 'advent-of-code-2022/day_8.in'
    with open(f_path, 'r') as f_in:
        data = [list(line.strip('\n')) for line in f_in.readlines()]
    return data

def task1(demo=False, console=False):
    input = np.array(in_data(demo))
    if console==True: print('Input:\n',input)
    visible_trees = 0
    
    # Add all perimeter trees
    visible_trees += len(input[0,:]) * 2
    visible_trees += len(input[:,0]) * 2
    visible_trees -= 4
    if console==True: print('\nPerimeter trees:', visible_trees)
    
    # Check internal trees - by row
    if console==True: print('\nChecking Internal trees..\nBy rows:')
    for row in range(input.shape[0]):
        
        # Ignore first and last row
        if row == 0 or row == input.shape[0] - 1:
            pass
        
        else:
            # Check remaining rows
            count = 0
            if console==True: print('\nRow:', row, 'Left to Right.\n', input[row,:])
            
            # Look left to right
            for col in range(input.shape[1] - 1):
                if input[row,col] < input[row, col+1]:
                    count += 1
                    if console==True: print('\t\tL->R +1 tree', input[row,col], '<', input[row, col+1])
                elif input[row,col] == input[row, col+1]:
                    if console==True: print('\t\tL->R == looking further')
                    pass
                else:
                    if console==True: print('\t\tL->R stopped', input[row,col], '>=', input[row, col+1])
                    highest = (row, col)
                    break
            
            # From right to left
            if console==True: print('Row:', row, 'Right to Left.\n', input[row,:])
            for col in reversed(range(input.shape[1] - 1)):
                if input[row,col] > input[row, col+1]:
                    count += 1
                    if console==True: print('\t\tR->L +1 tree', input[row,col], '>', input[row, col+1])
                elif input[row,col] == input[row, col+1]:
                    if console==True: print('\t\tR->L == looking further')
                    pass
                else:
                    if console==True: print('\t\tR->L stopped', input[row,col], '<=', input[row, col+1])
                    print('L->R highest:', highest, 'R->L Stop:', (row,col))
                    if (row, col) == highest:
                        print("match")
                        count -= 1
                    break
                if (row, col) == highest:
                    print("match")
                    count -= 1
            print('Added trees:', count)
    #         visible_trees += count
    
    # # Check internal trees - by column
    # if console==True: print('\nChecking columns:')
    # for col in range(input.shape[1]):
        
    #     # Ignore first and last column
    #     if col == 0 or col == input.shape[1] - 1:
    #         pass
        
    #     else:
    #         # Check remaining columns
    #         count = 0
    #         if console==True: print('Col:', col, '\n', input[:, col])
            
    #         # From top to bottom
    #         for row in range(input.shape[0]):
    #             if input[row+1,col] > input[row, col]:
    #                 count += 1
    #                 if console==True: print('\t\tT->B +1 tree', input[row+1,col], '>', input[row, col])
    #             elif input[row+1,col] == input[row, col]:
    #                 if console==True: print('\t\tEqual, looking at next')
    #                 pass
    #             else:
    #                 if console==True: print('\t\tT->B +0 tree', input[row+1,col], '<=', input[row, col])
    #                 highest = (row, col)
    #                 break
            
    #         # From bottom to top
    #         for row in reversed(range(input.shape[0])):
    #             if input[row-1,col] > input[row, col]:
    #                 count += 1
    #                 if console==True: print('\t\tB->T +1 tree', input[row-1,col], '>', input[row, col])
    #             elif input[row-1,col] == input[row, col]:
    #                 if console==True: print('\t\tEqual, looking at next')
    #                 pass
    #             else:
    #                 if console==True: print('\t\tB->T +0 tree', input[row-1,col], '<=', input[row, col])
    #                 if (row, col) == highest:
    #                     print("BHASBHDJ")
    #                     count -= 1
    #                 break
    #         visible_trees += count
    
    # print('\nNumber of trees:', visible_trees)


if __name__ == '__main__':
    task1(True, True)
    task1()