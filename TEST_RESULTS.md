# TEST_RESULTS.md

Rebuild (r2): rewritten from scratch, behavior-identical.
All numbers from real runs in this session unless marked "prev.".

## Correctness (local, Python 3.12)

- Perft: startpos 20/400/8902, kiwipete 48/2039/97862, ep 14/191/2812,
  castling 46/2079/89890 — all OK. Promotions count queen-only.
- Mate-in-1 Qxf7# (h5f7, score 29999). Determinism: same position,
  same move (b1c3, 14), twice.
- Hash: incremental == recomputed (8 plies); old collision
  sequence now distinct.
- Differential replay vs prev. build (100k nodes, 8 positions:
  startpos, kiwipete, 6x trial-2 ply-20): identical hash, move,
  depth, node count.

## Practice trial-2, rebuild (100k nodes/move)

Anchors: d2=855, d3=1073, d4=1199, 100k=1392, 250k=1497, 500k=1596.
Floor 1154; sunfish ~1365.

Games: beat depth-2/3/4, nodes-500k by mate; drew nodes-250k
(threefold); lost to nodes-100k (mate).
W/D/L 4/1/1, score 4.5/6, Elo 1545, wall 831 s of 1800 s.
Same as prev. trial-2 (4.5, 1545, 827 s).

## Timing (trial-2 rebuild)

262 moves, mean 3.08 s, p90 4.22 s, max 4.96 s (limit 10 s).
No timeouts.

## Prev. trials (reference)

0b: 3.0, Elo 1279, 802 s. Trial-1: 4.5, Elo 1545, 1299 s.
Trial-2: 4.5, Elo 1545, 827 s. Mean of 100k trials: 1456.

## Judge (gpt-6.1-sol Mode MAX, rebuild)

80/100 (strength 55/70, determinism 15/15, edge 5/10, packaging 5/5).
Ready for the final; plausibly competitive for a prize.
95/100 not claimed: 18 games only, two repetition edge cases
deferred; no change fits the 10 free bytes without costing Elo.
