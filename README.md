# Classification Approaches

**Regular Expression (Regex):** Handles simple, predictable patterns via predefined rules.

**Sentence Transformer + Logistic Regression:** Uses embeddings to classify when data is sufficient.

**LLM (Large Language Models):** Fallback for complex cases with limited labeled data.

# Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start FastAPI server:
   ```bash
   uvicorn server:app --reload
   ```
3. Access API:
   - Main: http://127.0.0.1:8000/
   - Swagger: http://127.0.0.1:8000/docs
   - ReDoc:   http://127.0.0.1:8000/redoc

# Usage

Upload a CSV (with `source` and `log_message` columns) to the `/classify` endpoint.
The response is a CSV with an added `target_label` column.
EOF
