"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1873/C --------------------------------

A 10×10 target is made out of five "rings" as shown. Each ring has a different point value: the outermost ring — 1 point, 
the next ring — 2 points, ..., the center ring — 5 points.

Vlad fired several arrows at the target. Help him determine how many points he got.

Input
The input consists of multiple test cases. The first line of the input contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of 10 lines, each containing 10 characters. Each character in the grid is either X (representing an arrow) or. (representing no arrow).

Output
For each test case, output a single integer — the total number of points of the arrows.

Input:
4
X.........
..........
.......X..
.....X....
......X...
..........
.........X
..X.......
..........
.........X
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
....X.....
..........
..........
..........
..........
..........
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX

Output:
17
0
5
220
"""
cases = int(input())
def classify_position(x, y, size=10):
    ring_points = [(0, size - 1), (1, size - 2), (2, size - 3), (3, size - 4), (4, size - 5)]  # Define the boundaries for each ring

    for i, (start, end) in enumerate(ring_points):
        if (x == start or x == end or y == start or y == end) or (start < x < end and (y == start or y == end)) or (start < y < end and (x == start or x == end)):
            return i + 1  # Return the ring number (1-based index)

    return None  # Not in any ring

for _ in range(cases):
    grid = []
    diction = {}
    for j in range(10):
        grid.append(input())
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == 'X':
                ring = classify_position(x, y)
                if(ring in diction):
                    diction[ring] += 1
                else:
                    diction[ring] = 1
    ans = 0
    for key in diction:
        temp = diction[key] * key
        ans += temp
    print(ans)