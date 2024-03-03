"""
This code compares two DataFrames line by line
whenever a difference is found
it writes: index, column-name, values in DF1 and DF2
into a new DataFrame
"""

import pandas as pd
import time

df = pd.read_csv("test.csv")
# print(df.columns)

df2 = pd.read_csv("test2.csv")
# print(df2)

cols = ["index", "column", "df1", "df2"]
df3 = pd.DataFrame(columns=cols)
for i in range(len(df)):
    # print(i)
    for j in df.columns:
        # print(j)
        if df.loc[i, j] != df2.loc[i, j]:
            new_row = {
                "index": i,
                "column": j,
                "df1": df.loc[i, j],
                "df2": df2.loc[i, j]
            }
            df3.loc[len(df3)] = new_row
            print(f"found one at {i, j}")

# print(df.loc[0])
# pd.DataFrame.to_csv(df3, "test_result.csv")

print(df3.head)
