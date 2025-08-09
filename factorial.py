#first we make function for factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#enter input
number = int(input("Enter a number: "))
#in factorial we cannot find the factorial of negative value that's why we use conditional statements
if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"Factorial of {number} is {factorial(number)}")
