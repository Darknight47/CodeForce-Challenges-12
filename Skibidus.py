"""
------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2065/B ------------------------

Skibidus is given a string s that consists of lowercase Latin letters. If s contains more than 1 letter, he can:

Choose an index i (1 ≤ i ≤ |s| −1 , |s| denotes the current length of s) such that s(i)=s(i)+1. 
Replace s(i) with any lowercase Latin letter of his choice. Remove s(i)+1 from the string.
Skibidus must determine the minimum possible length he can achieve through any number of operations.

Input
The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases.

The only line of each test case contains a string s (1 ≤ |s| ≤ 100). It is guaranteed s only contains lowercase Latin letters.

Output
For each test case, output an integer on the new line, the minimum achievable length of s.

Input:
4
baa
skibidus
cc
ohio

Output:
1
8
1
4
"""

cases = int(input())
for i in range(cases):
    s = input()
    indx = 0
    canPerform = False
    sLength = len(s)
    while True:
        if(indx >= sLength - 1):
            break
        t1 = s[indx]
        t2 = s[indx + 1]
        if(t1 == t2):
            canPerform = True
            indx += 2
        else:
            indx += 1
        if(canPerform):
            break
    if(canPerform):
        print(1)
    else:
        print(sLength)