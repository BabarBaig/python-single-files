"""
Modules are simply Python files.  Nothing more.
If we have 2 modules in the same folder, we can load a class from one module for use in the other.
Use the 'import' command to do this.
Suppose we have a module database.py and another module query.py.  In the latter, add code:
import database
db = database.Database()
db.query(...)
===============================
As the number of modules grows, we'll want to organize them into folders, called 'Package's.
A package is a collection of modules in a folder.
Name of the package is the name of the folder.
In order to distinguish a package folder from an ordinary folder, place an empty __init__.py in
that folder (like this file).
If a folder doesn't have an __init__.py file, we won't be able to import modules from that folder.
Look at the files in this workspace.  They show correct syntax for absolute and relative imports.
"""