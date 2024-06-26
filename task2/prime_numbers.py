number = int(input("Kindly enter a number to get the Primes number below it :  "))
lower = 2
upper = number
def prime_list(n : int):
    for num in range(lower, upper ):
   # all prime numbers are greater than 1 , so we start with 2 
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


prime_list(number)