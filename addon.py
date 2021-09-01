import pandas as pd

def get_addon():
    data = {'longitude':[-118.39, -118.15, -122.26, -122.42],	
            'latitude':[34.12, 34.2, 37.46, 37.75],
            'housing_median_age':[29, 52, 26, 52],	
            'total_rooms':[6447, 1786, 5067, 2112],	
            'total_bedrooms':[1012, 306, 750, 528],
            'population':[2184, 1018, 1996, 1227],
            'households':[960, 322, 728, 513],
            'median_income':[8.2816, 4.1518, 7.0001, 3.5536],
            'ocean_proximity':[1,2,3,4]}

    df = pd.DataFrame(data, index=['1','2','3','4'])
    return df
