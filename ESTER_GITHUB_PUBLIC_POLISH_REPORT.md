# Ester public GitHub polish report

## Result

`ESTER_PUBLIC_GITHUB_POLISH = PASS`

This public repository is a sanitized, curated derivative of the private Ester research source. The historical OneLife project tree was not used as a Git repository and was not modified by this publication pass.

## Repositories

- Public: https://github.com/Elitoow/ester (`PUBLIC`)
- Private source of truth: https://github.com/Elitoow/ester-private (`PRIVATE`)

## Documentation

- README expanded with project goal, status, architecture, research history, frontier, privacy, structure, and contribution guidance.
- Architecture, research history, personality, memory, training, evaluation, and privacy docs expanded.
- Added current frontier and roadmap.
- Added license options while retaining `USER_DECISION_REQUIRED`.
- Updated contribution, security, and changelog guidance.

## Safety gate

- `SECRET_SCAN_CRITICAL = 0`
- `PRIVACY_SCAN_CRITICAL = 0`
- `PRIVATE_REAL_TEXT_IN_PUBLIC = 0`
- `USER_PRIVATE_MEMORY_IN_PUBLIC = 0`
- `HOLDOUT_PAYLOAD_IN_PUBLIC = 0`
- `B45_PROTECTED_PAYLOAD_IN_PUBLIC = 0`
- `ABSOLUTE_PRIVATE_PATHS = 0`
- `LARGE_GIT_BLOB_VIOLATIONS = 0`

## Research boundaries

- `MODEL_LOADS = 0`
- `GENERATIONS = 0`
- `TRAINING_RUNS = 0`
- `G15 = NOT_STARTED`
- G14 remains research evidence; `CHECKPOINT_SELECTION = NONE` and `PROMOTION = NO`.

## License

`LICENSE_STATUS = USER_DECISION_REQUIRED`

No license was selected on Elito's behalf. See `LICENSE_OPTIONS.md`.
