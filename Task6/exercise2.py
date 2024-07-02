filename = "input.txt"
with open(filename, 'a') as file:
        while True:
            user_input = input("Enter something (type 'stop' to end): ")
            if user_input.lower() == 'stop':
                print("Stopping input.")
                break
            else:
                file.write(user_input + '\n')
    
print(f"Input has been written to {filename}")