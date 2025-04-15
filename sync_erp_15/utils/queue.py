import frappe
from sync_erp_15.utils.sync_utils import push_data_to_hq
from sync_erp_15.utils.log_helper import log_sync_event

def process_sync_queue():
    queue_items = frappe.get_all("Sync Queue", filters={"status": "Queued"})
    for item in queue_items:
        doc = frappe.get_doc("Sync Queue", item.name)
        try:
            result = push_data_to_hq(frappe.parse_json(doc.payload))
            doc.status = "Completed"
            doc.save()
            log_sync_event("Push", "Success", f"Queue ID {doc.name} processed")
        except Exception as e:
            doc.status = "Failed"
            doc.retry_count += 1
            doc.save()
            log_sync_event("Push", "Failed", str(e))