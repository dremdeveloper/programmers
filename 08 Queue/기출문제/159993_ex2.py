from collections import deque
import time

lst = list(range(100000))
dq = deque(range(100000))

# pop(0) 성능 측정
start_time = time.time()
for i in range(100000):
    lst.pop(0)
print("pop(0) 소요 시간: ", time.time() - start_time)  
# pop(0) 소요 시간:  0.7949254512786865

# deque의 popleft() 성능 측정
start_time = time.time()
for i in range(100000):
    dq.popleft()
print("deque의 popleft() 소요 시간: ", time.time() - start_time) 
#deque의 popleft() 소요 시간:  0.0071375370025634766
