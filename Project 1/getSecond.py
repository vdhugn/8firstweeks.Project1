import re
time_str = input()

def get_seconds(time_str):   
    pattern = r"^\d{2}:\d{2}:\d{2}$"
    if not re.match(pattern, time_str):
        return("INCORRECT")
    else:
        hh, mm, ss = time_str.split(':')
        if int(hh) > 24 or int(mm) > 59 or int(ss) > 59:
            return "INCORRECT"
        return int(hh) * 3600 + int(mm) * 60 + int(ss)

print(get_seconds(time_str))