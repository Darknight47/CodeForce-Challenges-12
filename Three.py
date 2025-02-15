"""

----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1933/B ---------------------

You are given an array a1,a2,…,an.

In one move, you can perform either of the following two operations:

Choose an element from the array and remove it from the array. As a result, the length of the array decreases by 1;
Choose an element from the array and increase its value by 1.
You can perform any number of moves. If the current array becomes empty, then no more moves can be made.

Your task is to find the minimum number of moves required to make the sum of the elements of the array a divisible by 3. It is possible that you may need 0 moves.

Note that the sum of the elements of an empty array (an array of length 0) is equal to 0.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^4).

The sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer: the minimum number of moves.

Input:
8
4
2 2 5 4
3
1 3 2
4
3 7 6 8
1
1
4
2 2 4 2
2
5 5
7
2 4 8 1 9 3 4
2
4 10

Output:
1
0
0
1
1
2
1
1
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    s = 0
    one = False
    for num in arr:
        s += num
        if(num % 3 == 1):
            one = True
    if(s % 3 == 0):
        print(0)
    elif(s % 3 == 2):
        print(1)
    else:
        print(1 if one else 2)