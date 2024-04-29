# Weekly Tasks

## Table of Contents
- [Weekly Tasks](#weekly-tasks)
  - [Table of Contents](#table-of-contents)
  - [Overview ](#overview-)
  - [Week Two Task ](#week-two-task-)
  - [Week Three Task ](#week-three-task-)
  - [Week Four Task ](#week-four-task-)
  - [Week Five Task ](#week-five-task-)
  - [Week Six Task ](#week-six-task-)
  - [Week Seven Task ](#week-seven-task-)
  - [Week Eight Task ](#week-eight-task-)
  - [Contributors ](#contributors-)
  - [License ](#license-)

## Overview <a name=overview>
Every week a new task will be put into the weekly tasks on the VLE. Your solutions will be assessed towards the end of the semester and will be worth 50% of your marks for this module. The marking scheme is given below. It is expected that you will be working on the exercises throughout the semester. It is not expected that you get every program right first time. So long as an attempt is made the week the problem is posted, this will count as a good approach. It is important that you keep working on any incomplete problems until the deadline. Please note that all students are bound by the Quality Framework [3] at GMIT which includes the Code of Student Conduct and the Policy on Plagiarism. The onus is on the student to ensure they do not, even inadvertently, break the rules. A clean and comprehensive git [1] history (see below) is the best way to demonstrate that your submission is your own work. It is, however, expected that you draw on works that are not your own and you should systematically reference those works to enhance your submission. 

## Week Two Task <a name=two>
**Background**<br>
When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
**Program Name** <br>
bank.ipynb
**Program Outline**
The program should:
1. Prompt the user and read in two money amounts (in cent)
2. Add the two amounts
3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
**Example**
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45
**Advice**
There is a bit in this, break it down into smaller parts, for example read in an integer first, (and print it back out again, then do some arithmetic to it and print, then read in a second one and add the two, and only then look at the formatting of the answer. of course there are many ways of doing this.
**References**

## Week Three Task <a name=three>
**Background**<br>
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs). 
**Program Name** <br>
accounts.py
**Program Outline**
The program should:
*Read in a 10 character account number and output the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).*
**Example**
Please enter an 10 digit account number: 1234567890
XXXXXX7890
**Extra**
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
**References**

## Week Four Task <a name=four>
**Background**<br>
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
**Program Name** <br>
collatz.py
**Program Outline**
The program should:
1.Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
1.At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
1.Have the program end if the current value is one.
**Example**
Please enter a positive integer: 10
10 5 16 8 4 2 1
**References**

## Week Five Task <a name=five>
**Background**<br>
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
**Program Name** <br>
weekday.py
**Program Outline**
The program should:
1.If its a weekday return: *Yes, unfortunately today is a weekday.*
1.If its the weekend return: *It is the weekend, yay!*
**Example**
An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!

**References**

## Week Six Task <a name=six>
**Background**<br>
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this. I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots.This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.
**Program Name** <br>
squareroot.ipynb
**Program Outline**
The program should:
1. Takes a positive floating-point number as input and output an approximation of its square root.
2. Use Newtons Square Root.

**Example**
python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

**References**

## Week Seven Task <a name=seven>
**Background**<br>
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
**Program Name** <br>
counter.py
**Program Outline**
The program should:
1. Take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
**Example**
python es.py moby-dick.txt
116960
**Assumptions**
There is a bit in this, break it down into smaller parts, for example read in an integer first, (and print it back out again, then do some arithmetic to it and print, then read in a second one and add the two, and only then look at the formatting of the answer. of course there are many ways of doing this.
**References**

## Week Eight Task <a name=eight>
**Background**<br>
Write a program called plottask.py that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.. 
**Program Name** <br>
plottask.py
**Program Outline**
The program should:
1. displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2.
2. Plot of the function  h(x)=x3 in the range 0 to 10.
3. On one set of axes.

**References**



## Contributors <a name=contributors>
- [Barry Egan]([GitHub URL](https://github.com/FDEgan))

## License <a name=license>

Distributed under the MIT License. Please click on below for more information on usage.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
