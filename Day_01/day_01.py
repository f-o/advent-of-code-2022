def solution_1():
    elves, elf = [], []
    with open('input.txt') as f:
        # Loop through each line in the file
        # Add the line to the elf array
        # If the line is empty, add the elf list to the elves list
        for line in f:
            if line.strip() == '':
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line.strip()))
        elves.append(elf)
    print(elves)

    # Find the max sum of the elves
    max_sum = 0
    for elf in elves:
        # Find the total sum of the elf
        total_sum = sum(elf)
        # If the total sum is greater than the max sum, update the max sum
        if total_sum > max_sum:
            max_sum = total_sum
    print(max_sum)
    
    
def solution_2():
    elves, elf = [], []
    with open('input.txt') as f:
        # Loop through each line in the file
        # Add the line to the elf array
        # If the line is empty, add the elf list to the elves list
        for line in f:
            if line.strip() == '':
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line.strip()))
        elves.append(elf)
    print(elves)
    
    # Find the max sum of the top three elves
    max_sum = []
    for elf in elves:
        # Find the total sum of the elf
        total_sum = sum(elf)
        # If the total sum is greater than the max sum, update the max sum
        if len(max_sum) < 3:
            max_sum.append(total_sum)
        elif total_sum > min(max_sum):
            max_sum.remove(min(max_sum))
            max_sum.append(total_sum)
    print(sorted(max_sum, reverse=True))
    print(sum(max_sum))

    

def main():
    solution_1()
    solution_2()

if __name__ == "__main__":
    main()