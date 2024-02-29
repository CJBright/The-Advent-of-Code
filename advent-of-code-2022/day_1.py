# --- Day 1: Calorie Counting ---

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_1.demo'
    else:
        f_path = 'advent-of-code-2022/day_1.in'
    with open(f_path, 'r') as f_in:
        data = [line.strip('\n') for line in f_in.readlines()]
    return data

# Task 1
def task1(demo=False):
    input = in_data(demo)    
    elves = []
    cal_sum = 0
    for item in range(len(input)):
        if input[item] != '':
            cal_sum += int(input[item])
        else:
            elves.append(cal_sum)
            cal_sum = 0
    print("Max calories carried by: ", max(elves))
    print("Elf carrying the max: ", elves.index(max(elves))+1)

# Task 2 
def task2(demo=False):
    input = in_data(demo)    
    elves = []
    cal_sum = 0
    for item in range(len(input)):
        if input[item] != '':
            cal_sum += int(input[item])
        else:
            elves.append(cal_sum)
            cal_sum = 0
    elves.sort()
    sorted_elves = elves[-3:]
    print("Sum of top 3 elves: ", sum(sorted_elves))

if __name__ == '__main__':
    task1()
    task2()