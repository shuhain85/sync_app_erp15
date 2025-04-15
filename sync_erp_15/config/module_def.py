from frappe import _

def get_module_list():
    return [
        {
            "module_name": "Sync ERP 15",
            "category": "Modules",
            "label": _("Sync ERP 15"),
            "color": "#33C9DC",
            "icon": "octicon octicon-sync",
            "type": "module",
            "description": "ERPNext HQ-Shop Synchronization"
        }
    ]