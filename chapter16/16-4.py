class Time:
    """Represents the time of day.

    attributes: hour, munute, second
    """
    def add_time(t1, t2):
        seconds = Time.time_to_int(t1) + Time.time_to_int(t2)
        return Time.int_to_time(seconds)

    def time_to_int(time):
        m = time.hour * 60 + time.minute
        s = m * 60 + time.second
        return s

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def print_time(self):
        print('%02d:%02d:%02d' %
            (self.hour, self.minute, self.second))


start = Time()
start.hour = 1
start.minute = 40
start.second = 0

Time.print_time(Time.add_time(start,start))