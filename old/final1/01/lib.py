import datetime


def is_expired(created, exp):
    my_time = created + datetime.timedelta(0, exp)
    current_time = datetime.datetime.now()
    print(created, current_time, my_time)
    if my_time > current_time:
        return True
    else:
        return False
