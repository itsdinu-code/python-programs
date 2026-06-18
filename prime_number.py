# Prime Number Check Program
# Author: Dinesh H
# BSc CS - Madras University

n = int(input("Enter a number: "))

if n < 2:
    print(n, "is NOT a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a PRIME number")
    else:
        print(n, "is NOT a prime number")