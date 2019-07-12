data_engineer.ams_sf_assets_input --> asset_tag,sku,created_date,serial_number,mac_address
data_engineer.shared_mdm_custom_rom_sku_mapping -->custom_rom_version
data_engineer.mdm_missing_mac_addresses -->asset_id

data_engineer.shared_assets_history -->asset_id,asset_name,type,status,cmh_id,last_pinged_at,export_date,cms_id,cms_column

data_engineer.broadsign_hosts_history --> name,display_unit_id,host_id,primary_mac_address,secondary_mac_address,export_date,asset_name,cms_id,last_pinged_at,cms_column
data_engineer.broadsign_monitor_polls_history -->client_resource_id,export_date

-data_engineer.airtight_sensors_history --> boxid,radio_macaddress,export_date,export_hour,radio_upsince,source,cms_id,cms_column, """"""""""""source_system_id"""""""""""" (ver final query)

data_engineer.ams_cms_input_history -->source_system,source_system_id,export_date

-data_engineer.ams_bat_input --> wifi_mac_address,lan_mac_address,asset_tag,product,sku

data_engineer.shared_sku_master -->sku,old_sku,rollup_sku_to_use,product

data_engineer.ams_rules_input -->value,rule

data_engineer.mdm_devices_history --> asset_id,custom_rom_version,device_id,client_id,status,mac_address,ssid,created_at,installed_date,deleted_at,export_date
