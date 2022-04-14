// Copyright (c) 2022, Muhammad Arsalan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Bank Reconciliation", "onload", function(frm) {
    frm.set_query("name1", function() {
        return {
            "filters": {
                "account_type": "Bank",
                "group_or_ledger": "Ledger"
            }
        };
    });
});

// frappe.ui.form.on('Bank Reconciliation', {
// 	// refresh: function(frm) {

// 	// }
// });
