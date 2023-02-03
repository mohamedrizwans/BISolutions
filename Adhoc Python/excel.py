import pandas as pd

df = pd.read_excel(r'TableDesign.xlsx', sheet_name="Sheet1")

print(df["sno"].count())
