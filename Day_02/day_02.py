values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}
win_values = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}

def solution_1():
    with open("input.txt") as h:
        games = h.readlines()

    total_sum = 0
    for game in games:
        game = game.strip().split(" ")
        result = win_values[game[0] + game[1]]
        total_sum += result + values[game[1]]

    print(total_sum)

def solution_2():
    with open("input.txt") as h:
        games = h.readlines()

    total_sum = 0
    for game in games:
        game = game.strip().split(" ")
        if game[1] == "X":
            # Find the key that has the same first letter as game[0] and the value of 0
            for key, value in win_values.items():
                if key[0] == game[0] and value == 0:
                    total_sum += values[key[1]]
                    break
        elif game[1] == "Y":
            # Find the key that has the same first letter as game[0] and the value of 3
            for key, value in win_values.items():
                if key[0] == game[0] and value == 3:
                    total_sum += values[key[1]] + 3
                    break
        elif game[1] == "Z":
            # Find the key that has the same first letter as game[0] and the value of 6
            for key, value in win_values.items():
                if key[0] == game[0] and value == 6:
                    total_sum += values[key[1]] + 6
                    break
    print(total_sum)

        
def main():
    solution_1()
    solution_2()

if __name__ == "__main__":
    main()