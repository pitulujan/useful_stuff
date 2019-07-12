WITH AMS_AIRTIGHT_SOURCE_SYSTEM_NAMES AS (
    SELECT DISTINCT A.SOURCE,
                    'at'|| DENSE_RANK() OVER (ORDER BY SOURCE ASC) AS SOURCE_SYSTEM_NAME
    FROM data_engineer.airtight_sensors_history A
    WHERE A.EXPORT_DATE = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
)

SELECT DISTINCT COALESCE(c.asset_tag, d.asset_tag, a.asset_tag) AS asset_tag,
       a.source_system,
       a.source_system_id,
       a.source_system_asset_name,
       COALESCE(c.product, d.product, e.product, f.product, g.product, a.product) AS product,
       CASE WHEN a.product_use IN ('Infusion Room Tablet','Rheumatology IRT') AND COALESCE(c.product, d.product, e.product, f.product, g.product, a.product) = 'Tablet' THEN a.product_use ELSE COALESCE(c.product, d.product, e.product, f.product, g.product, a.product) END AS product_use,
       a.cmh_id,
       a.device_location_status,
       a.last_pinged_at,
       COALESCE(c.wifi_mac_address,d.wifi_mac_address,d.lan_mac_address,e.wifi_mac_address,e.lan_mac_address,a.mac_address) AS mac_address,
       a.ssid,
       a.public_ip_address,
       COALESCE(c.sku, d.sku, e.sku, f.sku, g.sku, a.sku) AS sku,
       a.created_at,
       a.installed_date,
       a.deleted_at,
       a.reason_for_deletion,
       a.export_date
