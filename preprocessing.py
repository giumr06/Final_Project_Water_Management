import pandas as pd
import warnings
import numpy as np
from sklearn import set_config
set_config(transform_output="pandas")

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

### global variables ###

data_sparse_countries = ['Andorra','Antigua and Barbuda', 'Bahamas','Bosnia and Herzegovina','Brunei Darussalam','Cook Islands','Dominica','Equatorial Guinea','Faroe Islands','Grenada','Holy See','Kiribati', 'Liechtenstein','Marshall Islands','Micronesia (Federated States of)','Monaco','Montenegro','Nauru','Niue','Palau','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa','Serbia','San Marino', 'Sao Tome and Principe','Singapore', 'Seychelles','Solomon Islands','Tokelau','Tonga','Vanuatu','Djibouti','Maldives','Papua New Guinea','Tuvalu']

dropdrop_list = ["GDP Deflator (2015)" , "Environmental Flow Requirements" , "Groundwater: accounted outflow to other countries" , "Groundwater: leaving the country to other countries (total)"]

linear_drop_list = ["% of the cultivated area equipped for irrigation", "Area equipped for full control irrigation: actually irrigated", "Area equipped for full control irrigation: total", "MDG 7.5. Freshwater withdrawal as % of total renewable water resources", "Arable land area", "Area equipped for irrigation: total", "Long-term average annual precipitation in volume", "Long-term average annual precipitation in depth", "Groundwater produced internally","Surface water produced internally", "Permanent crops area", "Overlap between surface water and groundwater", "Overlap: between surface water and groundwater", "Rural population with access to safe drinking-water (JMP)", "Surface water: inflow not submitted to treaties", "Surface water: inflow submitted to treaties", "Surface water: accounted inflow", "Total renewable water resources", "Surface water: outflow to other countries secured through treaties", "Surface water: total external renewable", "Surface water: total flow of border rivers", "Surface water: accounted flow of border rivers", "Total renewable surface water", "% of area equipped for full control irrigation actually irrigated", "Surface water: outflow to other countries not submitted to treaties", "Surface water: outflow to other countries submitted to treaties", "Surface water: inflow secured through treaties", "Total freshwater withdrawal"]

drop_for_now_list = ["Human Development Index (HDI) [highest = 1]", "Industry, value added to GDP" , "Services, value added to GDP", "Agriculture, value added to GDP", "Industrial water withdrawal as % of total water withdrawal", "Municipal water withdrawal as % of total withdrawal"]

complete_drop_list = dropdrop_list + linear_drop_list + drop_for_now_list

transformation_dict = {
    "log":
        ["agricultural_water_withdrawal","agricultural_water_withdrawal_as_%_of_total_renewable_water_resources",        "cultivated_area_arable_land_plus_permanent_crops", "dam_capacity_per_capita", "groundwater_entering_the_country_total", "industrial_water_withdrawal", "municipal_water_withdrawal", "population_density", "ratio_between_rainfed_and_irrigated_yields", "rural_population", "industrial_water_use_efficiency","irrigated_agriculture_water_use_efficiency", "services_water_use_efficiency","water_use_efficiency","surface_water_entering_the_country_total", "surface_water_leaving_the_country_to_other_countries_total", "total_agricultural_water_managed_area","total_area_of_the_country_excl_coastal_water", "total_dam_capacity", "total_internal_renewable_water_resources", "total_internal_renewable_water_resources_per_capita", "total_population", "total_renewable_groundwater", "total_renewable_water_resources_per_capita", "total_water_withdrawal", "urban_population"],
    "square_root":
        ["national_rainfall_index"],
    "cube_root":
        ["%_of_agricultural_gva_produced_by_irrigated_agriculture", "%_of_total_country_area_cultivated",  "agriculture_value_added_%_gdp", "total_water_withdrawal_per_capita"]}

imputation_dict = {
    'Qatar': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0,'ratio_between_rainfed_and_irrigated_yields': 0},
    'Republic of Korea': {'national_rainfall_index': 1150},
    'Saudi Arabia': {'ratio_between_rainfed_and_irrigated_yields': 0, 'surface_water_leaving_the_country_to_other_countries_total': 0},
    'South Sudan': {'national_rainfall_index': 0, 'total_dam_capacity': 0, 'dam_capacity_per_capita': 0},
    'Sudan': {'national_rainfall_index': 257},
    'Timor-Leste':{'national_rainfall_index': 1500, 'total_dam_capacity': 0, 'dam_capacity_per_capita': 0},
    'Turkmenistan': {'ratio_between_rainfed_and_irrigated_yields': 0},
    'United Arab Emirates': {'ratio_between_rainfed_and_irrigated_yields': 0},
    'Yemen': {'surface_water_leaving_the_country_to_other_countries_total': 0},
    'Iceland': {'%_of_agricultural_water_managed_area_equipped_for_irrigation': 0, 'total_agricultural_water_managed_area': 0},
    'Iraq': {'surface_water_leaving_the_country_to_other_countries_total': 0},
    'Israel': {'dam_capacity_per_capita': 0,'total_dam_capacity': 0},
    'Jordan': {'surface_water_leaving_the_country_to_other_countries_total': 0},
    'Kuwait': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0, 'ratio_between_rainfed_and_irrigated_yields': 1.24},
    'Malta': {'national_rainfall_index': 568},
    'Luxembourg': {'national_rainfall_index': 847.9},
    'Mauritius': {'national_rainfall_index': 2342},
    'Oman': {'ratio_between_rainfed_and_irrigated_yields': 1.24,'surface_water_leaving_the_country_to_other_countries_total': 0},
    'Palestine': {'national_rainfall_index': 490},
    'Azerbaijan': {'surface_water_leaving_the_country_to_other_countries_total': 0},
    'Bahrain': {'national_rainfall_index': 36},
    'Barbados': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0, 'national_rainfall_index': 1525},
    'Burundi': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0},
    'Central African Republic': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0},
    'Chad': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0},
    'Comoros': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0},
    "Democratic People's Republic of Korea": {'national_rainfall_index': 244},
    'Egypt': {'ratio_between_rainfed_and_irrigated_yields': 1.124},
    'Gambia': {'dam_capacity_per_capita': 0, 'total_dam_capacity': 0},
    'Puerto Rico': {'dam_capacity_per_capita': 119.6, 'total_dam_capacity': 0.3937}
    }

