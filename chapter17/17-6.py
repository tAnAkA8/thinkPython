class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%02d:%02d:%02d' %\
        (self.hour, self.minute, self.second)

time = Time(9, 45)
print(time)