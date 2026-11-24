class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                box = (i // 3) * 3 + (j // 3)

                if val in row[i] or val in col[j] or val in sq[box]:
                    return False

                row[i].add(val)
                col[j].add(val)
                sq[box].add(val)

        return True