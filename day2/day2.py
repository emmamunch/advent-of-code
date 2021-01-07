import pandas as pd


df = pd.read_csv('day2input.txt', sep=" ", names=['range','rule', 'pw'])


df['rule'] = [ v[:-1] for v in df['rule']]
print(df)

valid = 0
for i, row in df.iterrows():
    range = row['range'].split('-')
    min = int(range[0]) - 1
    max = int(range[1]) - 1
    occur = row['pw'].count(row['rule'])
    # if occur <= max and occur >= min:
    #     valid += 1
    if bool(row['pw'][min] == row['rule']) != bool(row['pw'][max] == row['rule']):
        valid += 1

print(valid)
 