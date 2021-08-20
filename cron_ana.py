from collections import defaultdict
import csv


def init_times():
    times = dict()
    # 分
    # 小时
    # 每月 1-31
    # 月份
    # 每周 1-7
    hours = 0
    minute = 0
    for hour in range(0, 24):
        for minute in range(0, 60):
            k = "{:0>2}:{:0>2}".format(hour, minute)
            times[k] = list()
    return times

TIME_INFO = init_times()

def main():
    file = open("test.txt", mode="r")
    lines = file.readlines()
    for line in lines:
        if line.startswith("#"):
            continue
        line = line.strip()
        if not line:
            continue
        print(line)
        info = line.split(" ")
        if not info[6]:
            continue
        format_line(info[0], info[1], info[2], info[3], info[4], info[6])


def format_line(minute, hour, month_day, month, week_day, task):
    if minute == "*":
        m = [i for i in range(0, 60)]
    elif minute.isdigit():
        m = [int(minute)]
    else:
        temp_m = minute.split("*/")
        m = [i for i in range(0, 60, int(temp_m[1]))]
        
    if hour == "*":
        h = [i for i in range(0, 24)]
    elif hour.isdigit():
        h = [int(hour)]
    elif hour.startswith("*/"):
        temp_h = hour.split("*/")
        h = [i for i in range(0, 24, int(temp_h[1]))]
    elif "," in hour:
        h = [int(i) for i in hour.split(",")]
    elif "-" in hour:
        temp_h = hour.split("-")
        h = [i for i in range(int(temp_h[0]), int(temp_h[1])+ 1)]
    
    
    if month_day == "*":
        m_d = ""
    elif month_day.startswith("*/"):
        temp_m_d = month_day.split("*/")
        m_d = "每月{}号 ".format(temp_m_d[1])
    elif month_day.isdigit():
        m_d = "每月{}号 ".format(month_day)
    else:
        print(month_day)
    
    if month == "*":
        mo = ""
    elif month.startswith("*/"):
        temp_mo = month.split("*/")
        mo = "每{}月 ".format(temp_mo[1])
    else:
        print(month)
    
    if week_day == "*":
        wd = ""
    elif week_day.startswith("*/"):
        temp_mo = week_day.split("*/")
        wd = "每周{} ".format(temp_mo[1])
    elif "," in week_day:
        wd = "每周{} ".format(week_day)
    elif "-" in week_day:
        wd = "每周{} ".format(week_day)
    elif week_day.isdigit():
        wd = "每周{} ".format(week_day)
    else:
        print(week_day)
    
    print(mo, m_d, wd, h,m, task)
    
    for i in h:
        for j in m:
            key = "{:0>2}:{:0>2}".format(i, j)
            t = mo + m_d + wd + task
            TIME_INFO[key].append(t)
    
    
if __name__ == '__main__':
    main()
    
    headers = ['time', 'index', 'task','table']
    f =  open('test2.csv','w',newline='', encoding="utf-8")
    f_csv = csv.DictWriter(f,headers)
    f_csv.writeheader()
    
    resp = list()
    for k in TIME_INFO:
        tasks = sorted(TIME_INFO[k])
        for i,v in enumerate(tasks):
            resp.append({
                "time": k,
                "index": i,
                "task": v,
                "table": ""
            })
    f_csv.writerows(resp)
    f.close()

