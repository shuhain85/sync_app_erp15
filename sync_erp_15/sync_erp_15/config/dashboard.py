from frappe import _

def get_data():
    return {
        "fieldname": "reference_name",
        "transactions": [
            {
                "label": _("Sync Monitoring"),
                "items": ["Sync Job Log", "Conflict Log"]
            }
        ]
    }