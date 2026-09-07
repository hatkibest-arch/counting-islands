# Counting Islands

Solution for finding the number of connected islands in an M x N grid.

## Connectivity Rules
- **4-connectivity (Von Neumann neighborhood):** Land cells are connected strictly horizontally or vertically. Diagonal adjacency is treated as disconnected.

## Complexity
- **Time Complexity:** O(M * N) — each cell is visited and enqueued at most once.
- **Space Complexity:** O(M * N) for the visited set.

## Running the Solution

### Run Unit Tests
```bash
python3 -m unittest test_islands.py
```

### Run CLI via Standard Input
```bash
python3 count_islands.py << 'EOF'
3 4
0 0 0 1
0 0 1 1
0 1 0 1
EOF
```
