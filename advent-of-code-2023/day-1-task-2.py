# --- Day 1: Trebuchet?! ---
# --- Golden Star ---

# Method:
#   Open file --> demo or full dataset.
#   Read each line and each character per line.
#   Store the first numeric value.
#   Store the next numeric value and overwrite if a new one is found.
#   If there is only 1 number, assign as both the first and last numeric value.
#   Sum the 2 stored values and add to the total tally.

demodata = "advent-of-code-2023/day-1-task-2.demo"
fulldata = "advent-of-code-2023/day-1-task-2.input"

number_dict = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
    "twentyone": "21",
    "twentytwo": "22",
    "twentythree": "23",
    "twentyfour": "24",
    "twentyfive": "25",
    "twentysix": "26",
    "twentyseven": "27",
    "twentyeight": "28",
    "twentynine": "29",
    "thirty": "30",
    "thirtyone": "31",
    "thirtytwo": "32",
    "thirtythree": "33",
    "thirtyfour": "34",
    "thirtyfive": "35",
    "thirtysix": "36",
    "thirtyseven": "37",
    "thirtyeight": "38",
    "thirtynine": "39",
    "forty": "40",
    "fortyone": "41",
    "fortytwo": "42",
    "fortythree": "43",
    "fortyfour": "44",
    "fortyfive": "45",
    "fortysix": "46",
    "fortyseven": "47",
    "fortyeight": "48",
    "fortynine": "49",
    "fifty": "50",
    "fiftyone": "51",
    "fiftytwo": "52",
    "fiftythree": "53",
    "fiftyfour": "54",
    "fiftyfive": "55",
    "fiftysix": "56",
    "fiftyseven": "57",
    "fiftyeight": "58",
    "fiftynine": "59",
    "sixty": "60",
    "sixtyone": "61",
    "sixtytwo": "62",
    "sixtythree": "63",
    "sixtyfour": "64",
    "sixtyfive": "65",
    "sixtysix": "66",
    "sixtyseven": "67",
    "sixtyeight": "68",
    "sixtynine": "69",
    "seventy": "70",
    "seventyone": "71",
    "seventytwo": "72",
    "seventythree": "73",
    "seventyfour": "74",
    "seventyfive": "75",
    "seventysix": "76",
    "seventyseven": "77",
    "seventyeight": "78",
    "seventynine": "79",
    "eighty": "80",
    "eightyone": "81",
    "eightytwo": "82",
    "eightythree": "83",
    "eightyfour": "84",
    "eightyfive": "85",
    "eightysix": "86",
    "eightyseven": "87",
    "eightyeight": "88",
    "eightynine": "89",
    "ninety": "90",
    "ninetyone": "91",
    "ninetytwo": "92",
    "ninetythree": "93",
    "ninetyfour": "94",
    "ninetyfive": "95",
    "ninetysix": "96",
    "ninetyseven": "97",
    "ninetyeight": "98",
    "ninetynine": "99",
    "one hundred": "100"
}

def task2(inputfile):
    grand_total = 0
    
    with open(inputfile, "r") as fin:
        for line in fin:
            line = line.strip("\n")
            
            line_total = 0
            first_value, second_value = None, None            
            char_index = 0
            
            for char in line:
                if char.isnumeric() and first_value == None:
                    first_value = char
                elif char.isnumeric() and first_value != None:
                    second_value = char
                else:
                    if line[char_index] == "o" or line[char_index] == "t" or line[char_index] == "f" or line[char_index] == "s" or line[char_index] == "3" or line[char_index] == "n":
                        
                char_index += 1
            print(f"Line: {line}, First: {first_value}, Last: {last_value}")

task2(demodata)


