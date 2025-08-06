'''This file contains helper functions for notebooks.'''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score


def get_level_counts(data_df: pd.DataFrame, features: list) -> pd.DataFrame:
    '''Takes a dataframe and feature list. Gets level counts for each feature.
    Returns a dataframe with counts indexed by feature and level.'''

    dfs = []

    for feature in features:
        level_counts = data_df[feature].value_counts()
        tuples = list(zip([feature] * len(level_counts), level_counts.index))
        index = pd.MultiIndex.from_tuples(tuples, names=['feature', 'level'])
        df = pd.DataFrame.from_dict({'Count': level_counts.values})
        df.index = index
        dfs.append(df)

    return pd.concat(dfs, axis=0)


def encode_features(data_df: pd.DataFrame, encoder: OneHotEncoder, nominal_features: list) -> pd.DataFrame:
    '''Encodes nominal features in the dataframe using the provided encoder.'''

    encoded_df = pd.DataFrame(
        encoder.transform(data_df[nominal_features]),
        columns=encoder.get_feature_names_out(nominal_features),
        index=data_df.index
    )

    return pd.concat([data_df.drop(columns=nominal_features), encoded_df], axis=1)
