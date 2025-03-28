"""
------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1999/C -------------------------

As a computer science student, Alex faces a hard challenge — showering. He tries to shower daily, but despite his best efforts there are always challenges. 
He takes s minutes to shower and a day only has m minutes!

He already has n tasks planned for the day. Task i is represented as an interval (l(i), r(i)), which means that Alex is busy and can not take a shower in that time interval 
(at any point in time strictly between l(i) and r(i)). No two tasks overlap.

Given all n time intervals, will Alex be able to shower that day? In other words, will Alex have a free time interval of length at least s?

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains three integers n, s, and m (1 ≤ n ≤ 2⋅10^5; 1 ≤ s , m ≤ 10^9) — the number of time intervals Alex already has planned, 
the amount of time Alex takes to take a shower, and the amount of minutes a day has.

Then n lines follow, the i-th of which contains two integers l(i) and r(i) (0 ≤ l(i) < r(i) ≤ m) — the time interval of the i-th task. No two tasks overlap.

Additional constraint on the input: l(i) > r(i)−1 for every i > 1.

The sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case output "YES" (without quotes) if Alex can take a shower for that given test case, and "NO" (also without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes", and "Yes" will be recognized as a positive response).

Input:
4
3 3 10
3 5
6 8
9 10
3 3 10
1 2
3 5
6 7
3 3 10
1 2
3 5
6 8
3 4 10
1 2
6 7
8 9

Output:
YES
YES
NO
YES
"""
cases = int(input())
for i in range(cases):
    n, s, m = map(int, input().split())
    taskTime = 0
    tempR = 0
    tempL = 0
    ok = False
    for j in range(n):
        l, r = map(int, input().split())
        if(j == 0 and l >= s):
            ok = True
        timeBetween = abs(tempR - l)
        if(j > 0 and timeBetween >= s):
            ok = True
        tempR = r
        tempL = l
    timeAfter = m - tempR
    if(timeAfter >= s):
        ok = True
    print("YES" if ok else "NO")