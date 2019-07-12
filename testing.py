import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import joblib
import time 


def get_data_into_dataframes(dic_info,conn):

	dataframe_dic={}

	for key,value in dic_info.items():
		query='SELECT '+value+' FROM data_engineer.'+key
		dataframe_dic[key]=sqlio.read_sql_query(sql, conn)

	return dataframe_dic

if __name__ == '__main__':

	pd.options.display.max_colwidth = 200 

	conn = psycopg2.connect(host="data-interview.outcomehealth.io",
	                        port="5432",
	                        database="product_analytics", 
	                        user="pa_candidate", 
                        password="OsOntUnDleYeTivi")
	
	tables_columns={'airtight_sensors_history':'boxid,radio_macaddress,export_date,export_hour,radio_upsince,source',
					'ams_rules_input':'value,rule',
					'ams_bat_input':'wifi_mac_address,lan_mac_address,asset_tag,product,sku',
					'shared_sku_master': 'sku,old_sku,rollup_sku_to_use,product',
					'shared_assets_history': 'asset_id,asset_name,type,status,cmh_id,last_pinged_at,export_date,cms_id,cms_column',
					'mdm_devices_history':'id,asset_id,custom_rom_version,device_id,client_id,status,mac_address,ssid,created_at,installed_date,deleted_at,export_date',
					'ams_sf_assets_input': 'asset_tag,sku,created_date,serial_number,mac_address',
					'shared_mdm_custom_rom_sku_mapping' : 'custom_rom_version',
					'mdm_missing_mac_addresses': 'asset_id',
					'broadsign_hosts_history':'name,display_unit_id,host_id,primary_mac_address,secondary_mac_address,export_date',
					'broadsign_monitor_polls_history': 'poll_last_utc,public_ip,client_resource_id,export_date',
					'ams_broadsign_migration_devices_history': 'bs_host_id,export_date',
					'ams_cms_input_history': 'source_system,source_system_id,export_date'}

	#dataframe_dic=get_data_into_dataframes(tables_columns,conn)


airtight_sensors_history="SELECT boxid,radio_macaddress,export_date,export_hour,radio_upsince,source FROM data_engineer.airtight_sensors_history WHERE EXPORT_DATE = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')"
ams_rules_input='SELECT value,rule FROM data_engineer.ams_rules_input'
ams_bat_input='SELECT wifi_mac_address,lan_mac_address,asset_tag,product,sku FROM data_engineer.ams_bat_input'
shared_sku_master='SELECT sku,old_sku,rollup_sku_to_use,product FROM data_engineer.shared_sku_master' 
shared_assets_history="SELECT asset_id,asset_name,type,status,cmh_id,last_pinged_at,export_date,cms_id,cms_column FROM data_engineer.shared_assets_history WHERE export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')"
mdm_devices_history="SELECT id,asset_id,custom_rom_version,device_id,client_id,status,mac_address,ssid,created_at,installed_date,deleted_at,export_date FROM data_engineer.mdm_devices_history WHERE export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')"
ams_sf_assets_input='SELECT asset_tag,sku,created_date,serial_number,mac_address FROM data_engineer.ams_sf_assets_input'
shared_mdm_custom_rom_sku_mapping='SELECT custom_rom_version FROM data_engineer.shared_mdm_custom_rom_sku_mapping'
mdm_missing_mac_addresses='SELECT asset_id FROM data_engineer.mdm_missing_mac_addresses'
broadsign_hosts_history="SELECT name,display_unit_id,host_id,primary_mac_address,secondary_mac_address,export_date FROM data_engineer.broadsign_hosts_history WHERE export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')"
broadsign_monitor_polls_history='SELECT poll_last_utc,public_ip,client_resource_id,export_date FROM data_engineer.broadsign_monitor_polls_history'
ams_broadsign_migration_devices_history='SELECT bs_host_id,export_date FROM data_engineer.ams_broadsign_migration_devices_history WHERE bs_host_id IS NULL'
ams_cms_input_history='SELECT source_system,source_system_id,export_date FROM data_engineer.ams_cms_input_history WHERE source_system_id IS NULL'

query_list=[airtight_sensors_history,ams_rules_input,ams_bat_input,shared_sku_master,mdm_devices_history,ams_sf_assets_input,shared_mdm_custom_rom_sku_mapping,mdm_missing_mac_addresses,broadsign_hosts_history,broadsign_monitor_polls_history,ams_broadsign_migration_devices_history,ams_cms_input_history]
#joblib.dump(dataframe_dic,'dataframe_dic.h5')
start=time.time()
dataframe_dic={}
for idx,query in enumerate(query_list):
	dataframe_dic[idx]=sqlio.read_sql_query(query, conn)
end=time.time()

print('time taken', end-start)

#joblib.dump(dataframe_dic,'probando_data_con_filtro.h5')
