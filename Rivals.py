"""
------------------- Link for the challenge: https://codeforces.com/problemset/problem/1257/A ----------------------

You are the gym teacher in the school.

There are n students in the row. And there are two rivalling students among them. 
The first one is in position a, the second in position b. Positions are numbered from 1 to n from left to right.

Since they are rivals, you want to maximize the distance between them. If students are in positions p and s respectively, 
then distance between them is |p−s|.

You can do the following operation at most x times: choose two adjacent (neighbouring) students and swap them.

Calculate the maximum distance between two rivalling students after at most x swaps.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of test cases.

The only line of each test case contains four integers n, x, a and b (2 ≤ n ≤ 100, 0 ≤ x ≤ 100, 1 ≤ a,b ≤ n, a ≠ b) — 
the number of students in the row, the number of swaps which you can do, and positions of first and second rivaling students respectively.

Output
For each test case print one integer — the maximum distance between two rivaling students which you can obtain.

Input:
3
5 1 3 2
100 33 100 1
6 0 2 3

Output:
2
99
1
"""
cases = int(input())
for i in range(cases):
    n, x, a, b = map(int, input().split())
    diff1 = abs(a - b) + x
    diff2 = n - 1
    print(min(diff1, diff2))