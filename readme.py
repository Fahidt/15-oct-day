# Counting books coding challenge

Imagine you are in a library with many floors and many books on each floor. 

The books are not organised.

You are tasked with creating a list of how many unique books there are which start with each letter of the alphabet. 

Some books appear in the library more than once. 

You are told that you can use 10 volunteers to help you speed up the process. 

Write some code (in Python 3) which simulates the approach you would take to this problem.

### Guidelines

- For the sake of saving time - you don't have to code this to run on multiple cpu's
    - But you must be able to demonstrate how each "helpers" information is kept separate and how it would be shared if required

- You shouldn't use any libraries beyond what is built into Python in your solution

### Getting Started

1. Create a `main.py` for your solution
    - You may use other files too if you wish, as long as the whole solution runs by invoking `python3 main.py` 
2. Your solution should end in writing your result to a csv file in `data/output` of the format:

```
character,count
A,1
B,2
C,3
...
```
