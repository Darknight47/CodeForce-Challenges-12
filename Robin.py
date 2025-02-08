"""
---------------------- Link for the challenge: https://codeforces.com/problemset/problem/2014/A ----------------------

The heroic outlaw Robin Hood is famous for taking from the rich and giving to the poor.

Robin encounters n people starting from the 1-st and ending with the n-th. The i-th person has a(i) gold. If a(i) ≥ k, Robin will take all a(i) gold, 
and if a(i) = 0, Robin will give 1 gold if he has any. Robin starts with 0 gold.

Find out how many people Robin gives gold to.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers n, k (1 ≤ n ≤ 50, 1 ≤ k ≤ 100) — the number of people and the threshold at which Robin Hood takes the gold.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 100) — the gold of each person.

Output
For each test case, output a single integer, the number of people that will get gold from Robin Hood.

Input:
4
2 2
2 0
3 2
3 0 0
6 2
0 3 0 0 0 0
2 5
5 4

Output:
1
2
3
0
"""
cases = int(input())
for i in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    coin = 0
    ans = 0
    for num in arr:
        if(coin > 0 and num == 0):
            ans += 1
            coin -= 1
        else:
            if(num >= k):
                coin += num
    print(ans)