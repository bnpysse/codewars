# 应该是先求出两者的差，然后用 someTime 减去两者的差，得到正确的时间
# 这里面可能涉及到的就是跨年、跨月、大小月及闰年的关系，这些都主要涉及到天数的问题
from datetime import datetime
someTime = "1995-05-30 13:48"
leavingTime = "2016-04-22 05:32"

some_time = datetime.strptime(someTime, '%Y-%m-%d %H:%M')
leaving_time = datetime.strptime(leavingTime, "%Y-%m-%d %H:%M")
print((some_time - (leaving_time - some_time)).strftime("%Y-%m-%d %H:%M"))
"""
Benjamin recently bought a digital clock at a magic trick shop. The seller never told Ben what was so special about it, but mentioned that one day Benjamin would be faced with a surprise.

Indeed, the clock did surprise Benjamin: without warning, at someTime the clock suddenly started going in the opposite direction! Unfortunately, Benjamin has an important meeting very soon, and knows that at leavingTime he should leave the house so as to not be late. Ben spent all his money on the clock, so has to figure out what time his clock will show when it's time to leave.

Given the someTime at which the clock started to go backwards, find out what time will be shown on the curious clock at leavingTime.

For your convenience, here is the list of months lengths (from January to December, respectively):

Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
Please, note that in leap years February has 29 days.

Example

For someTime = "2016-08-26 22:40" and leavingTime = "2016-08-29 10:00", the output should be
solution(someTime, leavingTime) = "2016-08-24 11:20".

There are 2 days, 11 hours and 20 minutes till the meeting. Thus, the clock will show 2016-08-24 11:20 at the leavingTime.
"""