scaled_cols = ['year', '%_of_agricultural_gva_produced_by_irrigated_agriculture', '%_of_agricultural_water_managed_area_equipped_for_irrigation', '%_of_total_country_area_cultivated', 'agricultural_water_withdrawal', 'agricultural_water_withdrawal_as_%_of_total_renewable_water_resources', 'agricultural_water_withdrawal_as_%_of_total_water_withdrawal', 'agriculture_value_added_%_gdp', 'cultivated_area_arable_land_plus_permanent_crops', 'dam_capacity_per_capita', 'dependency_ratio', 'groundwater_accounted_inflow', 'groundwater_entering_the_country_total', 'industrial_water_withdrawal', 'municipal_water_withdrawal', 'national_rainfall_index', 'population_density', 'ratio_between_rainfed_and_irrigated_yields', 'rural_population', 'industrial_water_use_efficiency', 'irrigated_agriculture_water_use_efficiency', 'services_water_use_efficiency', 'water_use_efficiency', 'surface_water_entering_the_country_total', 'surface_water_leaving_the_country_to_other_countries_total', 'total_agricultural_water_managed_area', 'total_area_of_the_country_excl_coastal_water', 'total_dam_capacity', 'total_internal_renewable_water_resources', 'total_internal_renewable_water_resources_per_capita', 'total_population', 'total_renewable_groundwater', 'total_renewable_water_resources_per_capita', 'total_water_withdrawal', 'total_water_withdrawal_per_capita', 'urban_population', 'water_resources_total_external_renewable']

hot_cols = ['country']


### drop class ###

class FromColumnDropper:
    def __init__(self, drop_from_col, drop_list):
        self.drop_from_col = drop_from_col
        self.drop_list = drop_list

    def fit(self, df):
        pass

    def transform(self, df):
        df_short = df[~df[self.drop_from_list].isin(self.drop_list)]
        return df_short

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)


### pivot class ###

class Pivoter:
    def __init__(self):
        pass

    def fit(self):
        pass

    def transform(self, df):
        df_pivot = df_shorter.pivot_table(index=["Country","Year"], columns="Variable", values="Value")
        df_pivot.reset_index(inplace=True)
        return df_pivot

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)


### imputer classes ###

class GroupedMedianImputer:
    def __init__(self, group_col):
        self.group_col = group_col
        self.medians = None

    def fit(self, df):
        self.medians = df.groupby(self.group_col)[self.value_cols].median()

    def transform(self, df):
        df_new = df.copy()
        if self.medians is None:
            raise Exception("The imputer has not been fitted yet.")
        
        def fillna_grouped(x):
            return x.fillna(self.medians.loc[x.name, col])

        for col in df_new.columns.to_list():
            if col==self.group_col: continue
            df_new[col] = df.groupby(self.group_col)[col].transform(fillna_grouped)
        
        return df_new

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)


class FromDictImputer:
    def __init__(self, imputation_dict):
        self.imputation_dict = imputation_dict

    def fit(self):
        pass

    def transform(self, df):
        df_new = df.copy()
        for c, c_dict in self.imputation_dict.items():
            if c in df.country:
                index_list = df_new.query("country == @c").index
                for col, val in c_dict.items():
                    df_new.loc[index_list, col] = val
        return df_new

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)


### converter classes / functions ###

class FromDictConverter:
    def __init__(self, conversion_dict):
        self.conversion_dict = conversion_dict

    def fit(self):
        pass
    
    def transform(self, df):
        df_new = df.copy()
        df_new = self.log_convert(df_new, self.conversion_dict["log"])
        df_new = self.sqroot_convert(df_new, self.conversion_dict["square_root"])
        df_new = self.cube_convert(df_new, self.conversion_dict["cube_root"])
        return df_new

    def log_convert(self, df, col_list):
        df[col_list] = df[col_list].applymap(lambda x: np.log(x+1e-10))
        return df

    def sqroot_convert(self, df, col_list):
        df[col_list] = df[col_list].applymap(np.sqrt)
        return df

    def cube_convert(self, df, col_list):
        df[col_list] = df[col_list].applymap(lambda x: np.power(x, 1/3.))
        return df

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)


### preprocessing getter functions ###

def get_full_preprocessor():

    all_col_pipeline = Pipeline[(
        ("drop_countries", FromColumnDropper("country", data_sparse_countries)),
        ("drop_variables", FromColumnDropper("Variable", complete_drop_list)),
        ("pivot", Pivoter()),
        ("hard_imputation", FromDictImputer(imputation_dict)),
        ("median_imputation", GroupedMedianImputer("country")),
        ("conversion", FromDictConverter(transformation_dict)),        
    )]
    num_pipeline = Pipeline([
        ('scaling', StandardScaler())
        ])
    cat_pipeline = Pipeline([
        ('ohe', OneHotEncoder(drop='first',sparse=False))
        ])
    preprocessor = ColumnTransformer([
        ('all_col_preprocessor', all_col_pipeline, make_column_selector())
        ('num_preprocessor', num_pipeline, scaled_cols),
        ('cat_preprocessor', cat_pipeline, hot_cols),
        ])

    return preprocessor
