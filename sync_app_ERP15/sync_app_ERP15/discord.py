
import requests
import frappe

def send_discord_alert(message, title='🚨 Sync Alert', webhook_url=None):
    if not webhook_url:
        webhook_url = frappe.db.get_single_value("Sync Settings", "discord_webhook_url")
    if not webhook_url:
        frappe.logger().info("Discord webhook not configured.")
        return

    payload = {
        "username": "SyncBot",
        "embeds": [{
            "title": title,
            "description": message,
            "color": 15158332  # Red
        }]
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        frappe.logger().error(f"Failed to send Discord alert: {str(e)}")
