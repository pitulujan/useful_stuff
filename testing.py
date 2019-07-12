import pandas as pd
import pandas.io.sql as sqlio
import psycopg2



def get_data_into_dataframes(dic_info,conn):

	dataframe_dic={}

	for key,value in dic_info.items():
		query='SELECT '+value+' FROM data_engineer.'+key
		print(query)

if __name__ == '__main__':

	pd.options.display.max_colwidth = 200 

	conn = psycopg2.connect(host="data-interview.outcomehealth.io",
	                        port="5432",
	                        database="product_analytics", 
	                        user="pa_candidate", 
	                        password="OsOntUnDleYeTivi")

	tables_columns={'airtight_sensors_history':'boxid,radio_macaddress,export_date,export_hour,radio_upsince,source,cms_id,cms_column',
					'ams_rules_input':'value,rule',
					'ams_bat_input':'wifi_mac_address,lan_mac_address,asset_tag,product,sku',
					'shared_sku_master': 'sku,old_sku,rollup_sku_to_use,product',
					'shared_assets_history': 'asset_id,asset_name,type,status,cmh_id,last_pinged_at,export_date,cms_id,cms_column',
					'mdm_devices_history':'id,asset_id,custom_rom_version,device_id,client_id,status,mac_address,ssid,created_at,installed_date,deleted_at,export_date',
					'ams_sf_assets_input': 'asset_tag,sku,created_date,serial_number,mac_address',
					'shared_mdm_custom_rom_sku_mapping' : 'custom_rom_version',
					'mdm_missing_mac_addresses': 'asset_id',
					'broadsign_hosts_history':'name,display_unit_id,host_id,primary_mac_address,secondary_mac_address,export_date,asset_name,cms_id,last_pinged_at,cms_column',
					'broadsign_monitor_polls_history': 'poll_last_utc,public_ip,client_resource_id,export_date',
					'ams_broadsign_migration_devices_history': 'bs_host_id,export_date',
					'ams_cms_input_history': 'source_system,source_system_id,export_date'}
	get_data_into_dataframes(tables_columns,conn)