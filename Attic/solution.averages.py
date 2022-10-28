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

def count_increases_from_average_values_in_sequence(the_sequence):
    """
    Given a list or tuple of integers, return the number of times a value in
    the sequence is greater than the average of all values seen so far in the
    sequence.

    All values in the sequence must be integers and be greater than or equal to
    zero.

    Returns an integer.  
    Returns 0 if the sequence is too short.
    Returns None if an error occured and prints the error/exception to stdout.
    """

    
    increases = -1
    previous_value = -1

    sequence_sum = 0
    iterations = 0
    try:
        assert(isinstance(the_sequence, list)
               or isinstance(the_sequence, tuple))

        # The problem isn't valid without at least two values in the set.
        if len(the_sequence) < 2:
            return 0
        
        for this_value in the_sequence:
            assert(isinstance(this_value, int))
            if this_value < 0:
                raise ValueError("No negative values allowed in this function,"
                                 + " next sequence value was: "
                                 + str(this_value))
            
            iterations += 1
            sequence_sum += this_value

            if (sequence_sum / iterations) < this_value:
                increases += 1
            
            previous_value = this_value
    except BaseException as e:
        print("An error occurred in function "
              + "'count_increases_from_average_values_in_sequence': " + str(e))
        print("sequence_sum: " + str(sequence_sum))
        print("iterations: " + str(iterations))
        print("increases: " + str(increases))
        print("previous_value: " + str(previous_value))
        return None

    return increases

def read_integer_list_until_empty_line():
    """
    Collect a list of integers from standard input until an empty line is found.

    Returns a list.
    """
    result_list = []
    for this_line in sys.stdin:
        if len(this_line.rstrip().lstrip()) == 0:
            break
        else:
            try:
                result_list.append(int(this_line))
            except ValueError:
                print("That is not an integer, please re-load and try again.")
                exit()
            except BaseException as e:
                print("An unknown error occurred: " + e)
    return result_list

# Begin program execution if this script is invoked first by the python3 process
if __name__ == '__main__':
    print("Welcome to the modified 'Advent Of Code - Day 1' solution.")
    print("This program will report increases from the sequence average.")
    print("")
    print("Enter an integer and press enter, and continue to do so until there"
          + " are no more integers to input.  Then, press enter one more time"
          + " to begin processing.")
    numbers_list = read_integer_list_until_empty_line()
    print("")
    the_result = count_increases_from_average_values_in_sequence(numbers_list)
    print("Given that sequence, the values increased " + str(the_result)
          + " times from the average sequence value.")
    print("")
    print("Thank you for using the software.")



    
