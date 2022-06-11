import enum
import sys

def LCS(str1:str, str2:str) -> None:
    # Initiate LCS Matrix as 0 str1 * str2
    lcs_matrix = [
        [0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)
    ]
    # Index 0 of row and col are margin of this matrix
    # Need to start from index 1
    for i, n in enumerate(str2,start=1):
        for j, m in enumerate(str1,start=1):
            if n == m:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            else:
                lcs_matrix[i][j] = max([lcs_matrix[i-1][j],lcs_matrix[i][j-1]])
    print(lcs_matrix[i][j])

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    LCS(str1,str2)