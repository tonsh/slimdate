# slimdate 
一个基于 Python 的 datetime 封装的日期处理类。

在项目开发中，经常遇到需求说明里的日期描述，"每天凌晨2点“，”昨天一整天“，"上个月“ 等等，这种时间描述我们都能理解，但用代码描述就变得繁琐无比。slimdate 使日期调用更加人性化，为开发人员解决了很多繁琐的时间换算。

### Example

1. 初始化

	```
    date_time = datetime.datetime(2013, 12, 04, 20, 43, 11)
    d = SlimDate(date_time)
    ```

1. 日期可直接进行比较比较

	```
    d1 = SlimDate(datetime.datetime(2013, 12, 04, 20, 43, 11))
    d2 = SlimDate(datetime.datetime(2013, 12, 04, 20, 43, 10))

    if d1 >= d2:
        pass
    ```
    
1. 方便得获取年，月，日, 时，分，秒 等

	```
    d.year      -> 2013
    d.month     -> 12
    d.day       -> 4
    d.hour      -> 20
    d.minute    -> 43
    d.second    -> 11
    d.weekday   -> 3    周三（weekday 周几？）
    ```

1. 日期处理

	```
    d.beginning_of_day()    -> datetime(2013, 12, 4)
    d.end_of_day()          -> datetime(2013, 12, 4, 23, 59, 59, 999999)

    d.beginning_of_hour()   -> datetime(2013, 12, 4, 20)
    d.end_of_hour()         -> datetime(2013, 12, 4, 20, 59, 59, 999999)

    d.beginning_of_minute() -> datetime(2013, 12, 4, 20, 43)
    d.end_of_minute()       -> datetime(2013, 12, 4, 20, 43, 59, 999999)

    d.last_day()    -> datetime(2013, 12, 4) 前 0 天(凌晨) 即今天
    d.last_day(1)   -> datetime(2013, 12, 3) 昨天
    d.last_day(10)  -> datetime(2013, 11, 24) 前 10 天
    参数也可以是负数，负负得正表示未来的时间, 等价于 next_day
    d.last_day(-10)  -> datetime(2013, 12, 14) 后 10 天

    d.next_day()    -> datetime(2013, 12, 5) 后 0 天即今天
    d.next_day(1)   -> datetime(2013, 12, 5) 明天
    d.next_day(10)  -> datetime(2013, 12, 14) 后 10 天
    d.next_day(-10) -> datetime(2013, 11, 24) 前 10 天

    d.last_week()   -> datetime(2013, 11, 25) 上周周(三)
    d.last_week(1)  -> datetime(2013, 11, 25) 上周周一
    d.last_week(2)  -> datetime(2013, 11, 26) 上周周二
    ... ...
    d.last_week(7)  -> datetime(2013, 12, 1) 上周周日

    d.this_week()   -> datetime(2013, 12, 2) 本周周(三)
    d.this_week(1)  -> datetime(2013, 12, 2) 本周周一
    d.this_week(2)  -> datetime(2013, 12, 4) 本周周二
    d.this_week(7)  -> datetime(2013, 12, 8) 本周周日

    d.next_week()   -> datetime(2013, 12, 9) 下周周(三)
    d.next_week(1)  -> datetime(2013, 12, 9) 下周周一
    d.next_week(2)  -> datetime(2013, 12, 10) 下周周二 
    d.next_week(7)  -> datetime(2013, 12, 15) 下周周日

    d.last_month()  -> datetime(2013, 11, 4) 上月(4)号
    d.last_month(1) -> datetime(2013, 11, 1) 上月1号
    d.last_month(4)) -> datetime(2013, 11, 4) 上月4号
    d.last_month(15) -> datetime(2013, 11, 15) 上月15号
    d.last_month(30)  -> datetime(2013, 11, 30) 上月30号
    d.last_month(31) -> datetime(2013, 11, 30) 上月31号, 11月没有31会返回11月的最后一天
    d1 = SlimDatetime(datetime.datetime(2014, 1, 4))
    d1.last_month() # datetime(2013, 12, 4) 一月的上个月年份也会变化

    d.this_month()      -> datetime(2013, 12, 4) 本月(4)号
    d.this_month(1)     -> datetime(2013, 12, 1) 本月1号
    d.this_month(4)     -> datetime(2013, 12, 4) 本月4号
    d.this_month(15)    -> datetime(2013, 12, 15) 本月15号
    d.this_month(31)    -> datetime(2013, 12, 31) 本月31号

    d1 = SlimDatetime(datetime.datetime(2013, 2, 1))
    d1.this_month(31)   -> datetime(2013, 2, 28) 平年二月最后一天

    d1 = SlimDatetime(datetime.datetime(2012, 2, 1))
    d1.this_month(31)   -> datetime(2012, 2, 29) 闰年二月最后一天

    d.next_month()      -> datetime(2014, 1, 4) 下月(4)号
    d.next_month(1)     -> datetime(2014, 1, 1) 下月1号
    d.next_month(4)     -> datetime(2014, 1, 4) 下月4号
    d.next_month(15)    -> datetime(2014, 1, 15) 下月15号
    d.next_month(31)    -> datetime(2014, 1, 31) 下月31号

    d1 = SlimDatetime(datetime.datetime(2013, 2, 1))
    d1.next_month(31) -> datetime(2014, 2, 28) 平年二月最后一天

    d1 = SlimDatetime(datetime.datetime(2012, 1, 1)
    d1.next_month(31) -> datetime(2014, 2, 28) 平年二月最后一天
    ```
