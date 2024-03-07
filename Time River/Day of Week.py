import datetime

ymd = lambda birth: (int(birth[6:]), int(birth[:2]), int(birth[3:5]))

isLeap = lambda year: True if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) else False
birthdayDate = "02-01-2016"
y, m, d = ymd(birthdayDate)
week = datetime.date(y, m, d).weekday()
for i in range(y + 1, y + 50):
    if isLeap(y) and m == 2 and d == 29:
        if isLeap(i):
            if datetime.date(i, m, d).weekday() == week:
                print(i - y,i,'isLeap')
    else:
        if datetime.date(i, m, d).weekday() == week:
            print(i - y,i)
"""
Whenever you decide to celebrate your birthday you always do this your favorite café, which is quite popular and as such usually very crowded. This year you got lucky: when you and your friend enter the café you're surprised to see that it's almost empty. The waiter lets slip that there are always very few people on this day of the week.

You enjoyed having the café all to yourself, and are now curious about the next time you'll be this lucky. Given the current birthdayDate, determine the number of years until it will fall on the same day of the week.

For your convenience, here is the list of months lengths (from January to December, respectively):

Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
Please, note that in leap years February has 29 days. If your birthday is on the 29th of February, you celebrate it once in four years. Otherwise you birthday is celebrated each year.

Example

For birthdayDate = "02-01-2016", the output should be
solution(birthdayDate) = 5.

February 1 in 2016 is a Monday. The next year in which this same date will be Monday too is 2021. 2021 - 2016 = 5, which is the answer.
"""
