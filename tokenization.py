# Imports can go here
import pandas as pd
import numpy as np

psid_raw = pd.read_csv('J326246.csv').astype('Int64')
psid_raw.head()

old_col = list(psid_raw.columns)
print(old_col)

# The file with labels and reviews
FILENAME = 'J326246_labels.txt'


with open(FILENAME, 'r') as f:
    new_col = {}
    for col in old_col:
        lines = f.read().split('\n')[5:]
        for line in lines:
            variable, label = line.split(' ', 1)
            label = label.strip()
            if col == variable:
                new_col[col] = label
                break
            else:
                continue

print(new_col)
# df = psid_raw.rename(columns=new_col, inplace=True)
# print(df)