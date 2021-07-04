
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



# Example 2: Using a stack