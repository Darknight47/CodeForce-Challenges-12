"""

---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1921/B ----------------------------------

In order to test the hypothesis about the cats, the scientists must arrange the cats in the boxes in a specific way. 
Of course, they would like to test the hypothesis and publish a sensational article as quickly as possible, because they are too engrossed in the next hypothesis about the phone's battery charge.

Scientists have n boxes in which cats may or may not sit. Let the current state of the boxes be denoted by the sequence b1,…,bn:  b(i)=1 if there is a cat in box number i, and b(i)=0 otherwise.

Fortunately, the unlimited production of cats has already been established, so in one day, the scientists can perform one of the following operations:

Take a new cat and place it in a box (for some i such that b(i) = 0, assign b(i) = 1).
Remove a cat from a box and send it into retirement (for some i such that b(i) = 1, assign b(i) = 0).
Move a cat from one box to another (for some i,j such that b(i) = 1,b(j) = 0, assign b(i) = 0,b(j) = 1).
It has also been found that some boxes were immediately filled with cats. Therefore, the scientists know the initial position of the cats in the boxes s1,…,sn and the desired position f1,…,fn.

Due to the large amount of paperwork, the scientists do not have time to solve this problem. Help them for the sake of science and indicate the minimum number of days required to test the hypothesis.

Input
Each test consists of several test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. This is followed by descriptions of the test cases.

Each test case consists of three lines.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the number of boxes.

The second line of each test case contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise.

The third line of each test case contains a string (f) of (n) characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise.

It is guaranteed that in a test the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output a single integer on a separate line — the minimum number of operations required to obtain the desired position from the initial position. It can be shown that a solution always exists.

Input:
6
5
10010
00001
1
1
1
3
000
111
4
0101
1010
3
100
101
8
10011001
11111110

Output:
2
0
3
2
1
4
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    firstRow = input()
    secondRow = input()
    changeNeeded = 0
    firstOnes = 0
    secondOnes = 0
    for j in range(sze):
        first = firstRow[j]
        second = secondRow[j]
        if(first == '0' and second == '1'):
            changeNeeded += 1
        if(first == '1'):
            firstOnes += 1
        if(second == '1'):
            secondOnes += 1
    if firstOnes == secondOnes:
        print(changeNeeded)
    elif firstOnes > secondOnes:
        print((firstOnes - secondOnes) + changeNeeded)
    else:
        print(max((secondOnes -firstOnes), changeNeeded))