from proccessClass import Proccess
import queue


class Scheduler:

    def SJF_nonPreemptive(self, processList):
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

    def SJF_Preemptive(self, processList):
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
            time = time + 1
            if(len(Q) == 0 and len(processList) == count):
                break
        return out

    def roundRobin(self, processList, q):
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
                    # print(current_process.duration)
                    if(current_process.duration == 0):
                        print(current_process.name, i)
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

    def priority_preemptive(self, proccess_list):
        noop = True
        p_arrival = sorted(proccess_list, key=lambda x: x.arrival_t)
        ready_queue = []
        running = False     # running proccess
        occupied_slots = []
        time = 0
        while p_arrival or ready_queue or running:
            while p_arrival and p_arrival[0].arrival_t <= time:
                ready_queue.append(p_arrival[0])
                del p_arrival[0]
            if ready_queue:
                ready_queue.sort(key=lambda x: x.priority)

            if ready_queue and not running:
                running = ready_queue[0]
                del ready_queue[0]
                noop = False

            if not ready_queue and not running:
                noop = True

            if running:

                if running.duration <= 0:
                    if ready_queue:
                        running = ready_queue[0]
                        del ready_queue[0]
                    else:
                        running = False
                        noop = True

                elif ready_queue and ready_queue[0].priority < running.priority:
                    ready_queue.append(running)
                    running = ready_queue[0]
                    del ready_queue[0]
                    if ready_queue:
                        ready_queue.sort(key=lambda x: x.priority)

            if running:
                running.duration = running.duration - 1
                occupied_slots.append(running.name)

            if noop and p_arrival:
                occupied_slots.append("NOP")

            time = time + 1

        return occupied_slots

    def priority_nonpreemptive(self, proccess_list):
        noop = True
        p_arrival = sorted(proccess_list, key=lambda x: x.arrival_t)
        ready_queue = []
        running = False     # running proccess
        occupied_slots = []
        time = 0
        while p_arrival or ready_queue or running:
            while p_arrival and p_arrival[0].arrival_t <= time:
                ready_queue.append(p_arrival[0])
                del p_arrival[0]
            if ready_queue:
                ready_queue.sort(key=lambda x: x.priority)

            if ready_queue and not running:
                running = ready_queue[0]
                del ready_queue[0]
                noop = False

            if not ready_queue and not running:
                noop = True

            if running:

                if running.duration <= 0:
                    if ready_queue:
                        running = ready_queue[0]
                        del ready_queue[0]
                    else:
                        running = False
                        noop = True

            if running:
                running.duration = running.duration - 1
                occupied_slots.append(running.name)

            if noop and p_arrival:
                occupied_slots.append("NOP")

            time = time + 1

        return occupied_slots
