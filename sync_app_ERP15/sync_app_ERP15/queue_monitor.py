
import frappe
import redis
import json
from frappe.utils import now_datetime

@frappe.whitelist()
def get_queue_stats():
    r = redis.Redis.from_url(frappe.conf.redis_queue)
    try:
        stats = {
            "queued": r.llen("default"),
            "failed": r.llen("failed"),
            "last_processed": r.get("sync:last_processed") or "No jobs yet"
        }
        if isinstance(stats["last_processed"], bytes):
            stats["last_processed"] = stats["last_processed"].decode()
    except Exception as e:
        stats = {"error": str(e)}
    return stats
