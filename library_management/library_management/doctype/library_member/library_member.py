# -*- coding: utf-8 -*-
# Copyright (c) 2022, Muhammad Arsalan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

# Method starting point

class LibraryMember(Document):
    #this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'

# Method Ending Point

# class LibraryMember(Document):
# 	pass
