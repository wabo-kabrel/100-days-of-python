# Debugging Your Code

## 1. Describe the Problem
The first step of solving a problem is to clearly articulate what the issue is.
This involves understanding the expected behavior and comparing it with the actual
behavior of your code. You should then test your assumptions.

## 2. Reproduce the Bug
Some bugs are sneaky, they only occur under certain conditions. In order to debug
them, we need to be able to reliably reproduce the bug and diagnose our problem
to figure out which conditions trigger the bug.

## 3. Play Computer
Playing computer is an important skill in debugging. You need to be able to go through
your code line by line as if you were the computer to help you figure out what is going
wrong.

## 4. Fix the Errors
Fix any errors (red underlines) that show up in the editor before you run you code. The
warnings (yellow) are optional fixes, sometimes it will create a problem down the line,
other times it's fine and the editor just doesn't understand what you're trying to do.

## 5. Make use of the Print Function
The print() function can help you expose hidden values while your code is running. In a
for loop, the loop will follow some rules to perform a repeated block of code. But during
the loop it's difficultto see the intermediate values, which is a perfect example of how 
you can use print() to expose those intermediate values and help you debug your code.

## 6. Use a Debugger
Many IDEs such as PyCharm have inbuilt tools for debugging. This is normally known as the 
debugger. In many ways, they are like print statements on steroids.  
  
Debuggers allows us to peek into our code during execution and pause on chosen lines to figure
out what is the inner mechanism and where it's going wrong.  
  
There are a couple of things that are the same in most IDEs which you should be familiar with:  
  
**i. Breakpoint:** You can set a breakpoint by clicking on a line in the gutter of the code (where
the line numbers are). This line will be where the program pauses during debug run  
  
**ii. Step Over:** This button will go through the execution of your code line by line and allow you
to view the intermediate values of your variables  
    
**iii. Step Into:** This will enter into any other modules that your code references. E.g. if you use
a function from the random module, it will show you the original code for that function so you can
better understand its functionality and how it relates to your problems.  
  
**iv. Step Into My Code:** This does the same thing as Step Into, but it limits the scope to your own
project code and ignores library code such as random