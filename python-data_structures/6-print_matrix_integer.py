#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print the integer using str.format()
            print("{:d}".format(row[i]), end="")
            # Print a space ONLY if it's not the last element in the row
            if i < len(row) - 1:
                print(" ", end="")
        # After finishing a row, print a new line
        print()
