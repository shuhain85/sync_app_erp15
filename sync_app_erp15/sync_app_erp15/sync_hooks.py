
import frappe
from sync_app_erp15.discord import send_discord_alert

def after_insert(doc, method):
    if doc.doctype != "Sync Log" or doc.sync_status != "Failed":
        return
    msg = f"❌ Failed Sync\nDoctype: {doc.doctype_name}\nRef: {doc.reference_docname}\nMessage: {doc.message}"
    send_discord_alert(msg)
