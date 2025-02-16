
import pandas as pd

data = {'n': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]}
df = pd.DataFrame(data)
df['value'] = (1 + 1/df['n'])**df['n']

print(df)