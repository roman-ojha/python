#  Q) Write a recursive function to calculate the sum of first n natural numbers.

n=int(input("Enter the nth value to find the sum: "))

def recursiveSum(n):
    if n is 0:
        return 0
    else:
        return n+recursiveSum(n-1)

print("The sum of first n natural numbers is:",recursiveSum(n))