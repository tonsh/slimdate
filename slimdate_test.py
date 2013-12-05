# coding=utf-8

import datetime
import time
import unittest

from slimdate import (SlimDatetime,
                    str2datetime,
                    datetime_from_timestamp,
                    datetime_from_string)


class SlimDateTestCase(unittest.TestCase):

    def setUp(self):
        self.date_time = datetime.datetime(2013, 12, 04, 20, 43, 11)
        self.slim_date = SlimDatetime(self.date_time)

    def tearDown(self):
        self.date_time = None
        self.slim_date = None

    def test_init(self):
        self.assertEqual(self.slim_date.value, self.date_time)

    def test_lt(self):
        slim_date_2 = SlimDatetime(datetime.datetime.now())
        self.assertTrue(self.slim_date < slim_date_2)

    def test_le(self):
        slim_date_2 = SlimDatetime(datetime.datetime(2013, 12, 04, 20, 43, 11))
        self.assertTrue(self.slim_date <= slim_date_2)

    def test_eq(self):
        slim_date_2 = SlimDatetime(datetime.datetime(2013, 12, 04, 20, 43, 11))
        self.assertTrue(self.slim_date == slim_date_2)

    def test_gt(self):
        slim_date_2 = SlimDatetime(datetime.datetime(2013, 11, 11))
        self.assertTrue(self.slim_date > slim_date_2)

    def test_ge(self):
        slim_date_2 = SlimDatetime(datetime.datetime(2013, 11, 11))
        self.assertTrue(self.slim_date >= slim_date_2)

    def test_date(self):
        self.assertIsNone(self.slim_date._date)
        self.assertEqual(datetime.date(2013, 12, 04), self.slim_date.date)
        self.assertIsNotNone(self.slim_date._date)

    def test_time(self):
        self.assertIsNone(self.slim_date._time)
        self.assertEqual(datetime.time(20, 43, 11), self.slim_date.time)
        self.assertIsNotNone(self.slim_date._time)

    def test_year(self):
        self.assertIsNone(self.slim_date._year)
        self.assertEqual(2013, self.slim_date.year)
        self.assertIsNotNone(self.slim_date._year)

    def test_month(self):
        self.assertIsNone(self.slim_date._month)
        self.assertEqual(12, self.slim_date.month)
        self.assertIsNotNone(self.slim_date._month)

    def test_day(self):
        self.assertIsNone(self.slim_date._day)
        self.assertEqual(4, self.slim_date.day)
        self.assertIsNotNone(self.slim_date._day)

    def test_hour(self):
        self.assertIsNone(self.slim_date._hour)
        self.assertEqual(20, self.slim_date.hour)
        self.assertIsNotNone(self.slim_date._hour)

    def test_minute(self):
        self.assertIsNone(self.slim_date._minute)
        self.assertEqual(43, self.slim_date.minute)
        self.assertIsNotNone(self.slim_date._minute)

    def test_second(self):
        self.assertIsNone(self.slim_date._second)
        self.assertEqual(11, self.slim_date.second)
        self.assertIsNotNone(self.slim_date._second)

    def test_weekday(self):
        self.assertIsNone(self.slim_date._weekday)
        self.assertEqual(3, self.slim_date.weekday)
        self.assertIsNotNone(self.slim_date._weekday)

    def test_beginning_of_day(self):
        expect = datetime.datetime(2013, 12, 4)
        self.assertEqual(expect, self.slim_date.beginning_of_day())

    def test_end_of_day(self):
        expect = datetime.datetime(2013, 12, 4, 23, 59, 59, 999999)
        self.assertEqual(expect, self.slim_date.end_of_day())

    def test_beginning_of_hour(self):
        expect = datetime.datetime(2013, 12, 4, 20)
        self.assertEqual(expect, self.slim_date.beginning_of_hour())

    def test_end_of_hour(self):
        expect = datetime.datetime(2013, 12, 4, 20, 59, 59, 999999)
        self.assertEqual(expect, self.slim_date.end_of_hour())

    def test_beginning_of_minute(self):
        expect = datetime.datetime(2013, 12, 4, 20, 43)
        self.assertEqual(expect, self.slim_date.beginning_of_minute())

    def test_end_of_minute(self):
        expect = datetime.datetime(2013, 12, 4, 20, 43, 59, 999999)
        self.assertEqual(expect, self.slim_date.end_of_minute())

    def test_lastweek(self):
        # 默认
        expect = datetime.datetime(2013, 11, 27)
        self.assertEqual(expect, self.slim_date.last_week())

        # 上周一
        expect = datetime.datetime(2013, 11, 25)
        self.assertEqual(expect, self.slim_date.last_week(1))

        # 上周二
        expect = datetime.datetime(2013, 11, 26)
        self.assertEqual(expect, self.slim_date.last_week(2))

        # 上周三
        expect = datetime.datetime(2013, 11, 27)
        self.assertEqual(expect, self.slim_date.last_week(3))

        # 上周四
        expect = datetime.datetime(2013, 11, 28)
        self.assertEqual(expect, self.slim_date.last_week(4))

        # 上周五
        expect = datetime.datetime(2013, 11, 29)
        self.assertEqual(expect, self.slim_date.last_week(5))

        # 上周六
        expect = datetime.datetime(2013, 11, 30)
        self.assertEqual(expect, self.slim_date.last_week(6))

        # 上周日
        expect = datetime.datetime(2013, 12, 1)
        self.assertEqual(expect, self.slim_date.last_week(7))

    def test_this_week(self):
        # 默认
        expect = datetime.datetime(2013, 12, 4)
        self.assertEqual(expect, self.slim_date.this_week())

        # 本周一
        expect = datetime.datetime(2013, 12, 2)
        self.assertEqual(expect, self.slim_date.this_week(1))

        # 本周二
        expect = datetime.datetime(2013, 12, 3)
        self.assertEqual(expect, self.slim_date.this_week(2))

        # 本周三
        expect = datetime.datetime(2013, 12, 4)
        self.assertEqual(expect, self.slim_date.this_week(3))

        # 本周四
        expect = datetime.datetime(2013, 12, 5)
        self.assertEqual(expect, self.slim_date.this_week(4))

        # 本周五
        expect = datetime.datetime(2013, 12, 6)
        self.assertEqual(expect, self.slim_date.this_week(5))

        # 本周六
        expect = datetime.datetime(2013, 12, 7)
        self.assertEqual(expect, self.slim_date.this_week(6))

        # 本周日
        expect = datetime.datetime(2013, 12, 8)
        self.assertEqual(expect, self.slim_date.this_week(7))

    def test_next_week(self):
        # 默认
        expect = datetime.datetime(2013, 12, 11)
        self.assertEqual(expect, self.slim_date.next_week())

        # 下周一
        expect = datetime.datetime(2013, 12, 9)
        self.assertEqual(expect, self.slim_date.next_week(1))

        # 下周二
        expect = datetime.datetime(2013, 12, 10)
        self.assertEqual(expect, self.slim_date.next_week(2))

        # 下周三
        expect = datetime.datetime(2013, 12, 11)
        self.assertEqual(expect, self.slim_date.next_week(3))

        # 下周四
        expect = datetime.datetime(2013, 12, 12)
        self.assertEqual(expect, self.slim_date.next_week(4))

        # 下周五
        expect = datetime.datetime(2013, 12, 13)
        self.assertEqual(expect, self.slim_date.next_week(5))

        # 下周六
        expect = datetime.datetime(2013, 12, 14)
        self.assertEqual(expect, self.slim_date.next_week(6))

        # 下周日
        expect = datetime.datetime(2013, 12, 15)
        self.assertEqual(expect, self.slim_date.next_week(7))

    def test_last_month(self):
        # 默认
        expect = datetime.datetime(2013, 11, 4)
        self.assertEqual(expect, self.slim_date.last_month())

        # 上月1号
        expect = datetime.datetime(2013, 11, 1)
        self.assertEqual(expect, self.slim_date.last_month(1))

        # 上月4号
        expect = datetime.datetime(2013, 11, 4)
        self.assertEqual(expect, self.slim_date.last_month(4))

        # 上月15号
        expect = datetime.datetime(2013, 11, 15)
        self.assertEqual(expect, self.slim_date.last_month(15))

        # 上月30号
        expect = datetime.datetime(2013, 11, 30)
        self.assertEqual(expect, self.slim_date.last_month(30))

        # 上月31号, 11月没有31会返回11月的最后一天
        expect = datetime.datetime(2013, 11, 30)
        self.assertEqual(expect, self.slim_date.last_month(31))

        # 一月的上个月
        slim_date_2 = SlimDatetime(datetime.datetime(2014, 1, 4))
        expect = datetime.datetime(2013, 12, 4)
        self.assertEqual(expect, slim_date_2.last_month(4))

    def test_this_month(self):
        # 默认
        expect = datetime.datetime(2013, 12, 4)
        self.assertEqual(expect, self.slim_date.this_month())

        # 本月1号
        expect = datetime.datetime(2013, 12, 1)
        self.assertEqual(expect, self.slim_date.this_month(1))

        # 本月4号
        expect = datetime.datetime(2013, 12, 4)
        self.assertEqual(expect, self.slim_date.this_month(4))

        # 本月15号
        expect = datetime.datetime(2013, 12, 15)
        self.assertEqual(expect, self.slim_date.this_month(15))

        # 本月31号
        expect = datetime.datetime(2013, 12, 31)
        self.assertEqual(expect, self.slim_date.this_month(31))

        # 平年二月最后一天
        slim_date_2 = SlimDatetime(datetime.datetime(2013, 2, 1))
        expect = datetime.datetime(2013, 2, 28)
        self.assertEqual(expect, slim_date_2.this_month(31))

        # 闰年二月最后一天
        slim_date_2 = SlimDatetime(datetime.datetime(2012, 2, 1))
        expect = datetime.datetime(2012, 2, 29)
        self.assertEqual(expect, slim_date_2.this_month(31))

    def test_next_month(self):
        # 默认
        expect = datetime.datetime(2014, 1, 4)
        self.assertEqual(expect, self.slim_date.next_month())

        # 下月1号
        expect = datetime.datetime(2014, 1, 1)
        self.assertEqual(expect, self.slim_date.next_month(1))

        # 下月4号
        expect = datetime.datetime(2014, 1, 4)
        self.assertEqual(expect, self.slim_date.next_month(4))

        # 下月15号
        expect = datetime.datetime(2014, 1, 15)
        self.assertEqual(expect, self.slim_date.next_month(15))

        # 下月31号
        expect = datetime.datetime(2014, 1, 31)
        self.assertEqual(expect, self.slim_date.next_month(31))

        # 平年二月最后一天
        slim_date_2 = SlimDatetime(datetime.datetime(2013, 1, 1))
        expect = datetime.datetime(2013, 2, 28)
        self.assertEqual(expect, slim_date_2.next_month(31))

        # 闰年二月最后一天
        slim_date_2 = SlimDatetime(datetime.datetime(2012, 1, 1))
        expect = datetime.datetime(2012, 2, 29)
        self.assertEqual(expect, slim_date_2.next_month(31))

    def test_change_month(self):
        ymd_tuple = SlimDatetime.change_month(2013, 12, 31)
        self.assertEqual((2013, 12, 31), ymd_tuple)

        # 1月的前1个月
        ymd_tuple = SlimDatetime.change_month(2013, 1 - 1, 32)
        self.assertEqual((2012, 12, 31), ymd_tuple)
        # 1月的前4个月
        ymd_tuple = SlimDatetime.change_month(2013, -3, 32)
        self.assertEqual((2012, 9, 30), ymd_tuple)

        # 12月的下1个月
        ymd_tuple = SlimDatetime.change_month(2013, 13, 3)
        self.assertEqual((2014, 1, 3), ymd_tuple)
        # 12月的下4个月
        ymd_tuple = SlimDatetime.change_month(2013, 16, 4)
        self.assertEqual((2014, 4, 4), ymd_tuple)

        # 平年2月的最后一天
        ymd_tuple = SlimDatetime.change_month(2013, 2, 31)
        self.assertEqual((2013, 2, 28), ymd_tuple)

        # 闰年二月最后一天
        ymd_tuple = SlimDatetime.change_month(2012, 2, 31)
        self.assertEqual((2012, 2, 29), ymd_tuple)


