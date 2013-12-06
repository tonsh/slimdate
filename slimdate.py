# coding=utf-8

import datetime

class SlimDatetime(object):

    def __init__(self, date_time):
        self.value = date_time

        self._date = None
        self._time = None
        self._year = None
        self._month = None
        self._day = None
        self._hour = None
        self._minute = None
        self._second = None
        self._weekday = None

    def __repr__(self):
        return '<SlimDatetime class>'

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    @property
    def date(self):
        if not self._date:
            self._date = self.value.date()

        return self._date

    @property
    def time(self):
        if not self._time:
            self._time = self.value.time()

        return self._time

    @property
    def year(self):
        if not self._year:
            self._year = self.value.year

        return self._year

    @property
    def month(self):
        if not self._month:
            self._month = self.value.month

        return self._month

    @property
    def day(self):
        if not self._day:
            self._day = self.value.day

        return self._day

    @property
    def hour(self):
        if not self._hour:
            self._hour = self.value.hour

        return self._hour

    @property
    def minute(self):
        if not self._minute:
            self._minute = self.value.minute

        return self._minute

    @property
    def second(self):
        if not self._second:
            self._second = self.value.second

        return self._second

    @property
    def weekday(self):
        if not self._weekday:
            self._weekday = self.value.weekday() + 1

        return self._weekday

    def change_time(self, hour=0, minute=0, second=0, microsecond=0):
        """ 重置time部分, 未指定地参数将被置0 """
        return self.value.replace(hour=hour,
                                minute=minute,
                                second=second,
                                microsecond=microsecond)

    def beginning_of_day(self):
        return datetime.datetime.combine(self.date, self.time.min)

    def end_of_day(self):
        return datetime.datetime.combine(self.date, self.time.max)

    def beginning_of_hour(self):
        return self.change_time(hour=self.hour)

    def end_of_hour(self):
        time_max = self.time.max
        v_time = datetime.time(self.hour,
                                time_max.minute,
                                time_max.second,
                                time_max.microsecond)

        return datetime.datetime.combine(self.date, v_time)

    def beginning_of_minute(self):
        v_time = datetime.time(self.hour, self.minute)
        return datetime.datetime.combine(self.date, v_time)

    def end_of_minute(self):
        time_max = self.time.max
        v_time = datetime.time(self.hour, self.minute,
                                time_max.second,
                                time_max.microsecond)

        return datetime.datetime.combine(self.date, v_time)

    def last_day(self, days=None):
        days = days or 0
        return self.beginning_of_day() - datetime.timedelta(days=days)

    def next_day(self, days=None):
        days = days or 0
        return self.beginning_of_day() + datetime.timedelta(days=days)

    def last_week(self, weekday=None):
        days = 7
        if weekday:
            days = (7 + self.weekday) - weekday

        return self.beginning_of_day() - datetime.timedelta(days=days)

    def this_week(self, weekday=None):
        days = 0
        if weekday:
            days = weekday - self.weekday

        return self.beginning_of_day() + datetime.timedelta(days=days)

    def next_week(self, weekday=None):
        days = 7
        if weekday:
            days = 7 - self.weekday + weekday

        return self.beginning_of_day() + datetime.timedelta(days=days)

    def last_month(self, monthday=None):
        day = monthday if monthday else self.day 
        year, month, day = self.change_month(self.year, self.month - 1, day)

        return self.beginning_of_day().replace(year=year, month=month, day=day)

    def this_month(self, monthday=None):
        day = monthday if monthday else self.day 
        year, month, day = self.change_month(self.year, self.month, day)

        return self.beginning_of_day().replace(day=day)

    def next_month(self, monthday=None):
        day = monthday if monthday else self.day 
        year, month, day = self.change_month(self.year, self.month + 1, day)

        return self.beginning_of_day().replace(year=year, month=month, day=day)

    @staticmethod
    def change_month(year, month, day):
        if month < 1:
            year -= 1
            month = 12 - abs(month)

        if month > 12:
            year += 1
            month = abs(month) - 12

        n_year = year
        n_month = month + 1
        if n_month > 12:
            n_year += 1
            n_month = 1
        next_month = datetime.datetime(year=n_year, month=n_month, day=1)

        this_month = next_month - datetime.timedelta(days=1)

        # day 不能超过当月最大天数，若大于最大天数则默认为最大天数
        day = min(day, this_month.day)

        return (this_month.year, this_month.month, day)


def str2datetime(date_str, fmt=None):
    if isinstance(date_str, datetime.datetime):
        return date_str
    
    if date_str:
        if fmt:
            return datetime.datetime.strptime(date_str, fmt)

        fmts = list([
            '%Y-%m-%d',
            '%Y-%m-%d %H:%M:%S',
            '%m/%d/%Y',
            '%y%m%d',
            '%Y%m%d',
            '%y-%m-%d',
            '%Y-%m-%d %H:%M:%S:%f',
            '%a %b %d %X +0800 %Y',
        ])
    
        for fmt in fmts:
            try:
                return datetime.datetime.strptime(date_str, fmt)
            except ValueError:
                continue

    return None


def datetime_from_timestamp(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return SlimDatetime(dt)


def datetime_from_string(date_str, fmt=None):
    dt = str2datetime(date_str, fmt)
    return SlimDatetime(dt)

def datetime_from_datetime(date_time):
    return SlimDatetime(date_time)

