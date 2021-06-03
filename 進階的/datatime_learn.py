'''
Author: Swarfte_Tou
Date: 2021-05-16 12:56:46
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-16 13:56:37
FilePath: \Python\python_learn\進階的\datatime.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
import datetime as dt

#% datetime是Python处理日期和时间的标准库。
now_time = dt.datetime.now() #*datetime.now()方法翻回當前的時間
print(f"當前的時間 :{now_time}")
want_day = dt.datetime(2020,8,31,12,30,41)#*可以傳入參數以獲取指定的日期,順序是年,月,日,時,分,秒
print(f"指定的日期 :{want_day}")#&如果不傳入參數的話則默認為0

#!把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time记为0
#!当前时间就是相对于epoch time的秒数，称为timestamp。

#%datetime转换为timestamp
et = want_day.timestamp() #*timestamp()方法把datetime转换为timestamp
print(f"指定日期的timestamp :{et}")

#%timestamp转换为datetime
date = dt.datetime.fromtimestamp(et)#*datetime.fromtimestamp()方法用作把timestamp转换为datetime
print(f"把timestamp轉為datetime :{date}")#&這是+8時區(當前地區)的時間

#%timestamp轉換為UTC标准时区的时间
utc = dt.datetime.utcfromtimestamp(et)#*datetime.utcfromtimestamp()方法用作把timestamp转换为utc標準時區
print(f"把timestamp轉換為utc時區 : {utc}")#&這是+0時區的時間,因為相差了8小時

#%str转换为datetime
day_str = "2021-8-31 12:01:59"
time_format = "%Y-%m-%d %H:%M:%S"#*設置時間的轉換格式,需要和轉換的守符串匹配
dt_time = dt.datetime.strptime(day_str,time_format)#*datetime.strptime()方法用作把str轉換為datetime的形式
print(f"轉為後的時間:{dt_time}")

#%datetime转换为str
str_now = now_time.strftime(time_format)#*strftime()方法用作把datetime轉為str,同strptime一樣,需要傳入一個時間格式化字符串
print(f"datetime轉換為str的結果 : {str_now}")

#%timedelta對datetime加减
H_now_time = now_time + dt.timedelta(days = 3,hours = 4)#*利用timedelta()方法對原有的時間進行加減操作
print(f"更改過後的時間:{H_now_time}")

#%本地时间转换为UTC时间
utc_time = dt.timezone(dt.timedelta(hours = 8))#*创建时区UTC+8:00
utc_now = now_time.replace(tzinfo=utc_time)#*設置為utc+8時
print(f"本地轉換為utc+8時區:{utc_now}")#&如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

#%时区转换
utc0 = dt.datetime.utcnow().replace(tzinfo = dt.timezone.utc)#*利用datetime.utcnow()獲取一個utc時間,並把該時間轉換為utc+0時區
print(f"utc+0時區: {utc0}")

bj_time = utc0.astimezone(dt.timezone(dt.timedelta(hours = 8)))#*利用astimezone把+0時區變為+8時區
print(f"北京時區:{bj_time}")

dj_time = bj_time.astimezone(dt.timezone(dt.timedelta(hours = 9))) #*利用任一時區的時間即可進行時區變換
print(f"東京時區:{dj_time}")