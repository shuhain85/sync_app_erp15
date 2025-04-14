import frappe

def sync_hq_to_shops():
    if frappe.db.get_single_value("Sync Settings", "location_type") != "HQ":
        frappe.logger().info("Not HQ - skipping HQ sync job.")
        return

    # Example: send updated Item Prices to all connected shops
    frappe.logger().info("Running HQ -> Shop sync for Item Prices...")
    # Logic to pull Item Price changes and POST to shops goes here
