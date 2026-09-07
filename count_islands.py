"""Counting Islands in an M x N binary matrix."""

from collections import deque
import sys
from typing import List, Sequence, Tuple

DIRECTIONS: Tuple[Tuple[int, int], ...] = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)


def count_islands(matrix: Sequence[Sequence[int]]) -> int:
    """Calculates the number of 4-connected islands in a binary grid."""
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        if len(matrix[r]) != cols:
            raise ValueError(f"Row {r} length ({len(matrix[r])}) does not match expected columns ({cols}).")
        for c in range(cols):
            if matrix[r][c] not in (0, 1):
                raise ValueError(f"Invalid value at ({r}, {c}): {matrix[r][c]}. Expected 0 or 1.")

    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visited:
                islands += 1
                queue = deque([(r, c)])
                visited.add((r, c))

                while queue:
                    curr_r, curr_c = queue.popleft()

                    for dr, dc in DIRECTIONS:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if matrix[nr][nc] == 1 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))

    return islands


def main() -> None:
    """CLI entry point reading M, N and matrix cells from standard input."""
    raw_input = sys.stdin.read().split()
    if not raw_input:
        return

    m, n = int(raw_input[0]), int(raw_input[1])
    values = [int(v) for v in raw_input[2:]]

    if len(values) != m * n:
        raise ValueError(f"Expected {m * n} grid elements, but received {len(values)}.")

    grid: List[List[int]] = [values[i * n : (i + 1) * n] for i in range(m)]
    result = count_islands(grid)
    print(result)


if __name__ == "__main__":
    main()
