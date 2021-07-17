# Stack Example 1 Key

stack = []

stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

# We look at the possible instructions and define what we should do when we read that instruction.

while True:
    # Get the instruction
    instruction = stack.pop()
    # What do we do with it?
    if instruction == "D":
        number_1 = int(input("1st Number: "))
    elif instruction == "C":
        number_2 = int(input("2nd Number: "))
    elif instruction == "B":
        product = number_1 * number_2
    elif instruction == "A":
        print(f"Product: {product}")
        
    if stack == []:
        break

print()

# Example 2: Functions within Functions answer key

# Remember: the order we want the functions to execute in is A, D, B, C, E. Since we know we start with E, let's make E call C, and on and on.

def functionA():
    # Since A has no functions after it, you don't have to call anymore functions.
    print("Function A")

def functionB():
    functionD()

    print("Function B")

def functionC():
    functionB()
    
    print("Function C")

def functionD():
    functionA()

    print("Function D")

def functionE():
    functionC()

    print("Function E")

functionE()