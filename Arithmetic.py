"""
----------------- Link for the challenge: https://codeforces.com/problemset/problem/2061/A -------------------------

To train young Kevin's arithmetic skills, his mother devised the following problem.

Given n integers a1,a2,…,an and a sum s initialized to 0, Kevin performs the following operation for i=1,2,…,n in order:

Add a(i) to s. If the resulting s is even, Kevin earns a point and repeatedly divides s by 2 until it becomes odd.
Note that Kevin can earn at most one point per operation, regardless of how many divisions he does.

Since these divisions are considered more beneficial for Kevin's development, his mother wants to rearrange a
so that the number of Kevin's total points is maximized. Determine the maximum number of points.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). 
The description of the test cases follows.

The first line of each test case contains a single integer n(1 ≤ n ≤ 100) — the number of integers.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9).

Output
For each test case, output one integer — the maximum number of points.

Input:
5
1
1
2
1 2
3
2 4 6
4
1000000000 999999999 999999998 999999997
10
3 1 4 1 5 9 2 6 5 3

Output:
0
2
1
3
8
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    points = 0
    oneEvenExist = False
    odds = 0
    for num in arr:
        if(num % 2 == 0):
            oneEvenExist = True
        else:
            odds += 1
    if(oneEvenExist and odds > 0):
        print(odds + 1)
    elif(oneEvenExist and odds == 0):
        print(1)
    elif(not oneEvenExist and odds > 0):
        print(odds - 1)