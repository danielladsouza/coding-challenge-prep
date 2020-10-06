# EPI 17.2
from typing import List

def min_waiting_time(service_time : List[int])-> int:
# Given a schedule of service times, we will sort the list
# Return the minimum waiting time
    waiting_time = [0]    # Space Complexity O(N)
    # Sort this in increasing order
    service_time.sort()
    total_waiting_time = 0

    # [2.5.1.3]
    # [1,2,3,5]
    # [0, 0 + 1, 0 + 1 + 2, 0 + 1 + 2 + 3]
    # Waiting_time of a task is the waiting time of the previous task + service time of the previous task
    
    for i in range(1, len(service_time)):
       waiting_time.append(waiting_time[i-1] + service_time[i-1])
       total_waiting_time += waiting_time[i]

    return(total_waiting_time)

wait_time = min_waiting_time([2,5,1,3])
print(wait_time)





