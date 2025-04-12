"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1896/A ----------------------------------

You are given a permutation† a of size n. You can do the following operation

Select an index i from 2 to n−1 such that ai−1<ai and a(i) > a(i+1). Swap a(i) and a(i)+1.
Determine whether it is possible to sort the permutation after a finite number of operations.

† A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 5000). Description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 10) — the size of the permutation.

The second line of each test case contains n integers a1,a2,…,an (1 ≤a(i) ≤ n) — the elements of permutation a.

Output
For each test case, print "YES" if it is possible to sort the permutation, and "NO" otherwise.

You may print each letter in any case (for example, "YES", "Yes", "yes", "yEs" will all be recognized as positive answer).

Input:
6
3
1 2 3
5
1 3 2 5 4
5
5 4 3 2 1
3
3 1 2
4
2 3 1 4
5
5 1 2 3 4

Output:
YES
YES
NO
NO
NO
NO
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    if(arr[0] == 1):
        print("YES")
    else:
        print("NO")