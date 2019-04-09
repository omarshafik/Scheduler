from proccessClass import Proccess
import queue
def SJF_nonPreemptive(proccessList):
    time = 0
    last_time = -1
    count = 0
    out = []
    #Is_processed = 0
    Q = []
    while(1):
        for index in range(len(processList)):
            if(processList[index].arrival_t <= time and processList[index].arrival_t > last_time):
                Q.append(processList[index])
                count = count + 1
        last_time = time
        Q.sort(key=lambda x: x.duration)
        if(len(Q) > 0):
            #current_process = Q[0]
            #Is_processed = 1
            while(Q[0].duration > 0):
                time = time + 1
                Q[0].duration = Q[0].duration - 1
                out.append(Q[0].name)
            del Q[0]
        else:
            time = time + 1
            out.append("NOP")
        if(len(Q) == 0 and len(processList) == count):
            break
    return out

def SJF_Preemptive(proccessList):
    time = 0
    #last_time = -1
    count = 0
    out = []
    #Is_processed = 0
    Q = []
    while(1):
        for index in range(len(processList)):
            if(processList[index].arrival_t == time):
                Q.append(processList[index])
                count = count + 1
        #last_time = time
        Q.sort(key=lambda x: x.duration)
        if(len(Q) > 0):
            #current_process = Q[0]
            #Is_processed = 1
            Q[0].duration = Q[0].duration - 1
            out.append(Q[0].name)
            if(Q[0].duration == 0):
                del Q[0]
        else:
            out.append("NOP")
        time = time +1
        if(len(Q) == 0 and len(processList) == count):
            break
    return out
