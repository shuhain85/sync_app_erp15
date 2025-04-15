import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def receive_push(data):
    try:
        doc = frappe.get_doc({
            "doctype": "Sync Queue",
            "payload": data,
            "status": "Queued",
            "retry_count": 0
        })
        doc.insert(ignore_permissions=True)
        return {"status": "success", "message": "Data queued"}
    except Exception as e:
        frappe.log_error(str(e), "Push Receive Failed")
        return {"status": "error", "message": str(e)}