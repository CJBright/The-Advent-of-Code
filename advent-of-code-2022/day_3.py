#--- Day 3: Rucksack Reorganization ---

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_3.demo'
    else:
        f_path = 'advent-of-code-2022/day_3.in'
    with open(f_path, 'r') as f_in:
        data = [list(line.strip('\n')) for line in f_in.readlines()]
    return data

def task1(demo=False):
    input = in_data(demo)
    errors = []
    for line in input:        
        n_items = int(len(line)/2)
        comp_1 = line[:n_items]
        comp_2 = line[n_items:]
        
        for item in comp_1:
            if item in comp_2:
                errors.append(item)
                break
    
    score = 0
    for item in errors:
        if item.upper() == item:
            score += (ord(item.lower()) - 70)
        else:
            score += (ord(item) - 96)
    print(score)

def task2(demo=False):
    input = in_data(demo)
    badges = []
    for i in range(len(input)//3):
        elf_1 = input[i*3]
        elf_2 = input[i*3+1]
        elf_3 = input[i*3+2]
        
        for item in elf_1:
            if item in elf_2 and item in elf_3:
                badges.append(item)
                break
    
    score = 0
    for item in badges:
        if item.upper() == item:
            score += (ord(item.lower()) - 70)
        else:
            score += (ord(item) - 96)
    print(score)


if __name__ == '__main__':
    task1(True)
    task1()
    task2(True)
    task2()