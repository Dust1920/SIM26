def indicators_tables(Sonora, Municipio: str):
    data = Sonora[Municipio]
    df = data.copy()
    df.drop(columns=["Unnamed: 0.1","Unnamed: 0"], inplace=True)
    df['NA'] = df.isna().sum(axis = 1)
    search_tables = []
    for i in range(df.shape[0] - 1):
        if df.iloc[i, -1] == 5:
            if df.iloc[i + 1, -1] < 5:
                search_tables.append(i + 1)
        else:
            if df.iloc[i + 1, -1] == 5:
                search_tables.append(i + 1)
    new_dfs = []
    for k in range(len(search_tables) - 1):
        new_dfs.append(df.iloc[search_tables[k]:search_tables[k + 1], :])
    new_dfs.append(df.iloc[search_tables[-1]:, :])
    str_dfs = [data.astype(str) for data in new_dfs]
    str_rows = [data.shape[0] for data in new_dfs]
    select_nas = [(data.iloc[:,0] == 'nan').sum() for data in str_dfs]
    ne_dfs = []
    for k, data in enumerate(str_dfs):
        if select_nas[k] != str_rows[k]:
            ne_dfs.append(data)
    return ne_dfs