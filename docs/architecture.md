# Architecture

Ester separates identity, global state, memory, relationship context, session context, initiative, runtime control, neural generation, and visible output.

```text
ESTER_IDENTITY + ESTER_GLOBAL_STATE + ESTER_GLOBAL_MEMORY
       + USER_PRIVATE_MEMORY[user_id] + RELATIONSHIP[user_id]
       + CURRENT_SESSION[user_id] + INITIATIVE_STATE[user_id] + RUNTIME_STATE
       -> NEURAL ESTER -> REAL MODEL OUTPUT
```

The architecture is conceptual rather than a claim that every component is stable in the current runtime. One Ester may serve multiple users while keeping user-scoped memory and relationship state separate. `USER_A_PRIVATE` must never enter `USER_B` context.

Runtime code can assemble context, retrieve authorized memory, manage state, validate technical conditions, stop generation, split neural messages, and record provenance. It cannot author visible Ester speech.

