app_name = "sync_app_ERP15"
app_title = "Sync App ERP15"
app_publisher = "Your Company"
app_description = "ERPNext v15 Sync App for Shop-HQ architecture"
app_email = "dev@example.com"
app_license = "MIT"

scheduler_events = {
    "cron": {
        "*/15 * * * *": [
            "sync_app_ERP15.scripts.hq_sync.sync_hq_to_shops",
            "sync_app_ERP15.scripts.shop_sync.sync_shop_to_hq"
        ]
    }
}
