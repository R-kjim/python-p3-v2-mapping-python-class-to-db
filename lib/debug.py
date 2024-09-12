#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

# import ipdb

# ipdb.set_trace()

Department.drop_table()
# print(CURSOR.execute("PRAGMA table_info(departments)").fetchall())
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
# print(payroll)
# payroll.save()  # Persist to db, assign object id attribute
payroll.delete()
print(payroll) 

hr = Department.create("Human Resources", "Building C, East Wing")
# print(hr) 
# hr.save()  # Persist to db, assign object id attribute
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update() #update the database
print(hr)




# print(CURSOR.execute("PRAGMA table_info(departments)").fetchall())
