"""
---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2025/A -----------------------------

There are two screens which can display sequences of uppercase Latin letters. Initially, both screens display nothing.

In one second, you can do one of the following two actions:

choose a screen and an uppercase Latin letter, and append that letter to the end of the sequence displayed on that screen;
choose a screen and copy the sequence from it to the other screen, overwriting the sequence that was displayed on the other screen.
You have to calculate the minimum number of seconds you have to spend so that the first screen displays the sequence s, and the second screen displays the sequence t.

Input
The first line contains one integer q (1 ≤ q ≤ 500) — the number of test cases.

Each test case consists of two lines. The first line contains the string s, and the second line contains the string t (1 ≤ |s|, |t| ≤ 100). 
Both strings consist of uppercase Latin letters.

Output
For each test case, print one integer — the minimum possible number of seconds you have to spend so that the first screen displays the sequence s, and the second screen displays the sequence t.

Input:
3
GARAGE
GARAGEFORSALE
ABCDE
AABCD
TRAINING
DRAINING

Output:
14
10
16
"""
cases = int(input())
for i in range(cases):
    s = input()
    t = input()
    minLen = min(len(s), len(t))
    equals = 0
    for j in range(minLen):
        a = s[j]
        b = t[j]
        if(a == b):
            equals += 1
        else:
            break
    ans = (len(s) + len(t)) - equals
    if(equals > 0):
        ans += 1
    print(ans)