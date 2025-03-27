"""
------------------------ Link for the challenge: https://codeforces.com/contest/2000/problem/A ----------------------------

Dmitry wrote down t integers on the board, and that is good. He is sure that he lost an important integer n among them, and that is bad.

The integer n had the form 10^x (x≥2), where the symbol '^' denotes exponentiation.. 
Something went wrong, and Dmitry missed the symbol '^' when writing the important integer. For example, instead of the integer 10^5, 
he would have written 105, and instead of 10^19, he would have written 1019.

Dmitry wants to understand which of the integers on the board could have been the important integer and which could not.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 10^4) — the number of integers on the board.

The next t lines each contain an integer a (1 ≤ a ≤ 10000) — the next integer from the board.

Output
For each integer on the board, output "YES" if it could have been the important integer and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

Input:
7
100
1010
101
105
2033
1019
1002

Output:
NO
YES
NO
YES
NO
YES
NO
"""
cases = int(input())
for i in range(cases):
    temp = input()
    if("10" in temp):
        parts = temp.split("10")
        before = parts[0]
        after = "10".join(parts[1:])  # To handle cases with multiple "10"s
        if(after[0] != "0"):
            after = int(after)
            if(after >= 2):
                print("Yes")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")