import frappe

@frappe.whitelist()
def trigger_manual_sync():
    role = frappe.db.get_single_value("Sync Settings", "location_type")
    if role == "HQ":
        from sync_app_ERP15.scripts.hq_sync import sync_hq_to_shops
        sync_hq_to_shops()
    elif role == "Shop":
        from sync_app_ERP15.scripts.shop_sync import sync_shop_to_hq
        sync_shop_to_hq()
