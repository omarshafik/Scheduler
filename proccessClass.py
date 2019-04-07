class Proccess:
    procCount = 0

    def __init__(self, priority, arrival_t, duration):
        self.priority = priority
        self.arrival_t = arrival_t
        self.duration = duration
        Proccess.procCount += 1
