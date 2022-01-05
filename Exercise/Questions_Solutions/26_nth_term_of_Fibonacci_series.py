# Q) Write a function to print the nth term of the Fibonacci series using recursion.

n=int(input("Enter the nth term:"))

def nthFibonacci(n,ft,st):
    tt=ft+st
    if(n<0):
        print("Invalid number, Plese Try again !!!")
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return tt
    else:
        return nthFibonacci(n-1,st,tt)

    
print("nth fibonacci series is:",nthFibonacci(n,0,1))