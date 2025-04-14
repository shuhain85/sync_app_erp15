frappe.listview_settings['Sync Log'] = {
    add_fields: ['sync_status', 'sync_direction', 'doctype_name', 'timestamp'],
    filters: [['sync_status', '!=', 'Success']],
    onload: function(listview) {
        listview.page.add_inner_button('Show All Logs', () => {
            listview.filter_area.clear();
            listview.refresh();
        });
    }
};
