class Time(object):
    """Represents the time of day."""
    def print_time(self):
        print('%02d:%02d:%02d' %
            (self.hour, self.minute, self.second))

start = Time()
start.hour = 9
start.minute = 45
start.second = 0
Time.print_time(start)
start.print_time()