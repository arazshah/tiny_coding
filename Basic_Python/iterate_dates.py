import datetime

start_date=datetime.date(2023,11,1)
end_date=datetime.date(2023,12,31)

current_date=start_date

while current_date<=end_date:
    print(current_date)
    current_date+=datetime.timedelta(days=1)


