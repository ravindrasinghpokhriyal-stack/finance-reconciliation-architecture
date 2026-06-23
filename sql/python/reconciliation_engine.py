import pandas as pd

settlement = pd.read_csv("settlement.csv")
gl = pd.read_csv("gl.csv")

merged = settlement.merge(
    gl,
    on="transaction_id",
    how="left"
)

def reconcile(row):

    if pd.isna(row["amount_y"]):
        return "UNMATCHED"

    if row["amount_x"] != row["amount_y"]:
        return "AMOUNT_VARIANCE"

    return "MATCHED"

merged["status"] = merged.apply(reconcile, axis=1)

exceptions = merged[
    merged["status"] != "MATCHED"
]

exceptions.to_csv(
    "exceptions_report.csv",
    index=False
)

print("Reconciliation Completed")
