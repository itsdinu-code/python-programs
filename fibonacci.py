# Fibonacci Series Program
# Author: Dinesh H
# BSc CS - Madras University

n = int(input("Enter how many terms: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1