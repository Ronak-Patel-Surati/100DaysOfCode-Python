# A = P (1 + r/n)^t
import math

print("Welcome To Compund Interest Calculator")
principle_amount = int(input("Enter the Principle Amount: "))
rate_of_interest = int(input("Enter the Rate of Interest(%): "))
duration = int(input("Enter the Duration of loan: "))

amount = principle_amount * pow((1 + (rate_of_interest / 100)), duration)
print("Amount Due:", amount)
print("Why was the banker so good at relationships?")
print("Because he knew how to compound interest!")
