import frappe


def after_install():
    add_custom_fields_to_address()
    add_custom_fields_to_sales_order()
    add_custom_fields_to_customer()
    add_custom_fields_to_item()


def add_custom_fields_to_address():
    custom_fields = [
        {
            "doctype": "Custom Field",
            "dt": "Address",
            "fieldname": "woocommerce_identifier",
            "fieldtype": "Data",
            "label": "Woocommerce Identifier",
            "module": "WooCommerce",
            "name": "Address-woocommerce_identifier",
            "print_hide": 1,
            "read_only": 1,
        },
    ]

    add_custom_fields("Address", custom_fields)


def add_custom_fields_to_sales_order():
    custom_fields = [
        {
            "depends_on": "eval: doc.woocommerce_id",
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "woocommerce_shipment_tracking_html",
            "fieldtype": "HTML",
            "module": "WooCommerce",
            "name": "Sales Order-woocommerce_shipment_tracking_html",
        },
        {
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "woocommerce_id",
            "fieldtype": "Data",
            "insert_after": "woocommerce_site",
            "label": "Woocommerce ID",
            "module": "WooCommerce",
            "name": "Sales Order-woocommerce_id",
            "print_hide": 1,
            "read_only": 1,
        },
        {
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "custom_woocommerce_customer_note",
            "fieldtype": "Small Text",
            "hide_days": 1,
            "hide_seconds": 1,
            "insert_after": "amended_from",
            "label": "WooCommerce Customer Note",
            "module": "WooCommerce",
            "name": "Sales Order-custom_woocommerce_customer_note",
            "read_only": 1,
            "width": "100px",
        },
        {
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "woocommerce_payment_method",
            "fieldtype": "Data",
            "insert_after": "woocommerce_status",
            "label": "WooCommerce Payment Method",
            "module": "WooCommerce",
            "name": "Sales Order-woocommerce_payment_method",
            "read_only": 1,
        },
        {
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "custom_woocommerce_last_sync_hash",
            "fieldtype": "Datetime",
            "insert_after": "woocommerce_server",
            "label": "Last Sync Hash",
            "module": "WooCommerce",
            "name": "Sales Order-custom_woocommerce_last_sync_hash",
            "read_only": 1,
        },
        {
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "woocommerce_server",
            "fieldtype": "Link",
            "insert_after": "custom_attempted_woocommerce_auto_payment_entry",
            "label": "Woocommerce Server",
            "modified": "2023-11-15 08:01:54.789280",
            "module": "WooCommerce",
            "name": "Sales Order-woocommerce_server",
            "options": "WooCommerce Server",
            "read_only": 1,
        },
        {
            "allow_on_submit": 1,
            "description": "Checked if the sync process determined that no Payment Entry will be created for this Order automatically",
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "custom_attempted_woocommerce_auto_payment_entry",
            "fieldtype": "Check",
            "hidden": 1,
            "insert_after": "woocommerce_payment_entry",
            "label": "Attempted WooCommerce Auto Payment Entry",
            "module": "WooCommerce",
            "name": "Sales Order-custom_attempted_woocommerce_auto_payment_entry",
        },
        {
            "allow_on_submit": 1,
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "woocommerce_payment_entry",
            "fieldtype": "Link",
            "insert_after": "woocommerce_payment_method",
            "label": "Woocommerce Payment Entry",
            "module": "WooCommerce",
            "name": "Sales Order-woocommerce_payment_entry",
            "options": "Payment Entry",
        },
        {
            "allow_on_submit": 1,
            "doctype": "Custom Field",
            "dt": "Sales Order",
            "fieldname": "woocommerce_status",
            "fieldtype": "Select",
            "in_list_view": 1,
            "insert_after": "woocommerce_id",
            "label": "Woocommerce Status",
            "module": "WooCommerce",
            "name": "Sales Order-woocommerce_status",
            "options": "\nPending Payment\nOn hold\nFailed\nCancelled\nProcessing\nRefunded\nShipped\nReady for Pickup\nPicked up\nDelivered\nProcessing LP\nDraft\nQuote Sent\nTrash\nPartially Shipped",
            "width": "3",
        },
    ]

    add_custom_fields("Sales Order", custom_fields)


def add_custom_fields_to_customer():
    custom_fields = [
        {
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "woocommerce_identifier",
            "fieldtype": "Data",
            "in_list_view": 1,
            "is_system_generated": 1,
            "label": "Woocommerce Identifier",
            "module": "WooCommerce",
            "name": "Customer-woocommerce_identifier",
            "print_hide": 1,
            "read_only": 1,
            "translatable": 1,
        },
        {
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "woocommerce_is_guest",
            "fieldtype": "Check",
            "in_list_view": 1,
            "is_system_generated": 1,
            "label": "Woocommerce guest user",
            "module": "WooCommerce",
            "name": "Customer-woocommerce_is_guest",
            "print_hide": 1,
            "read_only": 1,
        },
        {
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "woocommerce_server",
            "fieldtype": "Link",
            "insert_after": "woocommerce_site",
            "label": "Woocommerce Server",
            "module": "WooCommerce",
            "name": "Customer-woocommerce_server",
            "options": "WooCommerce Server",
            "read_only": 1,
        },
    ]
    add_custom_fields("Customer", custom_fields)


def add_custom_fields_to_item():
    custom_fields = [
        {
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "custom_woocommerce_tab",
            "fieldtype": "Tab Break",
            "insert_after": "serial_no_series",
            "label": "WooCommerce",
            "module": "WooCommerce",
            "name": "Item-custom_woocommerce_tab",
        },
        {
            "description": "To create this item in WooCommerce, leave the WooCommerce ID field blank",
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "woocommerce_servers",
            "fieldtype": "Table",
            "insert_after": "custom_woocommerce_tab",
            "module": "WooCommerce",
            "name": "Item-woocommerce_servers",
            "options": "Item WooCommerce Server",
        },
    ]
    add_custom_fields("Item", custom_fields)


def add_custom_fields(doctype, fields):
    for field in fields:
        if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": field["fieldname"]}):
            new_field = frappe.get_doc({"doctype": "Custom Field", **field})
            new_field.insert()
            frappe.db.commit()
