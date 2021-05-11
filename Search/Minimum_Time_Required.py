def minTime(machines, goal):
    machines.sort()
    low=1
    high=machines[n-1]*goal
    while low<high:
        midDay=(low+high)//2
        tempGoal=0
        for i in machines:
            tempGoal+=midDay//i
        if tempGoal>=goal:
            high=midDay
        else:
            low=midDay+1
    
    return low
