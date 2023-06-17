import json
import glob
import os
import pandas as pd
from pandas.io.json import json_normalize


with open('merged_data_files-7.json') as f:
    json_data = json.load(f)

df = pd.DataFrame(json_data)

print(df)

df.to_csv('out.csv')
