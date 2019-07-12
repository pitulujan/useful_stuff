-data_engineer.airtight_sensors_history --> boxid,radio_macaddress,export_date,export_hour,radio_upsince,source
-data_engineer.ams_rules_input -->value,rule
-data_engineer.ams_bat_input --> wifi_mac_address,lan_mac_address,asset_tag,product,sku
-data_engineer.shared_sku_master -->sku,old_sku,rollup_sku_to_use,product

-data_engineer.shared_assets_history -->asset_id,asset_name,type,status,cmh_id,last_pinged_at,export_date,cms_id,cms_column --> export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')

-data_engineer.mdm_devices_history --> id,asset_id,custom_rom_version,device_id,client_id,status,mac_address,ssid,created_at,installed_date,deleted_at,export_date --> export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')

-data_engineer.ams_sf_assets_input --> asset_tag,sku,created_date,serial_number,mac_address

-data_engineer.shared_mdm_custom_rom_sku_mapping -->custom_rom_version

-data_engineer.mdm_missing_mac_addresses -->asset_id

-data_engineer.broadsign_hosts_history --> name,display_unit_id,host_id,primary_mac_address,secondary_mac_address,export_date --> export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')

-data_engineer.broadsign_monitor_polls_history -->poll_last_utc,public_ip,client_resource_id,export_date

-data_engineer.ams_broadsign_migration_devices_history --> bs_host_id,export_date -->WHERE d.bs_host_id IS NULL
-data_engineer.ams_cms_input_history -->source_system,source_system_id,export_date -->WHERE b.source_system_id IS NULL


SELECT boxid,radio_macaddress,export_date,export_hour,radio_upsince,source FROM data_engineer.airtight_sensors_history
SELECT value,rule FROM data_engineer.ams_rules_input
SELECT wifi_mac_address,lan_mac_address,asset_tag,product,sku FROM data_engineer.ams_bat_input
SELECT sku,old_sku,rollup_sku_to_use,product FROM data_engineer.shared_sku_master 
SELECT asset_id,asset_name,type,status,cmh_id,last_pinged_at,export_date,cms_id,cms_column FROM data_engineer.shared_assets_history WHERE export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
SELECT id,asset_id,custom_rom_version,device_id,client_id,status,mac_address,ssid,created_at,installed_date,deleted_at,export_date FROM data_engineer.mdm_devices_history WHERE export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
SELECT asset_tag,sku,created_date,serial_number,mac_address FROM data_engineer.ams_sf_assets_input
SELECT custom_rom_version FROM data_engineer.shared_mdm_custom_rom_sku_mapping
SELECT asset_id FROM data_engineer.mdm_missing_mac_addresses
SELECT name,display_unit_id,host_id,primary_mac_address,secondary_mac_address,export_date FROM data_engineer.broadsign_hosts_history WHERE export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
SELECT poll_last_utc,public_ip,client_resource_id,export_date FROM data_engineer.broadsign_monitor_polls_history
SELECT bs_host_id,export_date FROM data_engineer.ams_broadsign_migration_devices_history WHERE bs_host_id IS NULL
SELECT source_system,source_system_id,export_date FROM data_engineer.ams_cms_input_history WHERE source_system_id IS NULL























