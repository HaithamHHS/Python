range_50 = range(1 , 51)

def Fizz_Buzz(range):
    for num in range:
        if num%3==0 and num%5==0:
            print(f"FizzBuzz and number is {num}")
            continue
        elif num%5==0:
            print(f"Buzz")
            continue
        elif num%3==0:
            print(f"Fizz")

Fizz_Buzz(range_50)