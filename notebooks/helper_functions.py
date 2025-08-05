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


class SplitModel:
    def __init__(self, training_df, testing_df):
        self.smoker_training_df = training_df[training_df['smoker_yes'] == 1].copy()
        self.nonsmoker_training_df = training_df[training_df['smoker_yes'] == 0].copy()
        self.smoker_training_df.drop('smoker_yes', axis=1, inplace=True)
        self.nonsmoker_training_df.drop('smoker_yes', axis=1, inplace=True)

        self.smoker_testing_df = testing_df[testing_df['smoker_yes'] == 1].copy()
        self.nonsmoker_testing_df = testing_df[testing_df['smoker_yes'] == 0].copy()
        self.smoker_testing_df.drop('smoker_yes', axis=1, inplace=True)
        self.nonsmoker_testing_df.drop('smoker_yes', axis=1, inplace=True)
        
        self.smoker_model = LinearRegression()
        self.nonsmoker_model = LinearRegression()
        self.smoker_predictions = None
        self.nonsmoker_predictions = None

    def fit(self):
        # Fit the model on the training data

        self.smoker_model.fit(self.smoker_training_df.drop('charges', axis=1), self.smoker_training_df['charges'])
        self.nonsmoker_model.fit(self.nonsmoker_training_df.drop('charges', axis=1), self.nonsmoker_training_df['charges'])

    def predict(self):
        # Make predictions on the testing data

        self.smoker_predictions = self.smoker_model.predict(self.smoker_testing_df.drop('charges', axis=1))
        self.nonsmoker_predictions = self.nonsmoker_model.predict(self.nonsmoker_testing_df.drop('charges', axis=1))

    def evaluate(self):
        # Evaluate the model performance

        predictions = self.smoker_predictions.tolist() + self.nonsmoker_predictions.tolist()
        labels = self.smoker_testing_df['charges'].tolist() + self.nonsmoker_testing_df['charges'].tolist()

        rmse = root_mean_squared_error(labels, predictions)
        rsq = r2_score(labels, predictions)
        
        return rmse, rsq