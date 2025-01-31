"""
------------------ Link for the challenge: https://codeforces.com/problemset/problem/2013/A --------------------------

Today, a club fair was held at "NSPhM". In order to advertise his pastry club, Zhan decided to demonstrate the power of his blender.

To demonstrate the power of his blender, Zhan has n fruits.

The blender can mix up to x fruits per second.

In each second, Zhan can put up to y fruits into the blender. After that, the blender will blend min(x,c) fruits, 
where c is the number of fruits inside the blender. After blending, blended fruits are removed from the blender.

Help Zhan determine the minimum amount of time required for Zhan to blend all fruits.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). 
The description of the test cases follows.

The first line of each test case contains one integer n (0 ≤ n ≤ 10^9) — the number of fruits Zhan has.

The second line of each test case contains two integers x and y (1 ≤ x,y ≤ 10^9) — 
the number of fruits the blender can blend per second and the number of fruits Zhan can put into the blender per second.

Output
For each testcase, output a single integer — the minimum number of seconds to blend all fruits.

Input:
5
5
3 4
3
1 2
6
4 3
100
4 3
9
3 3

Output:
2
3
2
34
3
"""
import math
cases = int(input())
for i in range(cases):
    fruits = int(input())
    canBlend, inBlender = map(int, input().split())
    print(math.ceil(fruits / min(canBlend, inBlender)))