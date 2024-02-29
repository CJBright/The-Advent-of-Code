# --- Day 1: Trebuchet?! ---

# Silver Star
#   Open correct file.
#   Read each line and each character per line.
#   Store the first numeric value.
#   Store the next numeric value and overwrite if a new one is found.
#   If there is only 1 number, assign as both the first and last numeric value.
#   Sum the 2 stored values and add to the total tally.

demodata = "advent-of-code-2023/day-1-task-1.demo"
fulldata = "advent-of-code-2023/day-1-task-1.input"

def task1(inputfile):
    grand_total = 0
    with open(inputfile, "r") as fin:
        
        for line in fin:
            line = line.strip("\n")
            line_total = 0
            first_value = None
            second_value = None
            
            for char in line:
                if char.isnumeric() and first_value == None:
                    first_value = int(char)
                elif char.isnumeric() and first_value != None:
                    second_value = int(char)
                else:
                    pass
            
            if second_value == None:
                second_value = first_value
            
            calibration_value = int(str(first_value) + str(second_value))
            grand_total += calibration_value
        
        print(grand_total)
        fin.close()
task1(demodata)
task1(fulldata)
