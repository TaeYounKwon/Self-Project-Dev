# 가정 1. 프로세스 하나를 사용하여 프로그렘 하나가 꾸준히 돌고 있을 때 
# 특정 상황이 되면 그 프로세스 내에서 프로세스를 생성하여 이메일을 보냄
from multiprocessing import Process, Queue
import time
import datasend 

result = list()

# 시작 프로세스 - 우리 팀의 경우 detect.py
# 아래 함수에서는 50만번중 매 10만번마다 
# 이메일을 보내기 위한 프로세스를 생성 및 보냄
def Detecting_Process(id, begin, end, result):
    print("ID: ", id)
    print("\n----------- Detecting Process Started!\n")
    start = time.perf_counter()
    
    count = 0
    
    for j in range(begin, end):
        th1 = Process(target=Sending_Process, args=(1, 0, 500000, result))
        th1.start()
        th1.join()
        finish = time.perf_counter()
        count += 1
    
    
    
    print("\n----------- Second Process Ended!")
    print(f'\nFinished in {round(finish-start, 2)} second(s)')
    return     

# 이메일을 보내게 되는 프로세스 
# MariaDB에서 고객 데이터를 불러들인 후, 데이터를 이메일로 보냄
def Sending_Process(id, begin, end, result):
    print("\n----------- E-mail & Log Process Started!\n")
    start = time.perf_counter()
    
    datasend.send_alarm()
            
    finish = time.perf_counter()
    print("\n----------- Data Sent Perfectly!!")
    print(f'\nFinished in {round(finish-start, 2)} second(s)')
    return 



# main
if __name__ == '__main__':
    print("Program Started!\n")
    start_origin = time.perf_counter()
    result = Queue()
    
    pro_1 = Process(target=Detecting_Process, args=(1, 0, 500000, result))
    pro_1.start()
    pro_1.join()
    
    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    finish_origin = time.perf_counter()
    print("\n----------- Entire Process Ended!")
    print(f'\nEntire Program Finished in {round(finish_origin-start_origin, 2)} second(s)')
    
    