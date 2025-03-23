"""
--------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2036/A ----------------------------------

Boris Notkin composes melodies. He represents them as a sequence of notes, where each note is encoded as an integer from 0 to 127 inclusive. 
The interval between two notes a and b is equal to |a−b| semitones.

Boris considers a melody perfect if the interval between each two adjacent notes is either 5 semitones or 7 semitones.

After composing his latest melodies, he enthusiastically shows you his collection of works. Help Boris Notkin understand whether his melodies are perfect.

Input
The first line contains an integer t (1 ≤ t ≤ 1000) — the number of melodies.

Each melody is described by two lines.

The first line contains an integer n (2 ≤ n ≤ 50) — the number of notes in the melody.

The second line contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 127) — the notes of the melody.

Output
For each melody, output "YES", if it is perfect; otherwise, output "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
8
2
114 109
2
17 10
3
76 83 88
8
38 45 38 80 85 92 99 106
5
63 58 65 58 65
8
117 124 48 53 48 43 54 49
5
95 102 107 114 121
10
72 77 82 75 70 75 68 75 68 75

Output:
YES
YES
YES
NO
YES
NO
YES
YES
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ok = True
    temp = {5, 7}
    for j in range(sze - 1):
        diff = abs(arr[j] - arr[j + 1])
        if(diff not in temp):
            ok = False
            break
    print("YES" if ok else "NO")