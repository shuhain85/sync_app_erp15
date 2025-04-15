frappe.pages['conflict-ui'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Conflict Resolution',
        single_column: true
    });

    $(wrapper).html('<div class="conflict-ui">Conflict Resolution UI Coming Soon</div>');
};