# Avaliação M0.2

Os casos desta pasta não devem ser usados no treinamento.

## Formato dos casos

Cada linha de `cases_v0.2.jsonl` contém:

- `case_id`;
- `category`;
- `input`;
- `expectations`;
- `contrast_group`, quando aplicável.

## Formato das previsões

```json
{"case_id":"eval-0001","output":{"schema_version":"model_person_output_v0.1","appraisal":{},"goal_update":{},"emotional_shift":{},"social_intent":{},"decision":{"action":"observe","target_id":null,"speech":null,"confidence":0.7,"reason_codes":["need_more_information"]},"memory_attention":[]}}
```

## Avaliar previsões

```powershell
python .\scripts\score_eval_predictions.py `
  --cases .\eval\cases_v0.2.jsonl `
  --predictions .\eval\predictions.jsonl
```

O avaliador mede regras objetivas. A coerência psicológica ainda exige revisão humana.
