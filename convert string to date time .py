# solution 1 using datetime module
from datetime import datetime
date="oct 14 1997  7:15 AM"
print(type(date))

date_time = datetime.strptime(date," %b %d %Y %I: %M%p")
print(date_time)
print(type(date_time))


# solution 2 using dateutil  module
from dateutil import parser
date_time=parser.parse("oct 14 1997 7 :15 AM")
print(date_time)
print(type(date_time))