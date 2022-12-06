def solution_1(length):
    with open("input.txt") as f:
        lines = f.readlines()

    # Do something with the lines
    line = lines[0].strip()
    print(line)

    for i in range(0, len(line)):
        sequence = line[i:i+length]
        # If all characters are unique
        if len(set(sequence)) == len(sequence):
            # Get the position of the last character
            pos = line.index(sequence)+length
            print(pos)
            break

def solution_2():
    pass

def main():
    solution_1(4)
    solution_1(14)

if __name__ == "__main__":
    main()