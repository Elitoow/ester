# Research history

This is a compact technical narrative, not a dump of internal evidence.

1. **T0/T1 — foundation recovery:** conservative personality SFT produced no clear behavioral improvement.
2. **G5 — stronger SFT search:** validation loss improved, but conversation did not improve proportionally.
3. **G6 — positive-only limitation:** positive examples alone did not reliably move the foundation away from assistant behavior.
4. **G6.5/G6.6 — preference construction:** 17 human-supported directional pairs were assembled; the signal was intentionally small and bounded.
5. **G7 — preference optimization:** strong pressure caused overshortening, while weak pressure caused little movement.
6. **G8 — foundation search:** alternative foundations were tested; no suitable replacement was established.
7. **G9 — conversational substrate:** conversational reconstruction was attempted; termination remained weak.
8. **G10 — dedicated turn token:** a neural turn-end token was tested, but reliable emission was not achieved.
9. **G11 — turn controller:** teacher-forced controller behavior failed to generalize to free-running generation.
10. **G12 — on-policy rollout supervision:** rollout evidence showed that generator completion policy itself could be unhealthy.
11. **G13 — policy-conditioned generation:** termination recovered strongly, while semantic quality regressed.
12. **G14 — semantic completion recovery:** the strongest reported run, R4, reached EOS `31/32` (96.875%), hard max `1/32` (3.125%), with structural repetition `0` and role leakage `0`; out-of-context responses, under-answering, incomplete task coverage, technical explanation issues, self-reference, duplication, and technical loop E29 remained unresolved.

G14 is research evidence only. `CHECKPOINT_SELECTION = NONE` and `PROMOTION = NO`.

## What the experiments taught us

- Lower validation loss does not necessarily mean better conversation.
- Personality signals do not easily override a strong assistant prior.
- Preference optimization can overcorrect toward terseness.
- Termination and semantic completion are distinct problems.
- Teacher-forced behavior may not generalize to free-running generation.
- Structural generation fixes do not automatically fix semantic quality.

