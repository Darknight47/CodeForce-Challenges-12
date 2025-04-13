"""
---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2062/A ----------------------------

You are given a string s of length n consisting of 0 and/or 1. 
In one operation, you can select a non-empty subsequence t from s such that any two adjacent characters in t are different. Then, you flip each character of t (0 becomes 1 and 1 becomes 0). 
For example, if s=0––0101–––– and t=s1s3s4s5=0101, after the operation, s becomes 1––0010––––.

Calculate the minimum number of operations required to change all characters in s to 0.

Recall that for a string s=s1s2…sn, any string t=si1si2…sik (k ≥ 1) where 1≤i1<i2<…<ik≤n is a subsequence of s.

Input
The first line of input contains a single integer t (1 ≤ t ≤ 10^4) — the number of input test cases.

The only line of each test case contains the string s (1 ≤ |s| ≤ 50), where |s| represents the length of s.

Output
For each test case, output the minimum number of operations required to change all characters in s to 0.

Input:
5
1
000
1001
10101
01100101011101

Output:
1
0
2
3
8
"""
cases = int(input())
for _ in range(cases):
    s = input()
    ones = s.count("1")
    print(ones)