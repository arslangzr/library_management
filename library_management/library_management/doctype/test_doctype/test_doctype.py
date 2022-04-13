# -*- coding: utf-8 -*-
# Copyright (c) 2022, Muhammad Arsalan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from sys import prefix
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import getseries


class TestDoctype(WebsiteGenerator):
	def autoname(self):
		# prefix = `P-{}`.format(self.customer)
		self.name = ("Test - " + self.customer + " - " + getseries(prefix,3))
	# pass
	# def on_update(self):
	# 	frappe.throw(self.name)

	# throw exception before save
	# def validate(self):
	# 	frappe.throw("Validate method called")
	def on_trash(self):
		frappe.throw("Document deleted")

