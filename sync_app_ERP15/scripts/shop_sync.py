import frappe

def sync_shop_to_hq():
    if frappe.db.get_single_value("Sync Settings", "location_type") != "Shop":
        frappe.logger().info("Not Shop - skipping Shop sync job.")
        return

    # Example: push new Sales Invoices to HQ
    frappe.logger().info("Running Shop -> HQ sync for Sales Invoices...")
    # Logic to collect unsynced invoices and send to HQ API
