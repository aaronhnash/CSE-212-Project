# Stack Example 3 Key

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