import importlib
import sys

print("\nLOADING STATUS: Loading programs...\n")

required = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib.pyplot": "Visualization ready",
}

for p, m in required.items():
    try:
        ip = importlib.import_module(p)
        pv = getattr(ip, "__version__", "Available")
        print(f"[OK] {p} ({pv}) - {m}")

    except ImportError:
        print(f"Missing required package : {p}\n\n")
        print(
            "Please install with pip :\n"
            "> pip install -r requirements.txt\n\n"
            "Or Poetry :\n"
            "> poetry install\n"
            "> poetry run python loading.py\n\n"
        )
        sys.exit(1)

import pandas as pd  # noqa: E402
import numpy as np  # noqa: E402
import matplotlib.pyplot as mp  # noqa: E402
import requests  # noqa: E402


def fetch_data() -> list:
    """
    Fetches the data from external API
    """
    try:
        url = "https://dummyjson.com/quotes?limit=1000"
        req = requests.get(url, timeout=5)

        req.raise_for_status()

        data = req.json()

        return data.get("quotes", [])
    except Exception as e:
        print(f"API error \n\n {e}")
        sys.exit(1)


data = fetch_data()

print("\nAnalyzing Matrix data...")

df = pd.DataFrame(data)

authors, count = np.unique(df["author"].values, return_counts=True)

analyse_df = pd.DataFrame({"author": authors, "count": count})
analyse_df = analyse_df.sort_values(by="author")

print(f"Processing {len(df)} data points...")
print("Generating visualization...\n")

mp.figure(figsize=(12, 6))
mp.barh(analyse_df["author"], analyse_df["count"], color="green")

mp.title("Number of quote per author in the data")
mp.xlabel("Quotes number")
mp.ylabel("Authors")
mp.tight_layout()

image_file = "matrix_analysis.png"
mp.savefig(image_file)

print("Analysis complete!")
print(f"Results saved to: {image_file}")
