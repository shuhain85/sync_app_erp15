app_name = "sync_app_erp15"
app_title = "Sync App ERP15"
app_publisher = "Your Company"
app_description = "ERPNext v15 Sync App for Shop-HQ architecture"
app_email = "dev@example.com"
app_license = "MIT"

scheduler_events = {
    "cron": {
        "*/15 * * * *": [
            "sync_app_erp15.scripts.hq_sync.sync_hq_to_shops",
            "sync_app_erp15.scripts.shop_sync.sync_shop_to_hq"
        ]
    },
    "daily": [
        "sync_app_erp15.email_summary.send_daily_sync_summary"
    ]
}

# Include JS in desk
app_include_js = ["/assets/sync_app_erp15/sync_settings_client.js"]

# Link to custom JS for Sync Log
doctype_js = {
    "Sync Log": [
        "public/sync_log_list.js",
        "public/sync_log_form.js"
    ]
}

doc_events = {
    "Sync Log": {
        "after_insert": "sync_app_erp15.sync_hooks.after_insert"
    }
}
