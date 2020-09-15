from queues import BoundedQueue 
from queues import CircularQueue
import time

def main():
    n = 30000
    bq= BoundedQueue(n)
    cq = CircularQueue(n)
    

    for i in range(0, n):
        bq.enqueue('z')
        cq.enqueue('z')
 
    
    startbqd = time.time()
    for i in range(0, n):
        bq.dequeue()
    endbqd = time.time()
    time_intervalbqd = endbqd - startbqd     
    
    startcqd = time.time()  
    for i in range(0, n):
        cq.dequeue()   
    endcqd = time.time()
    time_intervalcqd = endcqd - startcqd   
    
    print('For Bounded Queue, the total runtime of dequeuing' ,n, ' items is:',
     time_intervalbqd, 'seconds.')
    print('For Circular Queue, the total runtime of dequeuing',n, ' items is:',
    time_intervalcqd, 'seconds.')    
    
   # the bounded queue is quadratic while the ciruqular queue is linear
   
   #For a bounded queue with n items, the dequeue method is O(n) because n elements are being shifted, whereas a circular queue with n items is only changing the idex, not the elements so it will be O(1)
   #if you are looking at these queues as n increases, the time complexity will become quadratic, linear respectively
main()