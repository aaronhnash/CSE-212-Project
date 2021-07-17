
# Visualizing a stack


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



# Using a stack -- Go back!

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

# Example 1: Now You try

stack = []

stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

#while True: # uncomment all of this once you've started workeing on the problem!

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

# Example 2: Functions within Functions

def functionA():
    # call another function here!
    # YOUR CODE HERE

    print("Function A")

def functionB():
    # YOUR CODE HERE

    print("Function B")

def functionC():
    # YOUR CODE HERE
    
    print("Function C")

def functionD():
    # YOUR CODE HERE

    print("Function D")

def functionE():
    # YOUR CODE HERE

    print("Function E")

functionE()