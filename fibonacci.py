#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

#Prompt the user
user_input = input("Enter how many terms of the Fibonacci sequence you want: ")

#Print the user input
print(f'User input: "{user_input}"')

#Validate input
if user_input.isdigit() and int(user_input) > 0:
    n = int(user_input)

    #Initialize first two Fibonacci numbers
    a = 0
    b = 1
    output = []

    #Generate Fibonacci sequence
    for i in range(n):
        output.append(str(a))
        a, b = b, a + b

    #Print the result
    print("Expected output:", " ".join(output))
else:
    #Print invalid input
    print('Expected output: "Please enter a positive integer."')

# your code is supposed to reprompt the user for input when they enter a wrong one instead of exiting the program -1
