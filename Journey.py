"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2051/B -----------------------------------

Monocarp decided to embark on a long hiking journey.

He decided that on the first day he would walk a kilometers, on the second day he would walk b kilometers, on the third day he would walk c kilometers, on the fourth day, 
just like on the first, he would walk a kilometers, on the fifth day, just like on the second, he would walk b kilometers, on the sixth day, just like on the third, he would walk c kilometers, and so on.

Monocarp will complete his journey on the day when he has walked at least n kilometers in total. Your task is to determine the day on which Monocarp will complete his journey.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of one line containing four integers n, a, b, c (1 ≤ n ≤ 10^9; 1 ≤ a,b, c ≤10^6).

Output
For each test case, output one integer — the day on which Monocarp will have walked at least n kilometers in total and will complete his journey.


Input:
4
12 1 5 3
6 6 7 4
16 3 4 1
1000000000 1 1 1

Output:
5
1
6
1000000000
"""
cases = int(input())
for i in range(cases):
    n, a, b, c = map(int, input().split())
    tempSum = a + b + c
    threeDays = n // tempSum
    days = 0
    tempDistance = threeDays * tempSum
    while True:
        if(tempDistance >= n):
            break
        tempDistance += a
        days += 1
        if(tempDistance >= n):
            break
        tempDistance += b
        days += 1
        if(tempDistance >= n):
            break
        tempDistance += c
        days += 1
    print(days + (threeDays * 3))