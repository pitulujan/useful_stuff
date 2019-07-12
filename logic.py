import pandas as pd
import joblib

dataframe_dic = joblib.load('dataframe_dic.h5')

device_history = dataframe_dic['mdm_devices_history']

def clean_asset_tags(x):
    if x:
        return x.upper()
    else:
        return None

b=pd.DataFrame()
b['ASSET_TAG'] = dataframe_dic['ams_sf_assets_input']['asset_tag'].apply(clean_asset_tags)

print(b.head())