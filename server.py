import os
import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
import uvicorn

from classify import classify

app = FastAPI()

@app.post("/classify")
async def classify_logs(file: UploadFile):
    if not file.filename.lower().endswith('.csv'):
        raise HTTPException(400, "File must be CSV.")
    try:
        df = pd.read_csv(file.file)
        if "source" not in df or "log_message" not in df:
            raise HTTPException(400, "CSV must have 'source' and 'log_message'.")
        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

        # resources klasörüne kaydet
        base = os.path.dirname(__file__)
        res_dir = os.path.join(base, "resources")
        os.makedirs(res_dir, exist_ok=True)
        out = os.path.join(res_dir, "output.csv")
        df.to_csv(out, index=False)

        return FileResponse(out, media_type="text/csv")
    finally:
        file.file.close()

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
