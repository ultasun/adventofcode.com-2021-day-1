# Sonar Sweep
This repository will contain a unique solution to the challenge presented [here](https://adventofcode.com/2021/day/1).  The language used will be [Python 3](https://docs.python.org/3/).

# Assumptions
1. The sequence always contains integers,
2. An integer in the sequence will never be less than `0`,
3. The sequence contains at least two integers.

# Solution
The solution is simple:
1. Have two integer variables both initialized to `-1`,
2. Iterate over the sequence with a *for each* loop,
  - If `this_value` is larger than the `previous_value`, then increment `increases`,
  - Set `previous_value` to equal `this_value`.
3. Return the `increases` integer as the result.

# Fault tolerance
1. If the sequence is too small, then `0` will be returned.
2. If the sequence contains anything other than integers, than `None` will be returned.

# Code and Tests
The code is in [`solution.py`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/solution.py), and some `unittest`s are in [`tests.py`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/tests.py).

# Example
```
root@d60890761729:/src/ultasun/adventofcode.com-2021-day-1# python3 ./solution.py
Welcome to an 'Advent of Code 2021 - Day 1' solution.

Enter an integer and press enter, and continue to do so until there are no more integers to input.  Then, press enter one more time to begin processing.
199
200
208
210
200
207
240
269
260
263


Given that sequence, the values increased 7 times from the previous value.

Thank you for using the software.
root@d60890761729:/src/ultasun/adventofcode.com-2021-day-1# 
```

# Credits
See the `LICENSE`.  The code in this repository is the original work of the repository owner.  The challenge problem is from [Advent of Code](https://adventofcode.com/).

If there turns out to be an issue in this solution, open an issue in this repository's issue tracker.

Thanks for reading.
