"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1846/A -------------------------------------

There are n nails driven into the wall, the i-th nail is driven a(i) meters above the ground, one end of the b(i) meters long rope is tied to it. 
All nails hang at different heights one above the other. One candy is tied to all ropes at once. Candy is tied to end of a rope that is not tied to a nail.

To take the candy, you need to lower it to the ground. To do this, Rudolph can cut some ropes, one at a time. Help Rudolph find the minimum number of ropes that must be cut to get the candy.


Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains one integer n (1 ≤ n ≤ 50) — the number of nails.

The i-th of the next n lines contains two integers a(i) and b(i) (1 ≤ a(i), b(i) ≤ 200) — the height of the i-th nail and the length of the rope tied to it, all a(i) are different.

It is guaranteed that the data is not contradictory, it is possible to build a configuration described in the statement.

Output
For each test case print one integer — the minimum number of ropes that need to be cut to make the candy fall to the ground.

Input:
4
3
4 3
3 1
1 2
4
9 2
5 2
7 7
3 4
5
11 7
5 10
12 9
3 2
1 5
3
5 6
4 5
7 7

Output:
2
2
3
0
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    ans = 0
    for j in range(sze):
        a, b = map(int, input().split())
        if(b < a):
            ans += 1
    print(ans)