class GetSlimDatetimeTestCase(unittest.TestCase):

    def test_str2datetime(self):
        # 参数为日期类型，直接返回
        a_date = datetime.datetime.now()
        self.assertEqual(a_date, str2datetime(a_date))

        # None
        self.assertIsNone(str2datetime(None))
        
        #'%Y-%m-%d'
        a_date = datetime.datetime(2013, 9, 29)
        self.assertEqual(a_date, str2datetime('2013-09-29'))
        
        #'%Y-%m-%d %H:%M:%S'
        a_date = datetime.datetime(2013, 9, 29, 18, 5, 23)
        self.assertEqual(a_date, str2datetime('2013-09-29 18:05:23'))
        
        #'%m/%d/%Y'
        a_date = datetime.datetime(2013, 9, 7)
        self.assertEqual(a_date, str2datetime('09/07/2013'))

        #'%Y%m%d'
        a_date = datetime.datetime(2013, 9, 29)
        self.assertEqual(a_date, str2datetime('20130929'))
        
        #'%y%m%d'
        a_date = datetime.datetime(2013, 9, 29)
        self.assertEqual(a_date, str2datetime('130929'))
        
        #'%y-%m-%d'
        a_date = datetime.datetime(2013, 9, 29)
        self.assertEqual(a_date, str2datetime('13-09-29'))
        
        #'%a %b %d %X +0800 %Y'
        a_date = datetime.datetime(2013, 5, 31, 17, 46, 55)
        self.assertEqual(a_date, str2datetime('Tue May 31 17:46:55 +0800 2013'))
        
        #'%Y-%m-%d %H:%M:%S:%f'
        a_date = datetime.datetime(2013, 9, 29, 18, 5, 23)
        self.assertEqual(a_date, str2datetime('2013-09-29 18:05:23:000'))

    def test_str2datetime_by_fmt(self):
        # None
        self.assertIsNone(str2datetime(None, '%Y-%m-%d'))
        
        #'%Y-%m-%d'
        a_date = datetime.datetime(2013, 9, 29)
        self.assertEqual(a_date, str2datetime('2013-09-29', '%Y-%m-%d'))
        
        #'%Y-%m-%d %H:%M:%S'
        a_date = datetime.datetime(2013, 9, 29, 18, 5, 23)
        self.assertEqual(a_date, str2datetime('2013-09-29 18:05:23'))

    def test_datetime_from_string(self):
        a_date = SlimDatetime(datetime.datetime(2013, 9, 7))
        self.assertEqual(a_date, datetime_from_string('09/07/2013'))

    def test_datetime_from_timestamp(self):
        dt = datetime.datetime(2013, 9, 7)
        a_date = SlimDatetime(dt)

        dt_timestamp = time.mktime(dt.timetuple())
        self.assertEqual(a_date, datetime_from_timestamp(dt_timestamp))

    def test_datetime_from_datetime(self):
        dt = datetime.datetime(2013, 9, 7)
        a_date = SlimDatetime(dt)

        self.assertEqual(a_date, datetime_from_datetime(dt))

