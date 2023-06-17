import json
import glob
import os
import pandas as pd

result = []

files = list(glob.glob(os.path.join('*.json')))

print(files)
print("")
print("Number of files : ", len(files))

for f in files:
    with open(f,'r') as infile:
        result.append(json.load(infile))

with open('merged_data_files-%s.json' % len(files), 'w') as outfile:
     json.dump(result, outfile)

#with open('merged_data_files-%s.json' % len(files)) as f:
#    json_data = json.load(f)

df = pd.DataFrame(result)

print(df)

df.to_csv('out.csv')

##df = pd.read_json('merged_data_files-%s.json' % len(files))
##
##print(df)
##
###df.set_index("Date", inplace=True)
##
###print(df)
##
##df.to_csv("merged.csv")
