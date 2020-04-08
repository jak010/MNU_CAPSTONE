# 2020 03 22
# Feature : 데이터가 수집된 일시 ,총 프로세스 ,총 쓰레드 갯수

import os
import csv
import time
import psutil

from time import localtime

while True:
    time.sleep(0.4)
    cur_time = str(localtime(time.time()).tm_min) + ":" + str(localtime(time.time()).tm_sec)
    # 0~10분 까지
    if len(cur_time.split(":")[0]) == 1:
        print("0분대")
        tarin_path = train_path = "../csvDataSet/TrainSet0.csv"
        if os.path.isfile(train_path):
            try:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)

                # 총 프로세스 , 총 쓰레드 갯수
                tot_process_number = len([x for x in psutil.pids()])
                tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                memory_usage = psutil.virtual_memory()
                print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                f.close()
            except Exception as e:
                print(e)
        else:
            f = open(train_path, "a+", newline='')
            wr = csv.writer(f)
            wr.writerow(["time", "process", "threads", "memory_usage"])
            f.close()

    elif len(cur_time.split(":")[0]) == 2:
        if int(cur_time.split(":")[0][0]) == 1:
            print("10분대")
            tarin_path = train_path = "../csvDataSet/TrainSet1.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()


        elif int(cur_time.split(":")[0][0]) == 2:
            print("20분대")
            tarin_path = train_path = "../csvDataSet/TrainSet2.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        elif int(cur_time.split(":")[0][0]) == 3:
            print("30분대")
            tarin_path = train_path = "../csvDataSet/TrainSet3.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        elif int(cur_time.split(":")[0][0]) == 4:
            print("40분대")
            tarin_path = train_path = "../csvDataSet/TrainSet4.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        elif int(cur_time.split(":")[0][0]) == 5:
            print("50분대")
            tarin_path = train_path = "../csvDataSet/TrainSet5.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        else:
            break
    else:
        break