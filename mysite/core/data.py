import pandas as pd
import difflib
def match(test):
    with open('data.csv', 'r') as data:
        data = data.read().split('\n')[1:]
    df = pd.read_csv('data.csv')
    col_mapping = [f"{c[0]}:{c[1]}" for c in enumerate(df.columns)]
    col_mapping_dict = {c[0]:c[1] for c in enumerate(df.columns)}
    profcard = df.iloc[:,:2]profcard=profcard.values.tolist()
    pf = []
    for i in range(len(profcard)):
        a = '_'.join(profcard[i]).replace(' ','_')
        pf.append(a)
    pf.index(difflib.get_close_matches('_'.join(test.split()),pf)[0])
    z = df.iloc[55,:]
    z = list(z)
    return z[2:]
