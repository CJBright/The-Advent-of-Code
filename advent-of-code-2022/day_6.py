#--- Day 6: Tuning Trouble ---

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_6.demo'
    else:
        f_path = 'advent-of-code-2022/day_6.in'
    with open(f_path, 'r') as f_in:
        data = [char for char in f_in.readline()]
    return data

def task1(demo=False):
    input = in_data(demo)
    #print(input)
    
    score = 0
    for char in range(len(input)):
        if len(input) - char > 4:
            signal = []
            for chunk in range(4):
                signal.append(input[char + chunk])
            #print(signal)
            
            unique = 0
            if score == 0:
                for point in signal:
                    if signal.count(point) == 1:
                        unique += 1
                        if unique == 4:
                            score += char + 4
                            print(score)
                    else:
                        score = 0

def task2(demo=False):
    input = in_data(demo)
    #print(input)
    
    score = 0
    for char in range(len(input)):
        if len(input) - char > 14:
            signal = []
            for chunk in range(14):
                signal.append(input[char + chunk])
            #print(signal)
            
            unique = 0
            if score == 0:
                for point in signal:
                    if signal.count(point) == 1:
                        unique += 1
                        if unique == 14:
                            score += char + 14
                            print(score)
                    else:
                        score = 0


if __name__ == '__main__':
    task1(True)
    task1()
    task2(True)
    task2()