"""
---------------- Link for the challenge: https://codeforces.com/problemset/problem/1857/A ---------------------

You are given an array consisting of n integers. Your task is to determine whether it is possible to color all its 
elements in two colors in such a way that the sums of the elements of both colors have the same parity and each color 
has at least one element colored.

For example, if the array is [1,2,4,3,2,3,5,4], we can color it as follows: [1,2,4,3,2,3,5,4], 
where the sum of the blue elements is 6 and the sum of the red elements is 18.

Input
The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case begins with a line containing an integer n (2 ≤ n ≤ 50) — the length of the array a.

The next line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 50) — the elements of the array a.

Output
For each test case, output "YES" (without quotes) if it is possible to color the array in two colors in such a 
way that the sums of the elements of both colors have the same parity and each color has at least one element colored, and "NO" otherwise.

You can output "Yes" and "No" in any case (for example, the strings "yES", "yes", and "Yes" will be recognized as correct answers).

Input:
7
8
1 2 4 3 2 3 5 4
2
4 7
3
3 9 8
2
1 7
5
5 4 3 2 1
4
4 3 4 5
2
50 48

Output:
YES
NO
YES
YES
NO
YES
YES
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    odds = 0
    for num in arr:
        if(num % 2 == 1):
            odds += 1
    if(odds % 2 == 0):
        print("YES")
    else:
        print("NO")