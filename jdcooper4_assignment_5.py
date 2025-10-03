print("=== Challenge 1: Collatz Conjecture ===")
num = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", num, end=" ")

while num > 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3) + 1
    print(num, end=" ")
    step_count +=1
print("")
print(f"Steps: {step_count}")
print("")
print("=== Challenge 2: Prime Number Checker ===")
number = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {number - 1}...")
for i in range(2, number -1):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        break
else:
    print(f"{number} is prime!")
print("")
