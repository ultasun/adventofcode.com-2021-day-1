# Sonar Sweep for Python 3
This repository will contain a unique solution to the *Advent of Code: 2021 Day 1* challenge presented [here](https://adventofcode.com/2021/day/1).  The language used will be [Python 3](https://docs.python.org/3/).

# Solution
This section is an *English* explanation of the solution.  Several variable names used in the script are used in this explanation.

### Assumptions
The original problem is not very specific, so the following assumptions were made by the author:
1. The sequence contains only integers,
2. An integer in the sequence will never be less than `0`,
3. The sequence contains at least *one plus the window size* integers.

### Solution: Part 1
The [solution](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/Attic/solution.old.py) is simple:
1. Have two integer variables both initialized to `-1`,
2. Iterate over the sequence with a *for each* loop,
  - If `this_value` is larger than the `previous_value`, then increment `increases`.
  - Set `previous_value` to equal `this_value`.
3. Return the `increases` integer as the result.

### Solution: Part 2
Quick reflection shows that *Part 1* is the same as *Part 2*, with the *window size* set to `1` -- so the function may be modified to remain backwards compatible.

The [solution](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/solution.py):
1. Modify the function from *Part 1* to accept a second argument: the `window` size.
2. Discard the *for each* loop over the sequence.  Instead, iterate over an integer range, starting from `0` and stopping before *the difference between the sequence length, and the window size minus 1* -- this will be called `this_frame_index`.
  - In each iteration, a nested iteration occurs over an integer range, starting from `0` and stopping before the `window` size -- this will be called `this_window_index`.
    - In each iteration, accumulate (sum) a subsequence of integers in the sequence, starting at the location indexed by `this_frame_index` plus `this_window_index` -- this is the *sliding window*.  Store the accumulation in `window_sum`.
  - After the nested iteration, if `window_sum` (which is analogous to `this_value` from *Part 1*) is larger than the `previous_value`, then increment `increases`.
  - Set `previous_value` to equal `window_sum` (which is analogous to `this_value` from *Part 1*).
3. Return the `increases` integer as the result.

# Code, Testing, Usage and Demonstration
The code is in [`solution.py`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/solution.py), and a [`unittest`](https://docs.python.org/3/library/unittest.html) with six tests are in [`tests.py`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/tests.py).

### Usage
Run `chmod +x solution.py` to make sure it is executable, if desired.
The only argument is an integer to specify the `window` size.
The default `window` size is `1`, and the default `window` size for `solution_part2.py` is `3`. 
```
usage: solution.py <window_size>
```
Pipe a `case1.txt` or `case2.txt` in if so desired:
```
$ cat case2.txt | ./solution.py 3
.
.
.
Given that sequence, the values increased 1571 times from the previous value.
The window sized used to perform the calculation was 3.
```

### Fault Tolerance
1. If the sequence is too small, then `0` will be returned.
2. If the sequence contains invalid data, then `None` will be returned.

##### Why two scripts
A convenience script has been provided, [`solution_part2.py`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/solution_part2.py) -- it will import everything from [`solution.py`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/solution.py), the only difference being the default `window` size is `3`, and the `print` messages will notify the user that the script is intended to solve *Part 2* sequences.

[The convenience script](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/solution_part2.py) is not used in any of the following examples.  Instead, the `window` size is adjusted in the following examples by providing a `3` as a command-line argument to the `python3` process.

##### Simple solution for *Part 1* only
The original code written prior to *Part 2* is found in [`Attic/solution.old.py`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/Attic/solution.old.py).

### Part 1: Demo
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

The much longer *Advent Of Code: Day 1, Part 1* example may be seen [here](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/demo_part1.txt), the correct answer is `1532`.

### Part 2: Demo
```
root@d60890761729:/src/ultasun/adventofcode.com-2021-day-1# python3 ./solution.py 3
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


Given that sequence, the values increased 5 times from the previous value.
The window sized used to perform the calculation was 3.

Thank you for using the software.
root@d60890761729:/src/ultasun/adventofcode.com-2021-day-1#
```

The much longer *Advent Of Code: Day 1, Part 2* example may be seen [here](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/demo_part2.txt), the correct answer is `1571`.

# Credits
See the [`LICENSE`](https://github.com/ultasun/adventofcode.com-2021-day-1/blob/main/LICENSE).  The code in this repository is the original work of the repository owner.  The challenge problem is written by [*Eric Wastl*](http://was.tl) from [Advent of Code](https://adventofcode.com/) and may be subject to copyrights specified there.

If there turns out to be an issue in this solution, open an issue in this repository's issue tracker.

Thanks for reading.
