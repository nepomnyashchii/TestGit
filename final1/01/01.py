import lib
import datetime

exp = 6
created = datetime.datetime(2019, 4, 25, 17, 10, 11)
isEpx = lib.is_expired(created, exp)
print(isEpx)
