from frappe import _

def get_data():
    return [
        {
            "module_name": "Sync ERP 15",
            "label": _("Sync ERP 15"),
            "icon": "octicon octicon-sync",
            "type": "module",
            "color": "#33C9DC",
            "description": _("ERPNext HQ-Shop Synchronization")
        }
    ]