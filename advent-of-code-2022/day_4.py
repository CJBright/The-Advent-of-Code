#--- Day 4: Camp Cleanup ---

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_4.demo'
    else:
        f_path = 'advent-of-code-2022/day_4.in'
    with open(f_path, 'r') as f_in:
        data = [line.strip('\n').split(',') for line in f_in.readlines()]
    return data

def task1(demo=False):
    input = in_data(demo)
    count = 0
    for line in input:
        elf_1 = line[0].split('-')
        elf_2 = line[1].split('-')
        if int(elf_1[0]) >= int(elf_2[0]) and int(elf_1[1]) <= int(elf_2[1]):
            count += 1
        elif int(elf_2[0]) >= int(elf_1[0]) and int(elf_2[1]) <= int(elf_1[1]):
            count += 1
        else:
            pass
    print(count)

def task2(demo=False):
    input = in_data(demo)
    count = 0
    for line in input:
        elf_1 = line[0].split('-')
        elf_2 = line[1].split('-')        
        if int(elf_1[0]) in range(int(elf_2[0]), int(elf_2[1]) + 1):
            count += 1
        elif int(elf_1[1]) in range(int(elf_2[0]), int(elf_2[1]) + 1):
            count += 1
        elif int(elf_2[0]) in range(int(elf_1[0]), int(elf_1[1]) + 1):
            count += 1
        elif int(elf_2[1]) in range(int(elf_1[0]), int(elf_1[1]) + 1):
            count += 1
    print(count)


if __name__ == '__main__':
    task1(True)
    task1()
    task2(True)
    task2()