class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(time):
        print('%02d:%02d:%02d' %
        (time.hour, time.minute, time.second))

time = Time()
time.print_time()

time = Time(9, 45)
time.print_time()