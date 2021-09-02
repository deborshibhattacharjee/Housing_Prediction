import numpy as np
import pandas as pd
from addon import get_addon

## Function to receive data from user
def predict_housing_price(area_data, model):
    df = pd.DataFrame(area_data, index=[0])
    
    added_df = get_addon()
    
    final_df = df.append(added_df)
    
    preprocess_data = preprocess_ocean_cols(final_df)
    
    prepared_data = pipeline_transformer(preprocess_data)

    y_pred = model.predict([prepared_data[0]])
    return np.array_str(y_pred)


def preprocess_ocean_cols(df):
    df["ocean_proximity"] = df["ocean_proximity"].map({1: "<1H OCEAN", 2: "INLAND", 3: "NEAR OCEAN", 4:"NEAR BAY"})
    return df

## A custom transformer class to add the combined attributes 
#  room_per_household, bedrooms_per_room and population_per_household to the
#  dataset
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6
from sklearn.base import BaseEstimator, TransformerMixin
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                        bedrooms_per_room]
        
        else:
            return np.c_[X, rooms_per_household, population_per_household]

##complete pipeline to transform 
##both numerical numerical and categorical attributes
##imputing -> adding attributes -> scale them

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
def pipeline_transformer(data):

    num_pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")),
                            ('attribs_adder', CombinedAttributesAdder()),
                            ('std_scaler', StandardScaler())])
    
    temp = data.drop(["ocean_proximity"],axis=1)

    num_attrs = list(temp)
    cat_attribs = ["ocean_proximity"]

    full_pipeline = ColumnTransformer([("nums", num_pipeline, list(num_attrs)),
                                  ("cat", OneHotEncoder(), cat_attribs)])

    housing_data = full_pipeline.fit_transform(data)
    return housing_data

