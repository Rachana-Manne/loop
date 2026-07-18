# Conditional Statements Practice using only for loops

# 1. Positive, Negative, Zero
num = int(input("Enter a number: "))
for _ in range(1):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# 2. Even or Odd
num = int(input("\nEnter a number: "))
for _ in range(1):
    print("Even" if num % 2 == 0 else "Odd")

# 3. Voting eligibility
age = int(input("\nEnter age: "))
for _ in range(1):
    print("Eligible to vote" if age >= 18 else "Not eligible")

# 4. Greater of two numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
for _ in range(1):
    print("Greater:", a if a > b else b)

# 5. Divisible by 5
num = int(input("\nEnter a number: "))
for _ in range(1):
    print("Divisible by 5" if num % 5 == 0 else "Not divisible by 5")

# 6. Multiple of 3
num = int(input("\nEnter a number: "))
for _ in range(1):
    print("Multiple of 3" if num % 3 == 0 else "Not multiple of 3")

# 7. Vowel or consonant
ch = input("\nEnter a character: ").lower()
for _ in range(1):
    if ch in "aeiou":
        print("Vowel")
    elif 'a' <= ch <= 'z':
        print("Consonant")
    else:
        print("Not an alphabet")

# 8. Greater than 100
num = int(input("\nEnter a number: "))
for _ in range(1):
    print("Greater than 100" if num > 100 else "Not greater than 100")

# 9. Leap year
year = int(input("\nEnter a year: "))
for _ in range(1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not leap year")

# 10. Temperature Hot/Cold
temp = float(input("\nEnter temperature: "))
for _ in range(1):
    print("Hot" if temp > 30 else "Cold")

# 11. Marks and Grade
marks = int(input("\nEnter marks: "))
for _ in range(1):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")

# 12. Simple Calculator
x = float(input("\nEnter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")
for _ in range(1):
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y if y != 0 else "Error: Division by zero")

# 13. FizzBuzz
num = int(input("\nEnter a number: "))
for _ in range(1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 14. Character type
ch = input("\nEnter a character: ")
for _ in range(1):
    if ch.isupper():
        print("Uppercase")
    elif ch.islower():
        print("Lowercase")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")

# 15. Salary tax percentage
salary = float(input("\nEnter salary: "))
for _ in range(1):
    if salary < 250000:
        print("No tax")
    elif salary <= 500000:
        print("5% tax")
    elif salary <= 1000000:
        print("20% tax")
    else:
        print("30% tax")

# 16. Largest of three numbers
a = int(input("\nEnter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
for _ in range(1):
    if a > b:
        if a > c:
            print("Largest:", a)
        else:
            print("Largest:", c)
    else:
        if b > c:
            print("Largest:", b)
        else:
            print("Largest:", c)

# 17. Login system
u = input("\nEnter username: ")
p = input("Enter password: ")
for _ in range(1):
    print("Login success" if u == "admin" and p == "1234" else "Login failed")

# 18. Positive then even/odd
num = int(input("\nEnter a number: "))
for _ in range(1):
    if num > 0:
        print("Positive")
        print("Even" if num % 2 == 0 else "Odd")
    else:
        print("Not positive")

# 19. ATM withdrawal
balance = 10000
withdraw = int(input("\nEnter withdrawal amount: "))
for _ in range(1):
    if withdraw <= balance:
        if withdraw <= 5000:
            balance -= withdraw
            print("Transaction successful. Balance:", balance)
        else:
            print("Withdrawal limit exceeded")
    else:
        print("Insufficient balance")

# 20. Student result
marks = int(input("\nEnter marks: "))
for _ in range(1):
    if marks >= 35:
        print("Pass")
        if marks >= 75:
            print("Distinction")
        elif marks >= 60:
            print("First Class")
    else:
        print("Fail")

# 21. 3-digit number
num = int(input("\nEnter a number: "))
for _ in range(1):
    print("3-digit" if 100 <= num <= 999 else "Not 3-digit")

# 22. Valid triangle
a = int(input("\nEnter angle1: "))
b = int(input("Enter angle2: "))
c = int(input("Enter angle3: "))
for _ in range(1):
    print("Valid triangle" if a + b + c == 180 else "Not valid")

# 23. Second largest of three
nums = [int(input("\nEnter first: ")), int(input("Enter second: ")), int(input("Enter third: "))]
for _ in range(1):
    nums.sort()
    print("Second largest:", nums[1])

# 24. Alphabet check
ch = input("\nEnter a character: ")
for _ in range(1):
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        print("Alphabet")
    else:
        print("Not alphabet")

# 25. Electricity bill
units = int(input("\nEnter units: "))
for _ in range(1):
    if units <= 100:
        bill = 0
    elif units <= 200:
        bill = (units - 100) * 5
    else:
        bill = (100 * 5) + (units - 200) * 10
    print("Bill:", bill)

# 26. Movie ticket pricing
age = int(input("\nEnter age: "))
for _ in range(1):
    if age < 12:
        print("Child ticket")
    elif age > 60:
        print("Senior ticket")
    else:
        print("Adult ticket")

# 27. Login system with 3 attempts
for attempt in range(3):
    u = input("\nEnter username: ")
    p = input("Enter password: ")
    if u == "admin" and p == "1234":
        print("Login success")
        break
    else:
        print("Login failed")
else:
    print("Max attempts reached")

# 28. Palindrome check
num = input("\nEnter a number: ")
for _ in range(1):
    print("Palindrome" if num == num[::-1] else "Not palindrome")

# 29. Shopping discount
amt = float(input("\nEnter shopping amount: "))
for _ in range(1):
    if amt >= 5000:
        print("Discount:", amt * 0.20)
    elif amt > 2000:
        print("Discount:", amt * 0.10)
    else:
        print("No discount")

# 30. Traffic signal system
signal = input("\nEnter signal color: ").lower()
for _ in range(1):
    if signal == "red":
        print("Stop")
    elif signal == "yellow":
        print("Ready to go")
    elif signal == "green":
        print("Go")
    else:
        print("Invalid signal")
