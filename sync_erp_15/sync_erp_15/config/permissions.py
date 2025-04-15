import frappe

def get_permissions():
    return {
        "Sync Settings": {
            "System Manager": ["read", "write"],
            "Shop Manager": ["read"]
        },
        "Sync Job Log": {
            "System Manager": ["read", "write", "create"],
            "Shop Manager": ["read"]
        }
    }