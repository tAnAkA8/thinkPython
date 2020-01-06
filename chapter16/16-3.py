class Time:
    """Represents the time of day.

    attributes: hour, munute, second
    """
    def increment(time, seconds):
        time.second += seconds
#80
        if time.second >= 60:
            a = seconds / 60
            b = seconds % 60
            time.second -= 60 * a
            time.second += b
            time.minute += 1 * a

        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1

def print_time(t):
    print(('%.2d:%.2d:%.2d') % (t.hour,t.minute,t.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

start.increment(80)
print_time(start)