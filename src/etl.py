import pandas as pd
import json
from pathlib import Path
from src.logger import get_logger

logger = get_logger()

def run_etl(input_path="src/db.json", output_path="src/processed.json"):
    logger.info("Starting ETL pipeline...")

    data = json.loads(Path(input_path).read_text())

    df = pd.DataFrame(data)
    df["value_squared"] = df["value"] ** 2
    df["tag"] = df["value"].apply(lambda x: "high" if x > 50 else "low")

    df.to_json(output_path, orient="records")
    logger.info(f"ETL complete. Output written to {output_path}")