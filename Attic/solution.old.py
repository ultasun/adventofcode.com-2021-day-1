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

def count_increases_from_previous_values_in_sequence(the_sequence):
    """
    Given a list or tuple of integers, return the number of times a value in
    the sequence is greater than the previous value.

    Returns an integer.
    """
    assert(isinstance(the_sequence, list) or isinstance(the_sequence, tuple))

    # The problem isn't valid without at least two values in the set.
    if len(the_sequence) < 2:
        return 0
    
    increases = -1
    previous_value = -1
    average_so_far = 0
    total_sum_so_far = 0
    iterations_so_far = 0
    try:
        for this_value in the_sequence:
            if not isinstance(this_value, int):
                print("invalide value: not an integer")
                return None

            # assumption 1: make sure this_value is greater than zero
            if not this_value > 0:
                print("invalid value: less than zero")
                return None
            
            iterations_so_far += 1
            total_sum_so_far += this_value
            
            #if this_value > previous_value:
            #    increases += 1

            if (total_sum_so_far / iterations_so_far) < this_value:
                increases += 1
            
            previous_value = this_value

            # print out values
            print("iterations_so_far: " + str(iterations_so_far))
            print("total_sum_so_far: " + str(total_sum_so_far))
            print("increases: " + str(increases))
            print("previous_value: " + str(previous_value))

    except BaseException as e:
        print("An error occurred: " + str(e))
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
    print("Welcome to an 'Advent of Code 2021 - Day 1' solution.")
    print("")
    print("Enter an integer and press enter, and continue to do so until there"
          + " are no more integers to input.  Then, press enter one more time"
          + " to begin processing.")
    numbers_list = read_integer_list_until_empty_line()
    print("")
    the_result = count_increases_from_previous_values_in_sequence(numbers_list)
    print("Given that sequence, the values increased " + str(the_result)
          + " times from the previous value.")
    print("")
    print("Thank you for using the software.")



    
