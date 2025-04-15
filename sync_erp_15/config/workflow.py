import frappe

def get_workflows():
    return [
        {
            "doctype": "Sync Job Log",
            "workflow_name": "Sync Job Review",
            "states": [
                {"state": "Pending", "doc_status": 0},
                {"state": "Reviewed", "doc_status": 1},
                {"state": "Error", "doc_status": 1}
            ],
            "transitions": [
                {"state": "Pending", "action": "Mark Reviewed", "next_state": "Reviewed"},
                {"state": "Pending", "action": "Mark Error", "next_state": "Error"}
            ]
        }
    ]