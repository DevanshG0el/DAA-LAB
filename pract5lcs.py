from typing import List, Tuple

def lcs_table(X: str, Y: str) -> Tuple[List[List[int]], List[List[str]]]:
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    direction = [['·'] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                direction[i][j] = '↖'
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    direction[i][j] = '↑'
                else:
                    dp[i][j] = dp[i][j - 1]
                    direction[i][j] = '←'
    return dp, direction

def lcs_backtrack(X: str, Y: str, dp: List[List[int]]) -> str:
    i, j = len(X), len(Y)
    lcs_chars: List[str] = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_chars.append(X[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return ''.join(reversed(lcs_chars))

def print_cost_matrix_with_directions(X: str, Y: str, dp: List[List[int]], direction: List[List[str]]) -> None:
    m, n = len(X), len(Y)
    header = ["    "]
    header += [f"   {ch} " for ch in (' ' + Y)]
    print(''.join(header))
    for i in range(m + 1):
        row_label = ' ' if i == 0 else X[i - 1]
        line = [f" {row_label}  "]
        for j in range(n + 1):
            arrow = direction[i][j]
            cell = f"{dp[i][j]}{arrow if not (i == 0 or j == 0) else '·'}"
            line.append(f"{cell:>4} ")
        print(''.join(line))

def lcs(X: str, Y: str) -> Tuple[int, str, List[List[int]], List[List[str]]]:
    dp, direction = lcs_table(X, Y)
    seq = lcs_backtrack(X, Y, dp)
    return dp[-1][-1], seq, dp, direction

if __name__ == "__main__":
    X = "AGCCCTAAGGGCTACCTAGCTT"
    Y = "GACAGCCTACAAGCGTTAGCTTG"
    length, seq, dp, direction = lcs(X, Y)
    print("LCS Cost Matrix with Directions:")
    print_cost_matrix_with_directions(X, Y, dp, direction)
    print()
    print(f"Final LCS Length: {length}")
    print(f"LCS: {seq}")