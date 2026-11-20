# tiny-chess-01

Strongest chess engine in 4096 bytes of Python (stdlib only).

## Architecture

- 0x88 board, 128-int array; pieces ±1..6.
- Alpha-beta + PVS, iterative deepening, fixed 100k nodes/move.
- Quiescence (captures/promotions; all evasions in check).
- Transposition table (incremental Zobrist-style hash, mate-score
  ply adjust), killer moves, MVV-LVA ordering.
- Eval: material + formula piece-square tables, king mg/eg phase
  interpolation, bishop pair +25.
- Repetition: game-history + search-path hash. Queen-only promotion.
- Deterministic: no clock, no randomness, no model calls.

## Limits

- `main.py` 4094 bytes (cap 4096). Repo total under 8192.
- Max ~5 s/move, under the 10 s/move limit.

## Test

See TEST_RESULTS.md. Practice trials vs house engines
(depth-2 .. nodes-500k).
