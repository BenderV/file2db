#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# USAGE INFORMATION:
# As you can see this text, you obviously have opened the file in a text editor.
#
# If you would like to *run* this example rather than *read* it, you
# should open Terminal.app, drag this document's icon onto the terminal
# window, bring Terminal.app to the foreground (if necessary) and hit return.
#

import Pashua
import os.path
from upload import upload

conf = u"""
# Set window title
*.title = File 2 DB
# INTRO
intro.type = text
intro.default = Automaticaly upload data file into your database without hassle.[return][return]File format supported: CSV | JSON | EXCEL[return]Database: PostgreSQL | MySQL | SQLite | Oracle | Microsoft SQL Server.
intro.height = 400
intro.width = 500
intro.tooltip = This is an element of type “text”
# DATABASE URI
uri.type = textfield
uri.label = URI of the database
uri.default = postgresql://localhost/defaultdb
uri.width = 500
# SCHEMA
schema.type = textfield
schema.label = schema
schema.default = 
# TABLE
table_name.type = textfield
table_name.label = table name
# CSV PATH
path.type = openbrowser
path.label = Select your file
path.width=500
path.tooltip = The file you want to import
"""

# Set the images' paths relative to Pashua.app's path
app_bundle = os.path.dirname(os.path.dirname(Pashua.locate_pashua()))

result = Pashua.run(conf.encode('utf8'))

print("Pashua returned the following dictionary keys and values:")

print(result)

for key in result.keys():
    print("%s = %s" % (key, result[key]))

upload(**result)
