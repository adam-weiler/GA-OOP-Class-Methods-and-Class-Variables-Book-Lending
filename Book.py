from datetime import datetime
import random

# options = [15,20,34923,31,3,5,86,1]
# print(random.choice(options))
# print(random.choice(options))
# print(random.choice(options))
# print(random.choice(options))
# print(random.choice(options))




# now = datetime.now()
# print(now) # datetime.datetime(2018, 12, 14, 17, 7, 5, 190626) <--- the current date and time
# print(now.timestamp()) # 1544825225.190626 <--- the current date and time represented as the number of seconds that have passed since January 1st 1970 at midnight UTC time (that's when they started counting!)
# one_hour = 60 * 60 # 60 seconds times 60 minutes
# print(now.timestamp() + one_hour) # 1544828825.190626 <---- an hour from now (as a "timestamp")
# hour_from_now = now.timestamp() + one_hour
# print(datetime.fromtimestamp(hour_from_now)) # datetime.datetime(2018, 12, 14, 18, 7, 5, 190626) <--- an hour from now (as a datetime obj)



class Book():
    #These are class variables.
    on_shelf = []
    on_loan = []
