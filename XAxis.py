"""
-------------------- Link for the challenge: https://codeforces.com/problemset/problem/1986/A ----------------------

You are given three points with integer coordinates x1, x2, and x3 on the X axis (1 ≤ x(i) ≤ 10). You can choose any point with an integer coordinate a on the X axis. 
Note that the point a may coincide with x1, x2, or x3. Let f(a) be the total distance from the given points to the point a. Find the smallest value of f(a).

The distance between points a and b is equal to |a−b|. For example, the distance between points a=5 and b=2 is 3.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. Then follows their descriptions.

The single line of each test case contains three integers x1, x2, and x3 (1 ≤ x(i) ≤ 10) — the coordinates of the points.

Output
For each test case, output the smallest value of f(a).

Input:
8
1 1 1
1 5 9
8 2 8
10 9 3
2 1 1
2 4 1
7 3 5
1 9 4

Output:
0
8
6
7
1
3
4
8
"""
cases = int(input())
for i in range(cases):
    a, b, c = map(int, input().split())
    lowest = 1000
    for i in range(1, 11):
        temp = abs(i - a) + abs(i - b) + abs(i - c)
        if(temp < lowest):
            lowest = temp
    print(lowest)