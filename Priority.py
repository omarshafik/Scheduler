from proccessClass import Proccess
import queue


class Scheduler:
    def priority_preemptive(self, proccess_list):
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

    def priority_nonpreemptive(self, proccess_list):
        p_arrival = sorted(proccess_list, key=lambda x: x.arrival_t)
        ready_queue = []
        running = False     # running proccess
        occupied_slots = []
        time = 0
        while time < Proccess.total_time:
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

            if running:
                running.duration = running.duration - 1
                occupied_slots.append(running.name)

            time = time + 1

        return occupied_slots
