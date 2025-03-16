"""
---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1776/A ---------------------------

One of the SWERC judges has a dog named Boy. Besides being a good competitive programmer, Boy loves fresh air, 
so she wants to be walked at least twice a day. Walking Boy requires 120 consecutive minutes. 
Two walks cannot overlap, but one can start as soon as the previous one has finished.

Today, the judge sent n messages to the SWERC Discord server. The i-th message was sent a(i) minutes after midnight. 
You know that, when walking Boy, the judge does not send any messages, 
but he can send a message right before or right after a walk. Is it possible that the judge walked Boy at least twice today?

Note that a day has 1440 minutes, and a walk is considered to happen today if it starts at a minute s ≥ 0 and ends right before a minute e ≤ 1440. 
In that case, it must hold that e−s=120 and, for every i=1,2…,, either a(i) ≤ s or a(i) ≥ e.

Input
Each test contains multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases. 
The descriptions of the t test cases follow.

The first line of each test case contains an integer n (1 ≤ n ≤ 100) — the number of messages sent by the judge.

The second line of each test case contains nintegers a1,a2,…,an (0 ≤ a1 < a2 < ⋯ < an < 1440) — 
the times at which the messages have been sent (in minutes elapsed from midnight).

Output
For each test case, output one line containing YES if it is possible that Boy has been walked at least twice, and NO otherwise.

Input:
6
14
100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400
12
100 200 300 400 600 700 800 900 1100 1200 1300 1400
13
100 200 300 400 500 600 700 800 900 1100 1200 1300 1400
13
101 189 272 356 463 563 659 739 979 1071 1170 1274 1358
1
42
5
0 1 2 3 4

Output:
NO
YES
NO
YES
YES
YES
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    counter = 0
    for j in range(sze - 1):
        diff = arr[j + 1] - arr[j]
        if(diff >= 120):
            counter += diff
    if(arr[0] >= 120):
        counter += arr[0]
    if((1440 - arr[sze - 1]) >= 120):
        counter += (1440 - arr[sze - 1])
    if(counter < 120):
        print("NO")
    else:
        temp = counter // 120
        if(temp >= 2):
            print("YES")
        else:
            print("NO")