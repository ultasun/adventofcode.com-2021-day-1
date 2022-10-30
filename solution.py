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

def count_increases_from_previous_values_in_sequence(the_sequence, window=1):
    """
    Given a list or tuple of integers, return the number of times a value in
    the sequence is greater than the previous value.

    An optional 'window' size can be specified in order to accomodate 'Part 2'
    of the problem -- this will consider differences in subsequence summations,
    instead of single values.

    Returns an integer.
    """    
    increases = -1
    previous_value = -1
    try:
        assert(isinstance(the_sequence, list)
               or isinstance(the_sequence, tuple))

        # The problem isn't valid without at least `window` values in the set
        if len(the_sequence) < (window + 1):
            return 0
        
        for this_frame_index in range(0, (len(the_sequence) - (window - 1))):
            window_sum = 0
            for this_window_index in range(0, window):
                this_integer = \
                    the_sequence[this_frame_index + this_window_index]
                assert(isinstance(this_integer, int))
                if this_integer <= 0:
                    raise ValueError("No negative values allowed in this"
                                     + " function, next sequence value was: "
                                     + str(this_value))
                window_sum += this_integer
            if window_sum > previous_value:
                increases += 1
            previous_value = window_sum
    except BaseException as e:
        print("An error occurred in function "
              + "'count_increases_from_previous_value_in_sequence':" + str(e))
        print("previous_value: " + str(previous_value))
        print("increases: " + str(increases))
        
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
    # Find `window` size argument, if present
    window = 1
    if len(sys.argv) > 1:
        try:
            window = int(sys.argv[1])
        except:
            pass

    # Greet and instruct the user
    print("Welcome to an 'Advent of Code 2021 - Day 1' solution.")
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
