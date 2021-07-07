
#Example 1: Visualizing a stack


stack = list()
# Now that we have our stack initialized, we can start adding instructions to it.

stack.append("A")
stack.append("B")
stack.append("C")

# What's in the stack right now?
print("Current stack:")
print(stack)
print()

# Let's get and display the most recent instruction.
instruction = stack.pop()
print("Most recent instruction:")
print(instruction)
print()

# Let's add another instruction and then display what's currently in the stack.
stack.append("D")
print("Current stack:")
print(stack)
print()

print("Instruction order:")
print(stack.pop()) # first
print(stack.pop()) # second
print(stack.pop()) # third
print()



# Example 2: Using a stack -- Go back!

stack = list()



stack.append("right")
stack.append("down") # This is where we accidentally make a wrong turn...
stack.append("down")
stack.append("right")
stack.append("down")

print(stack)

stack.pop()
stack.pop()
stack.pop()
stack.pop()

print(stack)

stack.append("right")
stack.append("right")
stack.append("right")
stack.append("down")
stack.append("down")

print(stack)

print()

# Example 3: Now You try

stack = []

stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

#while True:

    ## Write code to retrieve and return the next item in the stack.
    # instruction = ?

    #if instruction == ?
    #    pass
    #elif instruction == ?
    #    pass
    #elif instruction == ?
    #    pass
    #elif instruction == ?
    #    pass

    #if stack == []:
    ## Break out of the loop if it's empty. 
    #    break