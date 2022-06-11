import enum
import sys

'''
ACAYKP
CAPCAK

[ Print LCS Matrix ]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 1, 1]
[0, 1, 1, 2, 2, 2, 2]
[0, 1, 1, 2, 2, 2, 3]
[0, 1, 2, 2, 2, 2, 3]
[0, 1, 2, 3, 3, 3, 3]
[0, 1, 2, 3, 3, 4, 4]

LCS String : ACAK
'''

def LCS(str1:str, str2:str) -> str:
    lcs_string_result = []
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
    print("\n[ Print LCS Matrix ]")
    print(*lcs_matrix,sep="\n")
    # 왼쪽, 위중 왼쪽을 먼저 탐색한다고 가정한다.

    while(True):
        # 분기문 단축을 위해서 왼쪽 위중 같은 것이 없는지부터 확인한다
        if lcs_matrix[j][i] != lcs_matrix[j-1][i] and lcs_matrix[j][i] != lcs_matrix[j][i-1]:
            lcs_string_result.append(str1[i-1])
            # i와 j를 1씩 줄여 왼쪽 상단 대각선으로 이동
            i = i-1
            j = j-1
            # 만약 이동한 대각선의 값이 0이라면 종료한다.
            if not lcs_matrix[i][j]:
                break
        else:
            if lcs_matrix[j][i] == lcs_matrix[j-1][i]:
                # 왼쪽으로 이동
                j = j-1
            else:
                #위쪽으로 이동
                i = i-1
    return ''.join(reversed(lcs_string_result))

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(f"\nLCS String : {LCS(str1,str2)}")