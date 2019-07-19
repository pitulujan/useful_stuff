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
ams_broadsign_migration_devices_history=joblib.load('ams_broadsign_migration_devices_history.h5')
ams_cms_input_history=joblib.load('ams_cms_input_history.h5')

#Getting ams_airtight_source_system_names

ams_airtight_source_system_names = pd.DataFrame()
ams_airtight_source_system_names['source'] = airtight_sensors_history['source'].drop_duplicates()
ams_airtight_source_system_names['source_system_name'] ='at'+airtight_sensors_history.source.rank(method='dense').astype('int').astype('str')
ams_airtight_source_system_names.reset_index(drop=True,inplace=True)


#Getting b
ams_sf_assets_input['created_date'] = ams_sf_assets_input['created_date'].apply(lambda x: datetime.date(x))
ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)
ams_sf_assets_input['asset_tag'].fillna('None',inplace=True)
b=ams_sf_assets_input.groupby('asset_tag').agg({'sku':'first'}).reset_index()
#b=ams_sf_assets_input.groupby('asset_tag')[['sku']].first().reset_index()
b['asset_tag']=b['asset_tag'].str.upper() 

mdm_devices_history['asset_id'].fillna('None',inplace=True)
mdm_devices_history['asset_id']=mdm_devices_history['asset_id'].str.upper()
mdm_missing_mac_addresses['asset_id']=mdm_missing_mac_addresses['asset_id'].str.upper()


s1 = pd.merge(mdm_devices_history, b, how='left', left_on= ['asset_id'],right_on=['asset_tag'],suffixes=('_a','_b'))
#s1['custom_rom_version'].fillna('None',inplace=True)

#shared_mdm_custom_rom_sku_mapping['custom_rom_version'].fillna('None',inplace=True)
s2 = pd.merge(s1, shared_mdm_custom_rom_sku_mapping, how='left', left_on=['custom_rom_version'],right_on=['custom_rom_version'],suffixes=('','_c'))

#mdm_missing_mac_addresses['asset_id'].fillna('None',inplace=True)
s3 = pd.merge(s2, mdm_missing_mac_addresses, how='left', left_on=['asset_id'],right_on=['asset_id'],suffixes=('','_d'))
#s3.fillna('None').replace(to_replace='None',value=None,inplace=True)

b=pd.concat([s3[list(mdm_devices_history.columns)],s3.sku_c.combine_first(s3.sku)],axis=1)
b['missing_mac_address']=s3['mac_address_d']

#getting c
ams_sf_assets_input['created_date'] = ams_sf_assets_input['created_date'].apply(lambda x: datetime.date(x))

ams_sf_assets_input = joblib.load('ams_sf_assets_input.h5')
ams_sf_assets_input['created_date'] = ams_sf_assets_input['created_date'].apply(lambda x: datetime.date(x))
ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)
ams_sf_assets_input['mac_address'].fillna('None',inplace=True)
c=ams_sf_assets_input.groupby('mac_address').agg({'sku':'first'}).reset_index()


s1 = pd.merge(broadsign_hosts_history, broadsign_monitor_polls_history, how='left', left_on=['host_id','export_date'],right_on=['client_resource_id','export_date'],suffixes=('_a','_b'))
s2 = pd.merge(s1, c, how='left', left_on=[broadsign_hosts_history.primary_mac_address.combine_first(broadsign_hosts_history.secondary_mac_address).str.replace(':','').str.upper().str.strip()],right_on=['mac_address'],suffixes=('','_c'))
s3 = pd.merge(s2, ams_broadsign_migration_devices_history, how='left', left_on=[broadsign_hosts_history['host_id'],broadsign_hosts_history['export_date']],right_on=[ams_broadsign_migration_devices_history.bs_host_id.astype('int64'),'export_date'],suffixes=('','_d'))

def case(x):
    if x == None:
        return 'P-PLA-101-NWA-01'
    else:
        return 'P-PLA-102-NWA-01'

def nullif(x):
	if x == 'Player':
		return None
	else:
		return x


s3['secondary_mac_address'].fillna('None').replace(to_replace='None',value=None,inplace=True)

c=pd.concat([s3[['name','display_unit_id','poll_last_utc','host_id','public_ip','export_date']],s3.primary_mac_address.combine_first(s3.secondary_mac_address)],axis=1)
c = c.rename(columns={'poll_last_utc': 'last_pinged_at','primary_mac_address':'mac_address'})

s3['sku'].fillna('None').replace(to_replace='None',value=None,inplace=True)
c['sku'] = s3['sku'].apply(nullif).combine_first(s3['secondary_mac_address'].apply(case))



ams_sf_assets_input['created_date'] = ams_sf_assets_input['created_date'].apply(lambda x: datetime.date(x))
ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)

c=ams_sf_assets_input.groupby(ams_sf_assets_input['serial_number'].combine_first(ams_sf_assets_input['mac_address']).str.replace(':','').str.upper().str.strip().fillna('None'))[['asset_tag','sku']].agg({'asset_tag':'first','sku':'first'}).reset_index()
c=c.rename(columns={'serial_number':'mac_address'})

b=ams_sf_assets_input.groupby(ams_sf_assets_input['serial_number'].combine_first(ams_sf_assets_input['mac_address']).str.replace(':','').str.upper().str.strip().fillna('None'))[['asset_tag','sku']].first().reset_index()
b=b.rename(columns={'serial_number':'mac_address'})



ams_sf_assets_input = joblib.load('ams_sf_assets_input.h5')
ams_sf_assets_input['created_date'] = ams_sf_assets_input['created_date'].apply(lambda x: datetime.date(x))
ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)
c=ams_sf_assets_input.groupby(ams_sf_assets_input['serial_number'].combine_first(ams_sf_assets_input['mac_address']).str.replace(':','').str.upper().str.strip().fillna('None')).agg({'sku':'first'}).reset_index()
c['asset_tag']=ams_sf_assets_input.groupby(ams_sf_assets_input['serial_number'].combine_first(ams_sf_assets_input['mac_address']).str.replace(':','').str.upper().str.strip().fillna('None')).agg({'asset_tag':'first'}).reset_index()['asset_tag']
c=c.rename(columns={'serial_number':'mac_address'})