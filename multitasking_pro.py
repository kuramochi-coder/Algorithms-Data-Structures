# Task Scheduler
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
# Tasks could be done in any order. Each task is done in one unit of time. 
# For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.


def findTime(tasks, cooldown):
    lastPos = {}
    current = 0

    for task in tasks:
        if task in lastPos:
            if current - lastPos[task] <= cooldown:
                # add cooldown
                current = cooldown + lastPos[task] + 1
        lastPos[task] = current
        current = current + 1
    return current

def findTime2(tasks, cooldown):
     # this question is actually about putting a serialized tasks into parallel task Q
    task_run_time = 1
    lastExcStart = {} # coreId:lastTask's Start Time
    sim_time = 0 
    for task in tasks:
        if task not in lastExcStart:
            # if no task is running on this core, init the queue with cuurent simTime
            lastExcStart[task] = sim_time
        else:
            # if this core had a task. propergate the simTime using the cooldown constrict 
            if sim_time - lastExcStart[task] >= task_run_time + cooldown:
                # if the sim time gap is larger than a cooldown, then you can start this task right away
                lastExcStart[task] = sim_time
            else:
                # if sime time gap is not enough, you need to add a cooldown time to it. 
                lastExcStart[task] += task_run_time + cooldown
                sim_time = lastExcStart[task]
    
    return sim_time + task_run_time

print(findTime([1, 1, 2, 1], 2))
# 7
print(findTime2([1, 1, 2, 1], 2))
# 7