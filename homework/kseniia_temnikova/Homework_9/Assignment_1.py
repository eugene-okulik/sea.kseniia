import datetime

time_to_change = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(time_to_change, '%b %d, %Y - %H:%M:%S')
print(python_date.strftime('%B'))
print(python_date.strftime('%d.%m.%Y, %H:%M'))
