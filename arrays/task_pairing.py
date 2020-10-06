# EPI 17.1
from collections import namedtuple
from typing import List

PairedTasks = namedtuple('PairedTasks', ['Task_0', 'Task_1'])

def optimum_task_assignment(task_duration: List)-> List[PairedTasks]:
    task_duration.sort()

    return [
        # Assumes we have an even number of tasks
        PairedTasks(task_duration[i], task_duration[~i]) for i in range(len(task_duration) // 2)
    ]


result = optimum_task_assignment([5,2,1,6,4,4])
print(result)