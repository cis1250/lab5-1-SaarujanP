
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

#validating and returning user input.
def get_valid_input():
    while True:
        user_input = input("Enter how many terms of the Fibonacci sequence you want: ")
        print(f'User input: "{user_input}"')

        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print('Expected output: "Please enter a positive integer."')
#generating the Fibonacci sequence.
    #Initialize first two Fibonacci numbers
def generate_fibonacci(n):
    a = 0
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a, b = b, a + b

    return output

#printing the sequence.
    #Print the result
def print_fibonacci(sequence):
    print("Expected output:", " ".join(map(str, sequence)))
    
# main function
def main():
    n = get_valid_input()
    fib_sequence = generate_fibonacci(n)
    print_fibonacci(fib_sequence)

#run the program
if __name__ == "__main__":
    main()
