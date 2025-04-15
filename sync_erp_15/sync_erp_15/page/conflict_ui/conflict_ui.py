import frappe

@frappe.whitelist()
def get_conflicts():
    return frappe.get_all("Conflict Log", filters={"resolved": 0})