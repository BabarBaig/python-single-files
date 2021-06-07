#! /usr/bin/python
import re
import datetime

output_string = """
Thu Nov  5 14:33:46 2020 | INFO | Instrument S/N: 30874-20-21-01546 | HW: 50504 | Platform: V5E2 | CPLD: 0.38
Thu Nov  5 14:33:46 2020 | INFO | Heater already off
Thu Nov  5 14:33:46 2020 | INFO | Sent Instrument data status : WipeIdx: 0 | FileExistByte: 0x00 (No system data) | LastSavedTestSeqNum :     0
Thu Nov  5 14:33:53 2020 | INFO | Heater already off
STATUS=0, RSP:{TYPE:file, STATUS:OK_STATUS, PAYLOAD:{}}
"""
print(len(output_string.splitlines()))
print("*"*80)
def _get_date_baseline():
    today = datetime.datetime.now()
    day_mon_date = today.strftime('%a %b %-d')
    yyyy = today.strftime('%Y')
    return (day_mon_date, yyyy)

print(_get_date_baseline())
print("*"*80)
match_string = "Heater already off"

print("*"*60)
print("Using 'in' method")
for line_number, line in enumerate(output_string.splitlines()):
    in_line = match_string in line
    print("{}: {}".format(line_number, in_line))
    if in_line:
        print("\t{}".format(line))

print("*"*60)
day_m_d, yyyy = _get_date_baseline()
regex_search = day_m_d + "\s\d{2}:\d{2}:\d{2}\s" + yyyy + " | INFO | " + match_string
print("Match string {}".format(regex_search))
print("Using 're' module")
for line_number, line in enumerate(output_string.splitlines()):
    pass
