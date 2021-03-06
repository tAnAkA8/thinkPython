class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
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

    def increment(self, seconds):
        seconds += self.time_to_int()
        return Time.int_to_time(seconds)

    def __str__(self):
        return '%02d:%02d:%02d' %\
        (self.hour, self.minute, self.second)

    def __radd__(self, other):
        return self.__add__(other)

start = Time(9, 45)
duration = Time(1, 35)

print(start + duration)
print(start + 1337)
print(1337 + start)