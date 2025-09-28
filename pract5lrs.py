from typing import List, Tuple

def lrs_table(S: str) -> List[List[int]]:
    n = len(S)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if S[i - 1] == S[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp

def lrs_backtrack(S: str, dp: List[List[int]]) -> str:
    i, j = len(S), len(S)
    out: List[str] = []
    while i > 0 and j > 0:
        if S[i - 1] == S[j - 1] and i != j:
            out.append(S[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return ''.join(reversed(out))

def lrs(S: str) -> Tuple[int, str, List[List[int]]]:
    dp = lrs_table(S)
    seq = lrs_backtrack(S, dp)
    return dp[-1][-1], seq, dp

def print_matrix(S: str, dp: List[List[int]]) -> None:
    n = len(S)
    header = ["    "] + [f"   {ch} " for ch in (' ' + S)]
    print(''.join(header))
    for i in range(n + 1):
        row_label = ' ' if i == 0 else S[i - 1]
        line = [f" {row_label}  "]
        for j in range(n + 1):
            line.append(f"{dp[i][j]:>4} ")
        print(''.join(line))

if __name__ == "__main__":
    S = "AABEBCDD"
    length, seq, dp = lrs(S)
    print("LRS DP Matrix (values):")
    print_matrix(S, dp)
    print()
    print(f"Final LRS Length: {length}")
    print(f"LRS: {seq}")