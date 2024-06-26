def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)    


def list_factorial(my_list):
    for i in my_list:
        if i==1:
            print(i)
        else:
            fact =  i * factorial(i-1)
            print(fact)
       
list_factorial([2,3,4,5])