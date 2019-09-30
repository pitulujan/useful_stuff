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
try:
	ams_sf_assets_input['created_date'] = ams_sf_assets_input['created_date'].apply(lambda x: datetime.date(x))
except Exception as e:
	if str(e) == "descriptor 'date' requires a 'datetime.datetime' object but received a 'datetime.date'":
		pass
	else:
		print(str(e))

ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)
ams_sf_assets_input['asset_tag'].fillna('None',inplace=True)
b=ams_sf_assets_input.groupby('asset_tag').agg({'sku':'first'}).reset_index()
#b=ams_sf_assets_input.groupby('asset_tag')[['sku']].first().reset_index()
b['asset_tag']=b['asset_tag'].str.upper() 

mdm_devices_history['asset_id'].fillna('None',inplace=True)
#mdm_devices_history['asset_id']=mdm_devices_history['asset_id'].str.upper()
#mdm_missing_mac_addresses['asset_id']=mdm_missing_mac_addresses['asset_id'].str.upper()


s1 = pd.merge(mdm_devices_history, b, how='left', left_on= [mdm_devices_history['asset_id'].str.upper()],right_on=['asset_tag'],suffixes=('_a','_b'))
#s1['custom_rom_version'].fillna('None',inplace=True)

#shared_mdm_custom_rom_sku_mapping['custom_rom_version'].fillna('None',inplace=True)
s2 = pd.merge(s1, shared_mdm_custom_rom_sku_mapping, how='left', left_on=['custom_rom_version'],right_on=['custom_rom_version'],suffixes=('','_c'))

#mdm_missing_mac_addresses['asset_id'].fillna('None',inplace=True)
s3 = pd.merge(s2, mdm_missing_mac_addresses, how='left', left_on=['asset_id'],right_on=['asset_id'],suffixes=('','_d'))
#s3.fillna('None').replace(to_replace='None',value=None,inplace=True)

b=pd.concat([s3[list(mdm_devices_history.columns)],s3.sku_c.combine_first(s3.sku)],axis=1)
b['missing_mac_address']=s3['mac_address_d']
b=b.rename(columns={'sku_c':'sku'})

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

#Getting d

def combine_first_str(x):
    if x == 'None':
        return 'P-WFI-101-MOJ-01'
    else:
        return x

ams_sf_assets_input=joblib.load('ams_sf_assets_input.h5')
ams_sf_assets_input['created_date'] = ams_sf_assets_input['created_date'].apply(lambda x: datetime.date(x))
ams_sf_assets_input.sort_values(['created_date'],ascending=False,inplace=True)

ams_sf_assets_input['asset_tag'].fillna('None',inplace=True)

cc=ams_sf_assets_input.groupby(ams_sf_assets_input['serial_number'].combine_first(ams_sf_assets_input['mac_address']).str.replace(':','').str.upper().str.strip().fillna('None')).agg({'asset_tag':'first','sku':'first'}).reset_index().drop_duplicates()
cc=cc.rename(columns={'serial_number':'mac_address'})


airtight_sensors_history['foo']=airtight_sensors_history['radio_macaddress'].str.replace(':','').str.upper().str.strip()
airtight_sensors_history['radio_macaddress'].fillna('None',inplace=True)
#airtight_sensors_history['export_date'] = airtight_sensors_history['export_date'].apply(lambda x: datetime.date(x)) ya esta en datetime
airtight_sensors_history['radio_upsince'] = airtight_sensors_history['radio_upsince'].apply(lambda x: datetime.date(x))
#airtight_sensors_history['export_hour'] = airtight_sensors_history['export_hour'].apply(lambda x: datetime.date(x)) ya esta en datetime

s1=pd.merge(airtight_sensors_history,ams_airtight_source_system_names, on='source', how='inner')



s2=pd.merge(s1,cc,how='left', right_on='mac_address', left_on='foo')

s2['sku'].fillna('None',inplace=True)
s2['sku']=s2['sku'].apply(combine_first_str)

s2.sort_values(['export_hour','radio_upsince'],ascending=[False,False])
d=s2.groupby(['radio_macaddress', 'export_date']).agg({'boxid':'first','source_system_name':'first','asset_tag':'first','sku':'first'}).reset_index()


#Getting the first general table a

shared_assets_history=joblib.load('shared_assets_history.h5')

s1=pd.merge(shared_assets_history,b,how='left',left_on=['cms_id','export_date'],right_on=['client_id','export_date'],suffixes=('_a','_b'))


s2=pd.merge(s1,c,how='left',left_on=['asset_name','cms_id','export_date',shared_assets_history['last_pinged_at'].combine_first(shared_assets_history['last_pinged_at'].fillna('1900-01-01'))],right_on=['name',c.display_unit_id.astype('str'),'export_date',c['last_pinged_at'].combine_first(c['last_pinged_at'].fillna('1900-01-01'))],suffixes=('','_c'))

s3=pd.merge(s2,d,how='left',left_on=['cms_id','export_date'],right_on=['radio_macaddress','export_date'],suffixes=('','_d'))

s3=s3[s3['cms_column'].isin(["client_id","display_unit_id","radio_macaddress"])]

a = s3[['asset_name','type','cmh_id','last_pinged_at','ssid','public_ip','created_at','installed_date','deleted_at','export_date']]
a= a.rename(columns={'asset_name':'source_system_asset_name','type':'product_use','public_ip':'public_ip_address'})

a['source_system'] = np.where(shared_assets_history['cms_column']=='client_id','mdm',np.where(shared_assets_history['cms_column']=='radio_macaddress',s3['source_system_name'],'broadsign'))

a['source_system_id'] = np.where(shared_assets_history['cms_column']=='client_id',s3['device_id'],np.where(shared_assets_history['cms_column']=='radio_macaddress',s3['boxid'],s3['host_id']))

a['product'] = np.where(s3['type'].isin(['Infusion Room Tablet','Rheumatology IRT']),'tablet',s3['type'])

a['device_location_status']=np.where(s3['status_a']=='Active','Installed',np.where(s3['deleted_at'].isnull(),'Deleted',np.where(s3['status_b']=='Demo','Demo',None)))

a['reason_for_deletion'] =np.where(s3['deleted_at'].notnull(),'Deleted by membership'.astype('str'),s3['deleted_at'])

a['sku'] = s3['sku'].combine_first(s3['sku_c']).combine_first(s3['sku_d'])
a['mac_address']=s3.mac_address.combine_first(s3.missing_mac_address).combine_first(s3.mac_address_c).combine_first(s3.radio_macaddress).str.upper().str.strip().str.replace(':','')



def search_regex(x):
    if x:
        if re.search('^[0-9]+$',x):
            return True
        else:
            return False
    else:
        return False

a['asset_tag'] = np.where((s3['asset_tag'].notnull()) & (s3['asset_id_a'].apply(search_regex)),s3['asset_id_a'],s3.asset_tag.combine_first(s3.asset_id_a)).str.upper().str.strp()