FROM (
    SELECT
            TRIM(UPPER(CASE WHEN d.asset_tag IS NOT NULL AND a.asset_id ~ '^A[0-9]+$' THEN a.asset_id --If the airtight name is good then use it
                    ELSE COALESCE(d.asset_tag,a.asset_id) --Else use the salesforce/airtight name. If not airtight use CMS name
                   END)) AS asset_tag
        ,   CASE WHEN cms_column = 'client_id' THEN 'mdm'
                 WHEN cms_column = 'radio_macaddress' THEN d.source_system_name
                 WHEN cms_column = 'display_unit_id' THEN 'broadsign'
            END AS source_system
        ,   CASE WHEN cms_column = 'client_id' THEN b.device_id
                 WHEN cms_column = 'radio_macaddress' THEN d.boxid
                 WHEN cms_column = 'display_unit_id' THEN c.host_id
            END AS source_system_id
        ,   a.asset_name AS source_system_asset_name
        ,   CASE  WHEN a.type IN ('Infusion Room Tablet','Rheumatology IRT') THEN 'Tablet'
                  ELSE a.type
            END AS product
        ,   a.type AS product_use
        ,   a.cmh_id
        ,   CASE WHEN a.status = 'Active' THEN 'Installed'
                 WHEN b.deleted_at IS NOT NULL THEN 'Deleted'
                 WHEN b.status = 'Demo' THEN 'Demo'
                 ELSE NULL::varchar
            END AS device_location_status
        ,   a.last_pinged_at
        ,   REPLACE(TRIM(UPPER(COALESCE(COALESCE(b.mac_address, b.missing_mac_address),c.mac_address,d.radio_macaddress))),':','') AS mac_address
        ,   b.ssid
        ,   c.public_ip AS public_ip_address
        ,   COALESCE(b.sku,c.sku,d.sku) AS sku
        ,   b.created_at
        ,   b.installed_date
        ,   b.deleted_at
        ,   CASE WHEN b.deleted_at IS NOT NULL THEN 'Deleted by membership' END::varchar(250) AS reason_for_deletion
        ,   a.export_date

    FROM data_engineer.shared_assets_history a

        LEFT JOIN (
                    SELECT
                            a.*
                        ,   COALESCE(c.sku, b.sku) AS sku
                        ,   d.mac_address as missing_mac_address

                    FROM data_engineer.mdm_devices_history a

                        LEFT JOIN (
                          
                      --      SELECT DISTINCT UPPER(a.asset_tag) AS ASSET_TAG,
                      --                      FIRST_VALUE(a.sku) OVER(PARTITION BY a.asset_tag ORDER BY a.created_date DESC ROWS UNBOUNDED PRECEDING) as sku
                      --      FROM data_engineer.ams_sf_assets_input a
                        ) b 
                        ON UPPER(a.asset_id) = b.asset_tag

                        LEFT JOIN data_engineer.shared_mdm_custom_rom_sku_mapping c
                        ON a.custom_rom_version = c.custom_rom_version

                        LEFT JOIN data_engineer.mdm_missing_mac_addresses d    -- Some duplicate records for assets in MDM with one of which not having a MAC address, make sure that gets assigned so can be flagged as dupe
                        ON a.asset_id = d.asset_id

                    WHERE a.export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
                  ) b
            ON a.cms_id = b.client_id
            AND a.export_date = b.export_date
            AND a.cms_column = 'client_id'

        LEFT JOIN (
                    SELECT
                            a.name
                        ,   a.display_unit_id
                        ,   b.poll_last_utc AS last_pinged_at
                        ,   a.host_id
                        ,   COALESCE(a.primary_mac_address,a.secondary_mac_address) AS mac_address
                        ,   b.public_ip
                        ,   COALESCE(NULLIF(c.sku,'Player'), CASE WHEN a.secondary_mac_address IS NOT NULL THEN 'P-PLA-102-NWA-01' ELSE 'P-PLA-101-NWA-01' END) AS sku --At the time of coding this was the only way to ascertain SKU from broadsign
                        ,   a.export_date

                    FROM data_engineer.broadsign_hosts_history a

                        LEFT JOIN data_engineer.broadsign_monitor_polls_history b
                        ON a.host_id = b.client_resource_id
                        AND a.export_date = b.export_date

                        LEFT JOIN
                        (
                         SELECT DISTINCT TRIM(UPPER(REPLACE(mac_address,':',''))) AS mac_address,
                                         FIRST_VALUE(a.sku) OVER(PARTITION BY mac_address ORDER BY created_date DESC ROWS UNBOUNDED PRECEDING) as sku
                           FROM data_engineer.ams_sf_assets_input a
                        ) c 
                        ON TRIM(UPPER(REPLACE(COALESCE(a.primary_mac_address,a.secondary_mac_address),':',''))) = c.mac_address

                        LEFT JOIN data_engineer.ams_broadsign_migration_devices_history d
                        ON a.host_id = cast(d.bs_host_id as bigint)
                        AND a.export_date = d.export_date

                    WHERE d.bs_host_id IS NULL AND a.export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
                 ) c --It was a mistake to make the cms_id for broadsign display_unit_it but now I need to live with it. Therefore the below complex join is required. Once we move to ods.devices most of these joins after the FROM will not be necessary
            ON a.asset_name = c.name
            AND a.cms_id = cast(c.display_unit_id as varchar)
            AND a.export_date = c.export_date
            AND COALESCE(a.last_pinged_at,'1900-01-01') = COALESCE(c.last_pinged_at,'1900-01-01')
            AND a.cms_column = 'display_unit_id'

        LEFT JOIN (
                SELECT DISTINCT
                            FIRST_VALUE(a.boxid) OVER (PARTITION BY a.radio_macaddress, a.export_date ORDER BY a.export_hour DESC, a.radio_upsince DESC ROWS UNBOUNDED PRECEDING) AS boxid
                        ,   FIRST_VALUE(b.source_system_name) OVER (PARTITION BY a.radio_macaddress, a.export_date ORDER BY a.export_hour DESC, a.radio_upsince DESC  ROWS UNBOUNDED PRECEDING) AS source_system_name
                        ,   a.export_date
                        ,   FIRST_VALUE(a.radio_macaddress) OVER (PARTITION BY a.radio_macaddress, a.export_date ORDER BY a.export_hour DESC, a.radio_upsince DESC  ROWS UNBOUNDED PRECEDING) AS radio_macaddress
                        ,   FIRST_VALUE(c.asset_tag) OVER (PARTITION BY a.radio_macaddress, a.export_date ORDER BY a.export_hour DESC, a.radio_upsince DESC  ROWS UNBOUNDED PRECEDING) AS asset_tag
                        ,   FIRST_VALUE(COALESCE(c.sku,'P-WFI-101-MOJ-01')) OVER (PARTITION BY a.radio_macaddress, a.export_date ORDER BY a.export_hour DESC, a.radio_upsince DESC  ROWS UNBOUNDED PRECEDING) AS sku

                FROM data_engineer.airtight_sensors_history a

                    INNER JOIN ams_airtight_source_system_names b
                    ON a.source = b.source

                    LEFT JOIN(
                          SELECT DISTINCT TRIM(UPPER(REPLACE(COALESCE(serial_number, mac_address),':',''))) AS mac_address,
                                        FIRST_VALUE(a.asset_tag) OVER(PARTITION BY TRIM(UPPER(REPLACE(COALESCE(serial_number, mac_address),':',''))) ORDER BY created_date DESC ROWS UNBOUNDED PRECEDING) as asset_tag,
                                        FIRST_VALUE(a.sku) OVER(PARTITION BY TRIM(UPPER(REPLACE(COALESCE(serial_number, mac_address),':',''))) ORDER BY created_date DESC ROWS UNBOUNDED PRECEDING) as sku
                          FROM data_engineer.ams_sf_assets_input a
                            ) c
                    ON TRIM(UPPER(REPLACE(a.radio_macaddress,':',''))) = c.mac_address

                WHERE a.export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
                    ) d
            ON a.cms_id = d.radio_macaddress
            AND a.export_date = d.export_date
            AND a.cms_column = 'radio_macaddress'

    WHERE a.export_date = (SELECT value::date FROM data_engineer.ams_rules_input WHERE rule = 'Rollforward date')
    ) a

    LEFT JOIN data_engineer.ams_cms_input_history b --Ensure this is unique by source_system, source_system_id, export_date
    ON a.source_system = b.source_system
    AND a.source_system_id = b.source_system_id
    AND a.export_date = b.export_date

    LEFT JOIN data_engineer.ams_bat_input c
    ON a.mac_address = c.wifi_mac_address

    LEFT JOIN data_engineer.ams_bat_input d
    ON a.mac_address = d.lan_mac_address

    LEFT JOIN data_engineer.ams_bat_input e
    ON a.asset_tag = e.asset_tag
    AND a.product = e.product
    AND a.mac_address IS NULL

    LEFT JOIN data_engineer.shared_sku_master f
    ON a.sku = f.sku

    LEFT JOIN data_engineer.shared_sku_master g
    ON a.sku = g.old_sku
    AND g.rollup_sku_to_use

WHERE b.source_system_id IS NULL and a.source_system_asset_name NOT IN ('\nT17105') -- custom addition for the exercise