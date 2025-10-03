# COMP163 Assignment 5

This repository contains solutions for three challenges using Python loops.

---

## Challenge 1: Collatz Conjecture

**Loop Type:** `while` loop for unknown iterations  

**Reason for Choice:**  
The number of steps in the Collatz sequence is not known in advance. A `while` loop is ideal for repeating an operation until a condition (`num > 1`) is no longer true.  

**How It Works:**  
- The program takes a starting number from the user.  
- While the number is greater than 1, it repeatedly applies the Collatz rules:  
  - If even, divide by 2.  
  - If odd, multiply by 3 and add 1.  
- Each step is printed, and a counter tracks the number of steps until the sequence reaches 1.  

**AI Assistance:**  
AI was used to review and optimize the sequence printing and step-counting logic for clarity and readability.

---

## Challenge 2: Prime Number Checker

**Loop Type:** `for` loop for a known range  

**Reason for Choice:**  
When checking if a number is prime, the divisors to test are known: 2 through `number - 1`. A `for` loop efficiently iterates over this fixed range.  

**How It Works:**  
- The user inputs a number.  
- The program tests divisibility for all integers from 2 up to `number - 1`.  
- If any divisor evenly divides the number, it is declared not prime, and the loop breaks.  
- If no divisors divide the number, the `else` clause confirms it is prime.  

**AI Assistance:**  
AI helped with structuring the loop and adding informative print statements to show which divisor caused a number to fail the primality test.

---

## Challenge 3: Multiplication Table

**Loop Type:** Nested `for` loops for 2D data  

**Reason for Choice:**  
A multiplication table requires iterating over rows and columns, making nested `for` loops the natural choice for structured 2D output.  

**How It Works:**  
- A list of numbers from 1 to 10 represents both rows and columns.  
- The outer loop iterates over rows, while the inner loop iterates over columns.  
- Each product is calculated and printed in a formatted table.  

**AI Assistance:**  
AI was used to improve table formatting for alignment and readability, ensuring consistent spacing for all numbers in the 10x10 table.


---


**AI Assistance:**  
AI was used to assist with the README to improve readability and overall presentation in the writing. 
AI was used to assist with comments to help with professional language and overall improve the makeup of the code.
