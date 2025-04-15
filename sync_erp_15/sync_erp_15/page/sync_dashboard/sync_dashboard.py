import frappe

@frappe.whitelist()
def get_stats():
    return {
        "last_sync": "2024-04-15 08:30:00",
        "success_rate": "98%",
        "pending_jobs": 3,
        "failed_jobs": 1
    }

@frappe.whitelist()
def sync_now():
    return "Triggered"