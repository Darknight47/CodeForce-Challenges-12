"""
--------------------- Link for the challenge: https://codeforces.com/problemset/problem/2003/A ---------------------------

Turtle thinks a string s is a good string if there exists a sequence of strings t1,t2,…,tk (k is an arbitrary integer) such that:

    k≥2.
    s= t1 + t2 + … + tk, where + represents the concatenation operation. For example, abc = a+bc.
    For all 1 ≤ i < j ≤ k, the first character of ti isn't equal to the last character of t(j).

Turtle is given a string s consisting of lowercase Latin letters. Please tell him whether the string s is a good string!

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). 
The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the length of the string.

The second line of each test case contains a string s of length n, consisting of lowercase Latin letters.

Output
For each test case, output "YES" if the string s is a good string, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as 
positive responses.

Input:
4
2
aa
3
aba
4
abcb
12
abcabcabcabc

Output:
No
nO
Yes
YES
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    if(s[0] == s[sze - 1]):
        print("NO")
    else:
        ok = False
        first = s[0]
        for j in range(1, sze):
            temp = s[j]
            if(first != temp):
                ok = True
                break
        print("YES" if ok else "NO")