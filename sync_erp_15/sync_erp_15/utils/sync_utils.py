import requests
import frappe

def push_data_to_hq(data):
    settings = frappe.get_single("Sync Settings")
    headers = {"Authorization": f"Bearer {settings.hq_token}"}
    try:
        response = requests.post(settings.hq_url, json=data, headers=headers)
        return response.json()
    except Exception as e:
        frappe.log_error(str(e), "Sync Push Error")
        raise

def pull_data_from_hq():
    settings = frappe.get_single("Sync Settings")
    headers = {"Authorization": f"Bearer {settings.hq_token}"}
    try:
        response = requests.get(settings.hq_url, headers=headers)
        return response.json()
    except Exception as e:
        frappe.log_error(str(e), "Sync Pull Error")
        raise