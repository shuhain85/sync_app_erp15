app_name = "sync_erp_15"
app_title = "Sync ERP 15"
app_publisher = "Your Company"
app_description = "ERPNext HQ-Shop Synchronization Platform"
app_icon = "octicon octicon-sync"
app_color = "#33C9DC"
app_email = "support@example.com"
app_license = "MIT"

scheduler_events = {
    "hourly": ["sync_core.queue.process_sync_queue"]
}