#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def user_input():
    while True:
        try:
            num_terms = int(input("Enter the number of Fibonacci terms you want: "))
            if num_terms <= 0:
                print("Please enter a positive integer.")
            else:
                return num_terms
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_sequence(sequence):
    print("Fibonacci sequence:")
    print(", ".join(map(str, sequence)))

def main():
    num_terms = user_input()
    sequence = generate_fibonacci(num_terms)
    print_sequence(sequence)

if __name__ == "__main__":
    main()
