from proccessClass import Proccess
import queue
def roundRobin(processList,q):
    out = []
    Q = queue.Queue(maxsize=len(processList))
    i = 0
    last_i = -1
    count = 0
    for index in range(len(processList)):
        if(processList[index].arrival_t == i):
            if(Q.full() == False):
                Q.put(processList[index])
                count = count + 1
    while(1):
        j = 0
        last_i = i
        Is_processed = 0
        if(Q.empty() == False):
            current_process = Q.get()
            Is_processed = 1
            while(j < q):
                out.append(current_process.name)
                current_process.duration = current_process.duration-1
                j = j + 1
                i = i + 1
                #print(current_process.duration)
                if(current_process.duration == 0):
                    print(current_process.name,i)
                    break
        else:
            out.append("NOP")
            i = i + 1
        for index in range(len(processList)):
            if(processList[index].arrival_t <= i and processList[index].arrival_t > last_i):
                if(Q.full() == False):
                    Q.put(processList[index])
                    count = count + 1
        if(Is_processed == 1):
            if(current_process.duration > 0):
                if(Q.full() == False):
                    Q.put(current_process)
        if(Q.empty() == True and len(processList) == count):
            break
    return out