frappe.pages['sync-dashboard'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Sync Dashboard',
        single_column: true
    });

    page.set_primary_action('Run Sync Now', () => {
        frappe.call('sync_erp_15.api.sync_now', {
            callback: function(r) {
                frappe.msgprint('Sync triggered');
            }
        });
    });

    $(wrapper).html('<div class="sync-status">Sync Dashboard UI Coming Soon</div>');
};