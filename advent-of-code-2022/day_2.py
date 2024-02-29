#--- Day 2: Rock Paper Scissors ---

def in_data(demo):
    if demo == True:
        f_path = 'advent-of-code-2022/day_2.demo'
    else:
        f_path = 'advent-of-code-2022/day_2.in'
    with open(f_path, 'r') as f_in:
        data = [line.strip('\n').split() for line in f_in.readlines()]
    return data

"""
A | X | 1 - Rock
B | Y | 2 - Paper
C | Z | 3 - Scissors

Win - 6 points
Draw - 3 points
Lose - 0 points
"""

def task1(demo=False):
    input = in_data(demo)
    
    score = 0
    for line in input:
        if line[0] == 'A':
            if line[1] == 'X':
                score += (1+3)
            if line[1] == 'Y':
                score += (2+6)
            if line[1] == 'Z':
                score += (3+0)
        elif line[0] == 'B':
            if line[1] == 'X':
                score += (1+0)
            if line[1] == 'Y':
                score += (2+3)
            if line[1] == 'Z':
                score += (3+6)
        else: # 'C"
            if line[1] == 'X':
                score += (1+6)
            if line[1] == 'Y':
                score += (2+0)
            if line[1] == 'Z':
                score += (3+3)
    print(score)

"""
A | 1 - Rock
B | 2 - Paper
C | 3 - Scissors

X | Lose - 0 points
Y | Draw - 3 points
Z | Win - 6 points
"""
def task2(demo=False):
    input = in_data(demo)
    score = 0
    for line in input:        
        # Rock
        if line[0] == 'A':
            # Lose - Scissors
            if line[1] == 'X':
                score += (0+3)
            # Draw - Rock
            elif line[1] == 'Y':
                score += (3+1)
            # Win - Paper
            else:
                score += (6+2)
        
        # Paper
        elif line[0] == 'B':
            # Lose - Rock
            if line[1] == 'X':
                score += (0+1)
            # Draw - Paper
            elif line[1] == 'Y':
                score += (3+2)
            # Win - Scissors
            else:
                score += (6+3)
        
        # Scissors
        else:
            # Lose - Paper
            if line[1] == 'X':
                score += (0+2)
            # Draw - Scissors
            elif line[1] == 'Y':
                score += (3+3)
            # Win - Rock
            else:
                score += (6+1)
    print(score)

if __name__ == '__main__':
    task1(True)
    task1()
    task2(True)
    task2()