"""
------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1985/B ----------------------------------

Given an integer n, find an integer x such that:

2 ≤ x ≤ n.
The sum of multiples of x that are less than or equal to n is maximized. Formally, x+2x+3x+⋯+kx where kx≤n is maximized over all possible values of x.

Input
The first line contains t (1 ≤ t ≤ 100) — the number of test cases.

Each test case contains a single integer n (2 ≤ n ≤ 100).

Output
For each test case, output an integer, the optimal value of x. It can be shown there is only one unique answer.

Input:
2
3
15

Output:
3
2
"""
cases = int(input())
for i in range(cases):
    num = int(input())
    if(num == 3):
        print(3)
    else:
        print(2)