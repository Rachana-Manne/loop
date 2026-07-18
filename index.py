# Conditional Statements Practice - Comprehensive Assignment

# 1. Check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Even or Odd
num = int(input("\nEnter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# 3. Voting eligibility
age = int(input("\nEnter age: "))
print("Eligible to vote" if age >= 18 else "Not eligible to vote")

# 4. Greater of two numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("Greater number is:", a if a > b else b)

# 5. Divisible by 5
num = int(input("\nEnter a number: "))
print("Divisible by 5" if num % 5 == 0 else "Not divisible by 5")

# 6. Multiple of 3
num = int(input("\nEnter a number: "))
print("Multiple of 3" if num % 3 == 0 else "Not multiple of 3")

# 7. Vowel or consonant
ch = input("\nEnter a character: ").lower()
if ch in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")

# 8. Greater than 100
num = int(input("\nEnter a number: "))
print("Greater than 100" if num > 100 else "Not greater than 100")

# 9. Leap year
year = int(input("\nEnter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

# 10. Temperature Hot/Cold
temp = float(input("\nEnter temperature: "))
print("Hot" if temp > 30 else "Cold")

# 11. Marks and Grade
marks = int(input("\nEnter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"
print("Grade:", grade)

# 12. Simple Calculator
x = float(input("\nEnter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result:", x + y)
elif op == "-":
    print("Result:", x - y)
elif op == "*":
    print("Result:", x * y)
elif op == "/":
    print("Result:", x / y if y != 0 else "Error: Division by zero")
else:
    print("Invalid operator")

# 13. FizzBuzz
num = int(input("\nEnter a number: "))
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
if salary < 250000:
    tax = 0
elif salary <= 500000:
    tax = 5
elif salary <= 1000000:
    tax = 20
else:
    tax = 30
print("Tax percentage:", tax, "%")

# 16. Largest of three numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print("Largest number:", largest)

# 17. Login system
username = input("\nEnter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

# 18. Positive then even/odd
num = int(input("\nEnter a number: "))
if num > 0:
    print("Positive")
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Not positive")

# 19. ATM withdrawal
balance = 10000
withdraw = int(input("\nEnter withdrawal amount: "))
if withdraw <= balance:
    if withdraw <= 5000:
        balance -= withdraw
        print("Transaction successful. Remaining balance:", balance)
    else:
        print("Withdrawal limit exceeded (max 5000).")
else:
    print("Insufficient balance.")

# 20. Student result
marks = int(input("\nEnter marks: "))
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
print("3-digit number" if 100 <= num <= 999 else "Not a 3-digit number")

# 22. Valid triangle
a = int(input("\nEnter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))
print("Valid triangle" if a + b + c == 180 else "Not a valid triangle")

# 23. Second largest of three
nums = [int(input("\nEnter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))]
nums.sort()
print("Second largest:", nums[1])

# 24. Alphabet check
ch = input("\nEnter a character: ")
if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("Alphabet")
else:
    print("Not an alphabet")

# 25. Electricity bill
units = int(input("\nEnter units consumed: "))
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10
print("Electricity bill:", bill)

# 26. Movie ticket pricing
age = int(input("\nEnter age: "))
if age < 12:
    print("Child ticket")
elif age > 60:
    print("Senior ticket")
else:
    print("Adult ticket")

# 27. Login system with 3 attempts
for attempt in range(3):
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        print("Login failed")
else:
    print("Maximum attempts reached")

# 28. Palindrome check
num = input("\nEnter a number: ")
print("Palindrome" if num == num[::-1] else "Not palindrome")

# 29. Shopping discount
amount = float(input("\nEnter shopping amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10
else:
    discount = 0
print("Discount:", discount)

# 30. Traffic signal system
signal = input("\nEnter traffic signal color (Red/Yellow/Green): ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready to go")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")
