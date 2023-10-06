from datetime import datetime

"YYYY-MM-DD HH:MM:SS"

date_string="2023-10-05 14:30:00"
print(type(date_string))

parsed_datetime=datetime.strptime(date_string,"%Y-%d-%m %H:%M:%S")

print(type(parsed_datetime))
