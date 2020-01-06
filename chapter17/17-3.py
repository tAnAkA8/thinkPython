class Time():
    """Represents the time of day."""
    def increment(self, seconds):
        seconds += self.time_to_int()
        return Time.int_to_time(seconds)

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def int_to_time(second):
        time = Time()
        minutes, time.second = divmod(second, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def print_time(time):
        print('%02d:%02d:%02d' %
        (time.hour, time.minute, time.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

Time.print_time(start.increment(1))