# Evaluation

Evaluation separates structural, conversational, and provenance questions. Gates may include termination, hard-max rate, role leakage, prompt leakage, Portuguese behavior, coherence, context adherence, semantic completeness, task coverage, service posture, over-answering, under-answering, and multi-turn behavior.

Results must preserve provenance. `ELITO_HUMAN` means a judgment entered by Elito. `AI_ASSISTED_BY_CODEX` means an AI-assisted judgment. The latter must never be described as human review.

Automatic metrics can report objective structure such as token counts, termination, repetition, malformed separators, and truncation. Semantic labels and checkpoint preference require an explicitly approved review protocol. A clean stop is not proof that the answer fulfilled the request.

