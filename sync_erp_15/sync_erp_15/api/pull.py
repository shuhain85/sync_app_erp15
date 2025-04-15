import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_data_to_sync():
    # Dummy example: return all unsynced data from a placeholder Doctype
    return frappe.get_all("Item", filters={"disabled": 0}, fields=["name", "item_code"])