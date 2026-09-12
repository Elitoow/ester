# Schema de dados de treinamento — v0.1

Cada linha JSONL contém:

```json
{
  "example_id": "seed-0001",
  "capabilities": ["need_priority", "grounded_action"],
  "quality": {
    "source": "human_authored",
    "review_status": "approved",
    "confidence": 1.0
  },
  "input": {},
  "target": {}
}
```

## Capacidades iniciais

- `grounded_perception`
- `need_priority`
- `memory_influence`
- `relationship_specificity`
- `uncertainty`
- `emotion_causality`
- `habit_formation`
- `goal_persistence`
- `social_intent`
- `safe_inaction`
- `no_false_memory`
- `available_action_compliance`

## Regras

- não incluir chain of thought;
- não ensinar linguagem de assistente;
- não usar resultados do mundo que ainda não ocorreram;
- separar hipótese de fato;
- não treinar placeholders como verdade;
- manter IDs consistentes;
- usar exemplos contrastivos.
