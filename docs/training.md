# Training

The experiments use controlled adaptation methods rather than assuming that a small personality dataset can rebuild an entire conversational policy.

- **SFT:** supervised fine-tuning on approved targets.
- **QLoRA:** parameter-efficient adaptation of a quantized foundation.
- **Preference optimization:** learning from chosen/rejected conversational directions.
- **Rollout supervision:** labeling states observed during free-running generation.
- **Policy-conditioned generation:** testing explicit control over completion behavior.

The main lessons so far are that lower loss is not sufficient, preference pressure can cause overshortness, teacher-forced control can fail at runtime, and healthy termination does not guarantee semantic completeness. Private or protected datasets are not published.

