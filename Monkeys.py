"""
------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2044/C -----------------------------

Ball is the teacher in Paperfold University. The seats of his classroom are arranged in 2 rows with m seats each.

Ball is teaching a+b+c monkeys, and he wants to assign as many monkeys to a seat as possible. 
Ball knows that a of them only want to sit in row 1, b of them only want to sit in row 2, and c of them have no preference. 
Only one monkey may sit in each seat, and each monkey's preference must be followed if it is seated.

What is the maximum number of monkeys that Ball can seat?

Input
The first line contains an integer t (1≤t≤10^4) — the number of test cases.

Each test case contains four integers m, a, b, and c (1 ≤ m,a,b,c ≤ 10^8).

Output
For each test case, output the maximum number of monkeys you can seat.

Input:
5
10 5 5 10
3 6 1 1
15 14 12 4
1 1 1 1
420 6 9 69

Output:
20
5
30
2
84
"""
cases = int(input())
for i in range(cases):
    m, a, b, c = map(int, input().split())
    row1 = m
    row2 = m
    emptySeats = 0
    ans = 0
    ans += min(row1, a)
    emptySeats += row1 - min(row1, a)
    ans += min(row2, b)
    emptySeats += row2 - min(row2, b)
    ans += min(emptySeats, c)
    print(ans)