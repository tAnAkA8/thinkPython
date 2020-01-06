class Time:
    """Represents the time of day.

    attributes: hour, munute, second
    """

    def time_to_int(time):
        minutes = time.hour * 60 + time.minutes
        seconds = minutes * 60 + time.second
        return seconds

    def int_to_time(second):
        time = Time()
        minute, time.second = divmod(second, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def valid_time(time):
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return False
        return True

    def add_time(t1, t2):
        if not valid_time(t1) or not valid_time(t2):
            raise ValueError, 'invalid Time object in add_time'
        second = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)

    def time_assert(t1, t2):
        assert valid_time(t1) and valid_time(t2)
        seconds = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)