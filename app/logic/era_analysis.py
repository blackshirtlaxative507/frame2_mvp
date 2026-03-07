import pandas as pd

def build_df(data):
    return pd.DataFrame(data)

def best_win(df):
    return df.sort_values("win_pct", ascending=False).iloc[0]
