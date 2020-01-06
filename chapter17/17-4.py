class Time():
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

end = Time()
end.hour = 0
end.minute = 0
end.second = 10

print(Time.is_after(start,end))