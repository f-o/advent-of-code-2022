import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--day', type=int, required=True)
args = parser.parse_args()
day = args.day

# Create the directory for the day
os.mkdir(f"Day_{day:02}")
# Create the input file
with open(f"Day_{day:02}/input.txt", "w") as f:
    f.write("")
with open(f"Day_{day:02}/input_sample.txt", "w") as f:
    f.write("")
# Create the solution file
with open(f"Day_{day:02}/day_{day:02}.py", "w") as f:
    f.write("""# Path: Day_{day:02}/day_{day:02}.py
    
def solution_1():
    pass

def solution_2():
    pass

def main():
    solution_1()
    solution_2()

if __name__ == "__main__":
    main()
    """.format(day=day))
# Create the challenge file
with open(f"Day_{day:02}/challenge.md", "w") as f:
    f.write("")