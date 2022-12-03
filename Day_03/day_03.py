def get_char_value(char, use_ord=True):
    """
        Get the numeric value of a character.

    This is two different solutions I came up with, to find the numeric value of a character.
    The first solution, using the ord() function, was my initial solution to solving the challenge.
    The second solution, using the ascii_letters string, was a solution I came up with after I had already solved the challenge.
    As I am not doing these challenges to get the best and most efficient code, I am keeping both solutions.
    """
    if use_ord:
        # If the character is lowercase
        if ord(char) >= 97 and ord(char) <= 122:
            return ord(char) - 96
        # If the character is uppercase
        elif ord(char) >= 65 and ord(char) <= 90:
            return ord(char) - 38
    else:
        from string import ascii_letters

        return ascii_letters.index(char) + 1


def solution_1():
    with open("input.txt") as f:
        data = f.readlines()

    items = []
    for line in data:
        line = line.strip()

        compartments = []
        # Split the line into two equal sized parts
        for i in range(0, len(line), len(line)//2):
            compartments.append(line[i:i+len(line)//2])

        #print(compartments)

        # Find the character that appears in both compartments
        for char in compartments[0]:
            if char in compartments[1]:
                items.append(char)
                break
    #print(sorted(items))

    # We loop through all the letters (items) in the compartment, and get the numeric value of each letter.
    values = []
    for item in items:
        values.append(get_char_value(item))

    print(sum(values))

def solution_2():
    with open("input.txt") as f:
        data = f.readlines()

    
    # Split lines into a list of 3 list items
    data = [data[i:i+3] for i in range(0, len(data), 3)]
    #print(data)
     
    items = []
    for group in data:
        # Find the character that appears in all 3 lines
        for char in group[0]:
            if char in group[1] and char in group[2]:
                items.append(char)
                break
    #print(sorted(items))

    # We loop through all the letters (items) in the compartment, and get the numeric value of each letter.
    values = []
    for item in items:
        values.append(get_char_value(item))

    print(sum(values))

def main():
    solution_1()
    solution_2()

if __name__ == "__main__":
    main()