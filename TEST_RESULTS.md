# TEST_RESULTS.md

## Correctness (local, Python 3.12)

- Perft: startpos 20/400/8902, kiwipete 48/2039/97862, ep 14/191/2812,
  castling 46/2079/89890 — all OK. Promotion positions count queen-only.
- Mate-in-1 found (Qxf7#, score 29999). Qxd5 hanging pawn +912.
- Determinism: same position, same move, twice.
- Hash: incremental == recomputed over all plies; collision sequence
  b2c4 c8b7 c4d2 b7a8 now gives distinct hashes.

## Practice trials (kit env server, 100k nodes/move)

Anchors: depth-2=855, depth-3=1073, depth-4=1199, 100k=1392, 250k=1497,
500k=1596. Floor 1154; sunfish baseline ~1365.

| trial | engine | W/D/L | score | Elo | wall |
|---|---|---|---|---|---|
| 0 | 60k, old hash | 1/0/5 | 1.0 | 876 | 563 s |
| 0b | 100k, fixed | 3/0/3 | 3.0 | 1279 | 802 s |
| 1 | 100k, old hash | 3/3/0 | 4.5 | 1545 | 1299 s |
| 2 | 100k, fixed | 4/1/1 | 4.5 | 1545 | 827 s |

Trial-2 games: beat depth-2, depth-3, depth-4, nodes-500k by mate;
drew nodes-250k (threefold); lost to nodes-100k (mate).
Trial-0b games: beat depth-2, depth-3, depth-4 by mate; lost to
nodes-100k, nodes-250k, nodes-500k by mate.
Mean of 100k trials: 1456. Mean of fixed-engine trials: 1412.

## Timing (trial-2)

266 moves, mean 3.0 s, p90 4.2 s, max 5.1 s (limit 10 s).
Wall 827 s of 1800 s. No timeouts.
