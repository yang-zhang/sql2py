import pandas as pd
import numpy as np


def create_test_df(n_row=100):
    df = pd.DataFrame(
        {
            'id_': list(range(n_row)),
            'bin1': np.random.choice(["A", "B"], n_row),
            'bin2': np.random.choice(["T", "F"], n_row),
            'mul1': np.random.choice(["X", "Y", "Z"], n_row),
            'mul2': np.random.choice(["XS", "S", "M", "L", "XL"], n_row),
            'num1': np.random.rand(n_row),
            'num2': np.random.rand(n_row),
            'date_': np.random.choice(
                pd.date_range("2000-01-01",
                              "2000-12-31"),
                n_row, replace=True),
        }
    )
    df.loc[np.random.choice(n_row, int(n_row * 0.01),
                            replace=False), 'bin2'] = None
    df.loc[np.random.choice(n_row, int(n_row * 0.01),
                            replace=False), 'mul2'] = None
    df.loc[np.random.choice(n_row, int(n_row * 0.01),
                            replace=False), 'num2'] = None
    df['date_'] = df['date_'].dt.date.astype('str')

    return df[['id_',
               'date_',
               'bin1',
               'bin2',
               'mul1',
               'mul2',
               'num1',
               'num2']]


def count_star_grpby(df, cols):
    return df.groupby(cols).size().reset_index().rename(columns={0: 'count'})
