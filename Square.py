"""
---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2074/A -----------------------------------------

The pink soldiers have given you 4 distinct points on the plane. The 4 points' coordinates are (−l,0), (r,0), (0,−d), (0,u) correspondingly, where l, r, d, u are positive integers.

Input
Each test contains multiple test cases. The first line contains the number of test cases t(1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains four integers l, r, d, u (1 ≤ l,r,d,u ≤ 10).

Output
For each test case, if you can draw a square using the four points, output "Yes". Otherwise, output "No".

You can output the answer in any case. For example, the strings "yEs", "yes", and "YES" will also be recognized as positive responses.

Input:
2
2 2 2 2
1 2 3 4

Output:
YES
NO
"""
cases = int(input())
for i in range(cases):
    l, r, d, u = map(int, input().split())
    if(l == r == d == u):
        print("YES")
    else:
        print("NO")