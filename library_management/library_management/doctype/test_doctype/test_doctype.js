// Copyright (c) 2022, Muhammad Arsalan and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Test Doctype', {
// 	refresh: function(frm) {
// 		frm.add_custom_button(__('Get User Email Address'), function(){
// 			frappe.msgprint(frm.doc.customer);
// 		}), __("Utilities"));
// 	}
// });


frappe.ui.form.on('Test Doctype', {
    refresh: function(frm) {
    
      frm.add_custom_button(__('Get User Name'), function(){
        var d = new frappe.ui.Dialog({
          'fields': [
              {'fieldname': 'ht', 'fieldtype': 'HTML'},
              {'fieldname': 'today', 'fieldtype': 'Date', 'default': frappe.datetime.nowdate()}
          ],
          primary_action: function(){
              d.hide();
              show_alert(d.get_values());
          }
      });
      d.fields_dict.ht.$wrapper.html('Hello World');
      d.show();
        // frappe.msgprint("Hello " + frm.doc.customer);
        // frappe.show_alert('Hi, do you have a new message', 5);
      //   frappe.confirm(
      //     'Are you sure to leave this page?',
      //     function(){
      //         window.close();
      //     },
      //     function(){
      //         show_alert('Thanks for continue here!')
      //     }
      // )
    //   msgprint("<b>Server Status</b>"
    // + "<hr>"
    // + "<ul>"
    //         + "<li><b>28%</b> Memory</li>"
    //         + "<li><b>12%</b> Processor</li>"
    //         + "<li><b>0.3%</b> Disk</li>"
    // + "</ul>", 'Server Info')
    }, __("Utilities"));
    
  }
});