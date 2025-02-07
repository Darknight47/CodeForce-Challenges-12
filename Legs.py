"""
--------------- Link for the challenge: https://codeforces.com/problemset/problem/1996/A ------------------------

It's another beautiful day on Farmer John's farm.

After Farmer John arrived at his farm, he counted n legs. 
It is known only chickens and cows live on the farm, and a chicken has 2 legs while a cow has 4.

What is the minimum number of animals Farmer John can have on his farm assuming he counted the legs of all animals?

Input
The first line contains single integer t (1 ≤ t ≤ 10^3) — the number of test cases.

Each test case contains an integer n (2 ≤ n ≤ 2⋅10^3, n is even).

Output
For each test case, output an integer, the minimum number of animals Farmer John can have on his farm.

Input:
3
2
6
8

Output:
1
2
2
"""
import math
cases = int(input())
for i in range(cases):
    legs = int(input())
    cows = 0
    chicks = 0
    if(legs >= 4):
        cows = math.ceil(legs // 4)
    diff = legs - (cows * 4)
    if(diff > 0):
        chicks = diff // 2
    print(cows + chicks)