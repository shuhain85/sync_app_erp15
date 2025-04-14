frappe.ui.form.on('Sync Log', {
    refresh(frm) {
        if (frm.doc.sync_status === 'Failed') {
            frm.add_custom_button(__('Retry Sync'), function () {
                frappe.call({
                    method: 'sync_app_erp15.retry.retry_failed_log',
                    args: { logname: frm.doc.name },
                    callback: function (r) {
                        if (!r.exc) {
                            frappe.show_alert(__('Retry triggered.'));
                            frm.reload_doc();
                        }
                    }
                });
            });
        }
    }
});
