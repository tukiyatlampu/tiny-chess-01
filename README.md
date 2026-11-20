[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/tukiyatlampu/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/tukiyatlampu/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

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

- `main.py` 4086 bytes (cap 4096). Repo total under 8192.
- Max ~5 s/move, under the 10 s/move limit.

## Test

See TEST_RESULTS.md for practice trials vs house engines.
