#!/usr/bin/env python3
#
# Copyright 2022 ultasun, all rights reserved.  See the LICENSE file.
#
# See the original challenge prompt: https://adventofcode.com/2021/day/1
#
# Given a list of integers, return an integer representing the number of times
# a value in the sequence increased from the previous sequence.
#

import sys
from solution import count_increases_from_previous_values_in_sequence
from solution import read_integer_list_until_empty_line

# Begin program execution if this script is invoked first by the python3 process
if __name__ == '__main__':
    # Find `window` size argument, if present
    window = 3
    if len(sys.argv) > 1:
        try:
            window = int(sys.argv[1])
        except:
            pass

    # Greet and instruct the user
    print("Welcome to an 'Advent of Code 2021 - Day 1, Part 2' solution.")
    print("")
    print("Enter an integer and press enter, and continue to do so until there"
          + " are no more integers to input.  Then, press enter one more time"
          + " to begin processing.")
    numbers_list = read_integer_list_until_empty_line()
    print("")

    # Do the calculation
    the_result = \
        count_increases_from_previous_values_in_sequence(numbers_list, window)

    # Print the result and exit
    print("Given that sequence, the values increased " + str(the_result)
          + " times from the previous value.")
    print("The window sized used to perform the calculation was "
          + str(window) + ".")
    print("")
    print("Thank you for using the software.")
