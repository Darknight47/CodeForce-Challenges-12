"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1692/B -------------------------------------

Sho has an array a consisting of n integers. An operation consists of choosing two distinct indices i and j and removing a(i) and a(j) from the array.

For example, for the array [2,3,4,2,5], Sho can choose to remove indices 1 and 3. 
After this operation, the array becomes [3,2,5]. Note that after any operation, the length of the array is reduced by two.

After he made some operations, Sho has an array that has only distinct elements. In addition, he made operations such that the resulting array is the longest possible.

More formally, the array after Sho has made his operations respects these criteria:

No pairs such that (i < j) and ai=aj exist.
The length of a is maximized.
Output the length of the final array.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — the length of the array.

The second line of each test case contains n integers a(i) (1 ≤ a(i) ≤ 10^4) — the elements of the array.

Output
For each test case, output a single integer — the length of the final array. Remember that in the final array, all elements are different, and its length is maximum.

Input:
4
6
2 2 2 3 3 3
5
9 1 9 9 1
4
15 16 16 15
4
10 100 1000 10000

Output:
2
1
2
4
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempSet = set(arr)
    if((len(tempSet) % 2 == 0 and len(arr) % 2 == 0) or 
       (len(tempSet) % 2 == 1 and len(arr) % 2 == 1)):
        print(len(tempSet))
    else:
        print(len(tempSet) - 1)