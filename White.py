"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1927/A -----------------------------------------

You have a horizontal strip of n cells. Each cell is either white or black.

You can choose a continuous segment of cells once and paint them all white. After this action, all the black cells in this segment will become white, and the white ones will remain white.

What is the minimum length of the segment that needs to be painted white in order for all n cells to become white?

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10) — the length of the strip.

The second line of each test case contains a string s, consisting of n characters, each of which is either 'W' or 'B'. 
The symbol 'W' denotes a white cell, and 'B' — a black one. It is guaranteed that at least one cell of the given strip is black.

Output
For each test case, output a single number — the minimum length of a continuous segment of cells that needs to be painted white in order for the entire strip to become white.

Input:
8
6
WBBWBW
1
B
2
WB
3
BBW
4
BWWB
6
BWBWWB
6
WWBBWB
9
WBWBWWWBW

Output:
4
1
1
2
4
6
4
7
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    start = False
    end = False
    startIndx = 0
    endIndx = 0
    for j in range(sze):
        temp = s[j]
        if(not start and temp == 'B'):
            start = True
            startIndx = j +1
        elif(start and temp == 'B'):
            end = True
            endIndx = j + 1
    if(start and end):
        ans = (endIndx - startIndx) + 1
        print(ans)
    else:
        print(1)