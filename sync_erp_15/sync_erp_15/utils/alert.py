import requests
import frappe

def send_discord_alert(message):
    webhook_url = frappe.db.get_single_value("Sync Settings", "discord_webhook")
    if not webhook_url:
        return
    try:
        requests.post(webhook_url, json={"content": message})
    except Exception as e:
        frappe.log_error(str(e), "Discord Alert Failed")