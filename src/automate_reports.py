import pandas as pd
from pathlib import Path

# Define folder paths
DATA_FOLDER = Path("data")
OUTPUT_FOLDER = Path("output")
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Read all Excel files from the data folder
excel_files = list(DATA_FOLDER.glob("*.xlsx"))

# Combine all Excel files
all_data = pd.DataFrame()
for file in excel_files:
    df = pd.read_excel(file)
    df["Source_File"] = file.name  # Keep track of which file it came from
    all_data = pd.concat([all_data, df])

# Basic summary
summary = all_data.groupby("Product").agg({
    "Sales": ["sum", "mean", "max", "min"]
}).reset_index()
# Flatten MultiIndex columns
summary.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in summary.columns]


# Save combined and summary data
combined_path = OUTPUT_FOLDER / "combined_data.xlsx"
summary_path = OUTPUT_FOLDER / "summary_report.xlsx"

all_data.to_excel(combined_path, index=False)
summary.to_excel(summary_path, index=False)



print("✅ Reports generated successfully!")
print(f"Combined data → {combined_path}")
print(f"Summary report → {summary_path}")
