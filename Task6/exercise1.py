filename = 'numbers.txt'

with open(filename, 'w') as file:
     for i in range(1, 11):
            file.write(f"{i}\n")