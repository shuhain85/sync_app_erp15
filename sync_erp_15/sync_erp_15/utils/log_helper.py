import frappe

def log_sync_event(job_type, status, message):
    log = frappe.get_doc({
        "doctype": "Sync Job Log",
        "job_type": job_type,
        "status": status,
        "error_log": message
    })
    log.insert(ignore_permissions=True)