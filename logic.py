import pandas as pd
import joblib

airtight_sensors_history=joblib.load('airtight_sensors_history.h5')
ams_rules_input=joblib.load('ams_rules_input.h5')
ams_bat_input=joblib.load('query_ams_bat_input.h5')
shared_sku_master=joblib.load('shared_sku_master.h5')
shared_assets_history=joblib.load('shared_assets_history.h5')
mdm_devices_history=joblib.load('mdm_devices_history.h5')
ams_sf_assets_input=joblib.load('ams_sf_assets_input.h5')
shared_mdm_custom_rom_sku_mapping=joblib.load('shared_mdm_custom_rom_sku_mapping.h5')
mdm_missing_mac_addresses=joblib.load('mdm_missing_mac_addresses.h5')
broadsign_hosts_history=joblib.load('broadsign_hosts_history.h5')
broadsign_monitor_polls_history=joblib.load('broadsign_monitor_polls_history.h5')
ams_broadsign_migration_devices_historyjoblib.load('ams_broadsign_migration_devices_history.h5')
ams_cms_input_history=joblib.load('ams_cms_input_history.h5')

def clean_asset_tags(x):
    if x:
        return x.upper()
    else:
        return None

pandas_ams_cms_input_precursor = pd.DataFrame(columns=['asset_tag','source_system','source_system_id','source_system_asset_name','product','product_use','cmh_id','device_location_status','last_pinged_at','mac_address','public_ip_address','sku','created_at','installed_date','deleted_at','reason_for_deletion','export_date'])

ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)
ams_sf_assets_input.['asset_tag'].fillna('None',inplace=True)
b=ams_sf_assets_input.groupby('asset_tag')[['sku']].first().reset_index()
b['asset_tag']=b['asset_tag'].str.upper()


mdm_devices_history['asset_id'] = mdm_devices_history['asset_id'].str.upper()
s1 = pd.merge(mdm_devices_history, b, how='left', left_on=['asset_id'],right_on=['asset_tag'],suffixes=('_a','_b'))
s2 = pd.merge(s1, shared_mdm_custom_rom_sku_mapping, how='left', left_on=a['custom_rom_version'],right_on=['custom_rom_version'],suffixes=('','_c'))
s3 = pd.merge(s2, d, how='left', left_on=a['asset_id'],right_on=['asset_id'],suffixes=('','_d'))

b=pd.concat([s3[list(mdm_devices_history.columns)],s3.sku.combine_first(s3.sku_c)],axis=1)
b['missing_mac_address']=s3['mac_address_d']

#getting c

ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)
ams_sf_assets_input['mac_address'].fillna('None',inplace=True)
c=ams_sf_assets_input.groupby('mac_address')[['sku']].first().reset_index()
c['mac_address']=c['mac_address'].str.upper().str.strip().str.replace(':','')

broadsign_hosts_history.primary_mac_address.combine_first(broadsign_hosts_history.secondary_mac_address).str.replace(':','').str.upper().str.strip()









