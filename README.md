# Classification Approaches

**Regular Expression (Regex):** Handles simple, predictable patterns via predefined rules.

**Sentence Transformer + Logistic Regression:** Uses embeddings to classify when data is sufficient.

**LLM (Large Language Models):** Fallback for complex cases with limited labeled data.

# Usage

Upload a CSV (with `source` and `log_message` columns) to the `/classify` endpoint.
The response is a CSV with an added `target_label` column.

