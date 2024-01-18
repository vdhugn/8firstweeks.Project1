import sys
import re

s = sys.stdin.readline().split()
date_str = "".join(s)

def extract_date(date_string):
  pattern = r"^\d{4}-\d{2}-\d{2}$"
  if not re.match(pattern, date_string):
    print("INCORRECT")
  else:
    year, month, day = date_string.split("-")
    if int(day) > 31 or int(month)> 12:
      print("INCORRECT")
    else:
      print(int(year), int(month), int(day))

extract_date(date_str)
