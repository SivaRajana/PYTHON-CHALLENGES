date_given = input().split(" ")
Month_list = [['Jan',31],['Feb',28],['Mar',31],['Apr',30],['May',31],['Jun',30],['Jul',31],['Aug',31],['Sep',31],['Oct',30],['Nov',30],['Dec',31]]
month, date, year, time, timestamp = date_given
# print (month, date, year, time, timestamp)
year = int(year)
next_year = year + 1
#finding wether teh entered year is leap or not
if ( year % 100 == 0 and year % 400 == 0):
    Month_list[1][1] = 29
elif (year % 4 == 0):
    Month_list[1][1] = 29
    
index = 0
for i in Month_list:
    if (i[0] == month):
        month_index = index
    index = index + 1
        
total_days = 0
for j in range(month_index + 1, 12):
        total_days = total_days + Month_list[j][1]
total_days = total_days + (Month_list[month_index][1] - int(date))
# print (total_days)

hours_min_list = time.split(":")
hours, minutes = hours_min_list
if (timestamp == "AM"):
    hours = 24 - int(hours) - 1
else:
    hours = 12 - int(hours) - 1
minutes = 60 - int(minutes)


hours = hours + (total_days * 24)
print ("{} hours {} minutes".format(hours, int(minutes)))




        
