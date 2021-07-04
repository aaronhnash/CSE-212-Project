# **The Stack**

## Introduction
* [Welcome](welcome.md)
* **Stacks**
  * [Introduction](##introduction)
  * [Using the Stack](#uses)
* [Linked Lists](02-linkedlist.md)
* [Trees](03-tree.md)

### ***What is a stack?***
A stack is at the very basis of how a program *thinks*. When you send your program a set of instructions, it will work through that set from the top down. If you tell the program to do something else before it's gone through everything else, then it will handle whatever is on top of its instruction list first, working its way down the stack.

### ***Visualizing a Stack***
Imagine this. You sit down for breakfast to enjoy a nice breakfast, and you have a big plate of pancakes in front of you. Looks good, right? Well, if you want the freshest pancake, you'll reach for the one on top. And so will everyone else sitting at the table, taking a pancake one by one from the top until there are no more. 

If you'd like a more code-like example, then you're in luck! Lists in Python provide us with an excellent demonstration of how the stack works. Let's initialize our stack as a list and add a few instructions to it. Feel free to follow along in [this sample code](01-stack.py)!
```python
stack = list()
stack.append("A")
stack.append("B")
stack.append("C")
```
So now, we have a stack that looks like this:
```
['A', 'B', 'C']
```
Now that we have our stack with some instructions, let's take a look at what's at the end of the stack and handle it. 
```python
instruction = stack.pop()
print(instruction)
```
Running this code will display the following in our terminal:
```
C
```
Let's say that the computer recieves a new instruction after it handles C. 
```python
stack.append("D")
```
Right now, our stack looks something like this:
```
['A', 'B', 'D']
```
While we might see A as being in the "front", A is actually at the bottom of our stack right now. Retrieving the rest of our stack using the .pop() method as above will return the most recently added item, returning D, then B, then A. 

## <a name="uses"></a> Using the Stack


### ***Keeping organized***
Wait, but how does only handling what was *just* given to you keep you organized? Won’t you forget about everything at the start?

Stacks help you see where you are. How many layers deep are we? 

### **Examples**
“Is this what I want to do?” Code snippet showing a program taking an imaginary “step” forward, testing if a calculation will work. If it does work, then it will advance to the next stage. 

This works because the program handles whatever it was told to do most recently first. [Explain more, but with code]