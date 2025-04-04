import pandas as pd
sheetId = '1bQo1an4yS1tSOMDhmUTGYtUlgnHDQ47EmIcj4YyuIxo/edit?gid=543365513#gid=543365513' ## REPLACE WITH YOUR SHEETID
sheetUrl = f'https://docs.google.com/spreadsheets/d/{sheetId}'
sheetDF = pd.read_html(
    sheetUrl, attrs={'class': 'waffle'}, skiprows=1
)[0].drop(['1'], axis=1).dropna(axis=0, how='all').dropna(axis=1, how='all')