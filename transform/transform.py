def transform_mun(mun: str, data):
    df = data[mun].copy()
    df.drop(columns=["Unnamed: 0.1","Unnamed: 0"], inplace=True)
    df.dropna(how = 'all', axis = 0, inplace=True)
    df.reset_index(drop=True,inplace=True)

    abs_index = []
    for i in range(len(df)):
        if df.iloc[i, 1] == 'Absoluto':
            abs_index.append(i)
    abs_index.append(len(df))
    new_dfs = []
    for a in range(len(abs_index) - 1):
        u = df.iloc[abs_index[a]:abs_index[a + 1],:]
        u = u.dropna(how = 'all', axis = 1) 
        new_dfs.append(u)
    return new_dfs