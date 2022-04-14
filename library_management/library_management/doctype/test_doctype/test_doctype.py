# -*- coding: utf-8 -*-
# Copyright (c) 2022, Muhammad Arsalan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from sys import prefix
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import getseries
from pyparsing import autoname_elements


class TestDoctype(WebsiteGenerator):
	def autoname(self):
		# prefix = `P-{}`.format(self.customer)
		self.name = ("Test - " + self.customer + " - " + getseries(prefix,3))
	# pass
	def on_update(self):
		todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
		todo.insert()
	# 	frappe.throw(self.name)

	# throw exception before save
	# def validate(self):
	# 	frappe.throw("Validate method called")
	def on_trash(self):
		autoname_elements()
		frappe.throw("Document deleted")
		frappe.delete_doc("Test Doctype", ("Test - " + self.customer + " - " + getseries(prefix,3)))

