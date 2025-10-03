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
