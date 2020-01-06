class Time:
    """Represents the time of day.

    attributes: hour, munute, second
    """
    def print_time(t):
        print(('%.2d:%.2d:%.2d') % (t.hour,t.minute,t.second))


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time.print_time()