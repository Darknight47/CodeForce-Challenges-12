"""
--------------------- Link for the challenge: https://codeforces.com/problemset/problem/1914/A ---------------------

Monocarp is participating in a programming contest, which features 26 problems, named from 'A' to 'Z'. The problems are sorted by difficulty. 
Moreover, it's known that Monocarp can solve problem 'A' in 1 minute, problem 'B' in 2 minutes, ..., problem 'Z' in 26 minutes.

After the contest, you discovered his contest log — a string, consisting of uppercase Latin letters, such that the i-th letter tells which problem Monocarp was solving 
during the i-th minute of the contest. If Monocarp had spent enough time in total on a problem to solve it, he solved it. Note that Monocarp could have been thinking about a problem after solving it.

Given Monocarp's contest log, calculate the number of problems he solved during the contest.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of testcases.

The first line of each testcase contains a single integer n (1 ≤ n ≤ 500) — the duration of the contest, in minutes.

The second line contains a string of length exactly n, consisting only of uppercase Latin letters, — Monocarp's contest log.

Output
For each testcase, print a single integer — the number of problems Monocarp solved during the contest.

Input:
3
6
ACBCBC
7
AAAAFPC
22
FEADBBDFFEDFFFDHHHADCC

Output:
3
1
4
"""
def count_solved_problems(duration, log):
    # Create a dictionary to track time spent on each problem
    problem_time = {}

    for problem in log:
        # Calculate the time required to solve the current problem
        time_required = ord(problem) - ord('A') + 1

        # Accumulate the time spent on the current problem
        if problem in problem_time:
            problem_time[problem] += 1
        else:
            problem_time[problem] = 1

    # Count the number of problems solved
    solved_problems = 0
    for problem, time_spent in problem_time.items():
        time_required = ord(problem) - ord('A') + 1
        if time_spent >= time_required:
            solved_problems += 1

    return solved_problems

cases = int(input())
for i in range(cases):
    print(count_solved_problems(int(input()), input()))