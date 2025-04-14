app_name = "sync_app_ERP15"
app_title = "Sync App"
app_publisher = "Your Company"
app_description = "Shop-HQ ERPNext Sync App"
app_email = "dev@example.com"
app_license = "MIT"

# Scheduler events
scheduler_events = {
    "cron": {
        "*/15 * * * *": [
            "sync_app.scripts.pull_shop_data.auto_sync_enabled_shops",
            "sync_app.scripts.push_master_data.sync_hq_to_shops"
        ]
    }
}
