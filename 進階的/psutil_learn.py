import psutil as pt
#%psutil用作时刻监控系统运行的状态
number = pt.cpu_count()#*獲取CPU的逻辑数量
print(number)
pys_number = pt.cpu_count(logical=False)#*獲取CPU的物理核心
print(pys_number)
#*說明這個CPU是4核非超线程
data = pt.cpu_times()#*统计CPU的用户／系统／空闲时间
print(data)
print("=============================================")
# for x in range(10) :#*类似top命令的CPU使用率，每秒刷新一次，累计10次
#     print(pt.cpu_percent(interval = 1,percpu = True))#*interval為間隔,percpu為顯示每個CPU
pys_memory = pt.virtual_memory() #*获取物理内存的信息
print(pys_memory)#*total為總內全,available為可用的內存,percent為使用百分比,used為已使用的內存,free為空閒的內存
change_memory = pt.swap_memory()#*獲取交换内存的信息
print(change_memory)
print("============================================")
check_list = pt.disk_partitions()#*獲取磁盘分区信息
print(check_list)
list_use = pt.disk_usage("/")#*磁盘使用情况
print(list_use)
list_io = pt.disk_io_counters()#*磁盘IO
print(list_io)
print("=====================================")
internet = pt.net_io_counters()#*获取网络读写字节／包的个数
print(internet)
internet_data = pt.net_if_addrs()#*获取网络接口信息
print(internet_data)
internet_stats = pt.net_if_stats()#*获取网络接口状态
print(internet_stats)
internet_now = pt.net_connections()#*获取当前网络连接信息
print(internet_now)
process = pt.pids()#*獲得所有进程ID
print(process)
p = pt.Process(1924)#*获取指定进程ID=1924
print(p.name())#*該進程的名稱
print(p.exe())#*进程exe路径
print(p.cwd())#* 进程工作目录
print(p.cmdline())#* 进程启动的命令行
print(p.ppid()) #*父进程ID
print(p.parent())#*父进程
print(p.children())#*子进程列表
print(p.status())#*进程状态
print(p.username())#*进程用户名
print(p.create_time())#*进程创建时间
print(p.cpu_times())#*进程使用的CPU时间
print(p.memory_info())#*进程使用的内存
print(p.open_files())#*进程打开的文件
print(p.connections())#*进程相关网络连接
print(p.num_threads())#*进程的线程数量
print(p.threads())#*所有线程信息
print(p.environ())#*程环境变量


