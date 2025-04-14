frappe.ui.form.on('Sync Settings', {
    refresh: function(frm) {
        frm.add_custom_button(__('Sync Now'), function () {
            frappe.call({
                method: 'sync_app_erp15.utils.trigger_manual_sync',
                callback: function () {
                    frappe.show_alert('Manual sync triggered');
                }
            });
        });

        frm.add_custom_button(__('Backup Now'), function () {
            frappe.call({
                method: 'sync_app_erp15.scripts.backup_to_hq.generate_and_upload_backup',
                callback: function (r) {
                    if (!r.exc) {
                        frappe.msgprint(__('Backup uploaded to HQ.'));
                    }
                }
            });
        });

        // Auto-refresh dashboard and pie chart (existing content)
        // ...
    }
});
