from proccessClass import Proccess
import queue


def priority_preemptive(proccess_list):
    p_arrival = sorted(proccess_list, key=lambda x: x.arrival_t)
    ready_queue = []
    running = False     # running proccess
    occupied_slots = []
    time = 0
    while p_arrival or ready_queue or running:
        while p_arrival and p_arrival[0].arrival_t <= time:
            ready_queue.append(p_arrival[0])
            del p_arrival[0]
        ready_queue.sort(key=lambda x: x.priority)

        if ready_queue and not running:
            running = ready_queue[0]
            del ready_queue[0]

        if running:

            if running.duration <= 0:
                if ready_queue:
                    running = ready_queue[0]
                    del ready_queue[0]
                else:
                    running = False

            elif ready_queue and ready_queue[0].priority < running.priority:
                ready_queue.append(running)
                running = ready_queue[0]
                del ready_queue[0]
                if ready_queue:
                    ready_queue.sort(key=lambda x: x.priority)

            if running:
                running.duration = running.duration - 1
                occupied_slots.append(running.name)

        time = time + 1

    return occupied_slots


p = priority_preemptive({Proccess(0, 5, "U1", 5), Proccess(
    2, 4, "U2", 3), Proccess(5, 5, "U3", 1), Proccess(5, 1, "U4", 2)})

print(p)
