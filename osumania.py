"""
---------------------------- Link for the challenge: https://codeforces.com/contest/2009/problem/B ----------------------------------

You are playing your favorite rhythm game, osu!mania. The layout of your beatmap consists of n rows and 4 columns. 
Because notes at the bottom are closer, you will process the bottommost row first and the topmost row last. Each row will contain exactly one note, represented as a '#'.

For each note 1,2,…,n, in the order of processing, output the column in which the note appears.

Input
The first line contains t (1 ≤ t ≤ 100) — the number of test cases.

For each test case, the first line contains n (1 ≤ n ≤ 500) — the number of rows of the beatmap.

The following n lines contain 4 characters. The i-th line represents the i-th row of the beatmap from the top. 
It is guaranteed that the characters are either '.' or '#', and exactly one of the characters is '#'.

It is guaranteed that the sum of n over all test cases does not exceed 500.

Output
For each test case, output n integers on a new line, the column that the i-th note appears in for all i from 1 to n.

Input:
3
4
#...
.#..
..#.
...#
2
.#..
.#..
1
...#

Output:
4 3 2 1 
2 2 
4 
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = []
    ans = []
    for j in range(sze):
        arr.append(input())
    for a in range(sze - 1, -1, -1):
        temp = arr[a]
        ans.append(temp.index('#') + 1)
    print(*ans)